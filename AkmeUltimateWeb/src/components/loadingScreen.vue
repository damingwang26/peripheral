<template>
  <div ref="loadingScreenRef" class="loading-fullscreen w-screen h-screen flex flex-col">
    <AkmeUltimateLogo class="loading-icon" />
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'; 
import AkmeUltimateLogo from './Logo/AkmeUltimate.vue';

const props = defineProps(['bShowLoading'])
const loadingScreenRef = ref<any>()

watch(
  () => props.bShowLoading,
  (newVal, oldVal) => {
    if (newVal) {
      loadingScreenRef.value.style = 'opacity: 1; filter: blur(0);'
    }
    else {
      loadingScreenRef.value.style = 'opacity: 0; filter: blur(10px);'
      setTimeout(() => {
        loadingScreenRef.value.style = 'opacity: 0; filter: blur(10px); display: none;'
      }, 800)
    }
  }
);
</script>

<style lang="less" scoped>
@keyframes loading-icon-anim {
  0% {
    opacity: 0;
    transform: scale(.9);
    filter: drop-shadow(0 0 1px rgba(255, 255, 255, 0.8));
  }
  15% {
    opacity: 1;
    transform: scale(1);
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.8));
  }
  40% {
    opacity: 1;
    transform: scale(1);
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.8));
  }
  45% {
    opacity: 1;
    transform: scale(1);
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.4));
  }
  50% {
    opacity: 1;
    transform: scale(1);
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.8));
  }
  55% {
    opacity: 1;
    transform: scale(1);
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.4));
  }
  60% {
    opacity: 1;
    transform: scale(1);
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.8));
  }
  85% {
    opacity: 1;
    transform: scale(1);
    filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.8));
  }
  100% {
    opacity: 0;
    transform: scale(.9);
    filter: drop-shadow(0 0 1px rgba(255, 255, 255, 0.8));
  }
}

.loading-fullscreen {
  background: linear-gradient(135deg, var(--dark-gray), var(--primary-color-dark));
  position: fixed;
  z-index: 999;
  opacity: 0;
  filter: blur(10px);
  transition-duration: .4s;
}

.loading-icon {
  width: 200px;
  animation: loading-icon-anim 10s infinite;
}
</style>