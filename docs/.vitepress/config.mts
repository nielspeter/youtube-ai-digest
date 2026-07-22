import { defineConfig } from 'vitepress'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const dirname = path.dirname(fileURLToPath(import.meta.url))
const summariesDir = path.resolve(dirname, '../summaries')

function titleFromFrontmatter(file: string, fallback: string): { title: string; published: string } {
  const text = fs.readFileSync(file, 'utf-8')
  const m = text.match(/^---\n([\s\S]*?)\n---/)
  const fm = m ? m[1] : ''
  const title = fm.match(/^title:\s*"?(.*?)"?\s*$/m)?.[1] ?? fallback
  const published = fm.match(/^published:\s*"?(.*?)"?\s*$/m)?.[1] ?? ''
  return { title, published }
}

// Build the sidebar directly from the generated files so it always reflects
// what exists on disk, grouped by channel and newest-first.
function buildSidebar() {
  if (!fs.existsSync(summariesDir)) return []
  return fs
    .readdirSync(summariesDir, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => {
      const channelDir = path.join(summariesDir, d.name)
      const items = fs
        .readdirSync(channelDir)
        .filter((f) => f.endsWith('.md'))
        .map((f) => {
          const id = f.replace(/\.md$/, '')
          const { title, published } = titleFromFrontmatter(path.join(channelDir, f), id)
          return { text: title, link: `/summaries/${d.name}/${id}`, published }
        })
        .sort((a, b) => (a.published < b.published ? 1 : -1))
        .map(({ text, link }) => ({ text, link }))
      return { text: d.name, collapsed: true, items }
    })
    .sort((a, b) => a.text.localeCompare(b.text))
}

// For GitHub project pages set SITE_BASE="/<repo-name>/" in the workflow.
const base = process.env.SITE_BASE || '/'

export default defineConfig({
  title: 'YouTube Digest',
  description: 'Auto-generated summaries of subscribed YouTube channels.',
  base,
  // Without an explicit icon the browser falls back to /favicon.ico at the
  // origin root, which is outside `base` and always 404s. Links in `head` are
  // not rewritten for base, so it is applied by hand.
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: `${base}favicon.svg` }],
    // Keep the digest out of search engines. This is a GitHub *project* page
    // served under a subpath, so a robots.txt (only honored at the domain root)
    // can't cover it — a per-page noindex is the reliable signal. noindex drops
    // the page from results; nofollow stops crawlers discovering onward via its
    // links. Applied to every generated page.
    ['meta', { name: 'robots', content: 'noindex, nofollow' }],
  ],
  lastUpdated: true,
  cleanUrls: true,
  ignoreDeadLinks: true, // content is machine-generated; don't fail the build on odd links
  themeConfig: {
    nav: [{ text: 'Home', link: '/' }],
    sidebar: buildSidebar(),
    // detailedView renders the matching text in the results list. Without it a
    // result is only its heading, which for a transcript hit says nothing about
    // what actually matched.
    search: { provider: 'local', options: { detailedView: true } },
    outline: { level: [2, 3] },
  },
})
