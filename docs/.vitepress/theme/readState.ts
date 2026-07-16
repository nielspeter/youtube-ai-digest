import { computed, ref } from 'vue'

const READ_KEY = 'yt-digest:read:v1'
const HIDE_KEY = 'yt-digest:hide-read:v1'

// Empty on the server: the site is prerendered, so read state can only be
// resolved after hydration. Rendering it during SSR would mismatch.
const readIds = ref<Set<string>>(new Set())
const hideRead = ref(false)

let loaded = false

function safeRead(key: string): string | null {
  try {
    return localStorage.getItem(key)
  } catch {
    // Storage can throw when disabled (private mode, blocked cookies).
    return null
  }
}

function safeWrite(key: string, value: string): void {
  try {
    localStorage.setItem(key, value)
  } catch {
    // Losing persistence is survivable; breaking the page is not.
  }
}

/** Hydrate from localStorage. Safe to call repeatedly; only the first run reads. */
export function loadReadState(): void {
  if (loaded || typeof window === 'undefined') return
  loaded = true

  const raw = safeRead(READ_KEY)
  if (raw) {
    try {
      const parsed = JSON.parse(raw)
      if (Array.isArray(parsed)) readIds.value = new Set(parsed.filter((id) => typeof id === 'string'))
    } catch {
      // Corrupt payload: start clean rather than wedge the page on every load.
    }
  }
  hideRead.value = safeRead(HIDE_KEY) === '1'
}

function persistRead(): void {
  safeWrite(READ_KEY, JSON.stringify([...readIds.value]))
}

/** Pull the video id out of a card href like `summaries/langchain/3lb_4OEOykc`. */
export function videoIdFromHref(href: string): string | null {
  const path = href.split(/[?#]/)[0].replace(/\.html$/, '').replace(/\/$/, '')
  const parts = path.split('/').filter(Boolean)
  return parts.length ? parts[parts.length - 1] : null
}

export function isRead(id: string): boolean {
  return readIds.value.has(id)
}

export function markRead(id: string): void {
  if (!id || readIds.value.has(id)) return
  readIds.value.add(id)
  persistRead()
}

export function markUnread(id: string): void {
  if (!readIds.value.delete(id)) return
  persistRead()
}

export function toggleRead(id: string): void {
  readIds.value.has(id) ? markUnread(id) : markRead(id)
}

export function clearAll(): void {
  readIds.value = new Set()
  persistRead()
}

export function markAllRead(ids: string[]): void {
  const next = new Set(readIds.value)
  ids.forEach((id) => next.add(id))
  readIds.value = next
  persistRead()
}

export function setHideRead(value: boolean): void {
  hideRead.value = value
  safeWrite(HIDE_KEY, value ? '1' : '0')
}

export const readCount = computed(() => readIds.value.size)
export const readSet = computed(() => readIds.value)
export const hideReadEnabled = computed(() => hideRead.value)
