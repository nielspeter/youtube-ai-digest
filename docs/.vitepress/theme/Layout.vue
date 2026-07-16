<script setup lang="ts">
import { computed } from 'vue'
import DefaultTheme from 'vitepress/theme'
import { useRoute } from 'vitepress'
import ReadControls from './ReadControls.vue'
import ReadTracker from './ReadTracker.vue'

const { Layout } = DefaultTheme
const route = useRoute()

const isHome = computed(() => {
  const path = route.path.replace(/index\.html$/, '').replace(/\.html$/, '')
  return path === '/' || path === ''
})
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
