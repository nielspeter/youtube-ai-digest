<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useData } from 'vitepress'
import { loadReadState, readSet, toggleRead } from './readState'

const { frontmatter } = useData()

// Read state only exists after hydration, so nothing renders during SSR.
const ready = ref(false)
const videoId = computed(() => {
  const id = frontmatter.value?.video_id
  return typeof id === 'string' && id ? id : null
})
const read = computed(() => !!videoId.value && readSet.value.has(videoId.value))

onMounted(() => {
  loadReadState()
  ready.value = true
})
</script>

<template>
  <div v-if="ready && videoId" class="read-mark-bar">
    <button
      type="button"
      class="read-mark-btn"
      :class="{ 'is-read': read }"
      @click="toggleRead(videoId)"
    >
      {{ read ? '✓ Read — mark unread' : 'Mark as read' }}
    </button>
  </div>
</template>
