<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import {
  clearAll,
  hideReadEnabled,
  loadReadState,
  markAllRead,
  readSet,
  setHideRead,
  videoIdFromHref,
} from './readState'

// Rendered only after mount: read counts depend on localStorage, which does not
// exist while the page is prerendered.
const ready = ref(false)
const cardIds = ref<string[]>([])

// Read ids persist for videos no longer on the index, so count against the
// cards actually present rather than the whole stored set.
const unread = computed(() => cardIds.value.filter((id) => !readSet.value.has(id)).length)

onMounted(() => {
  loadReadState()
  cardIds.value = [...document.querySelectorAll<HTMLAnchorElement>('a.video-card')]
    .map((c) => videoIdFromHref(c.getAttribute('href') ?? ''))
    .filter((id): id is string => !!id)
  ready.value = true
})
</script>

<template>
  <div v-if="ready" class="read-controls">
    <span class="read-stat">{{ unread }} unread of {{ cardIds.length }}</span>
    <label class="read-toggle">
      <input
        type="checkbox"
        :checked="hideReadEnabled"
        @change="setHideRead(($event.target as HTMLInputElement).checked)"
      />
      Hide read
    </label>
    <button type="button" @click="markAllRead(cardIds)">Mark all read</button>
    <button type="button" :disabled="!readSet.size" @click="clearAll()">Reset</button>
  </div>
</template>
