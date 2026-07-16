<script setup lang="ts">
import { computed } from 'vue'
import DefaultTheme from 'vitepress/theme'
import { useData } from 'vitepress'
import ReadControls from './ReadControls.vue'
import ReadTracker from './ReadTracker.vue'

const { Layout } = DefaultTheme
const { page } = useData()

// relativePath is independent of the deployed base path, which is '/' locally
// but '/<repo>/' on GitHub Pages.
const isHome = computed(() => page.value.relativePath === 'index.md')
</script>

<template>
  <Layout>
    <template #layout-top>
      <ReadTracker />
    </template>
    <template #doc-before>
      <ReadControls v-if="isHome" />
    </template>
  </Layout>
</template>
