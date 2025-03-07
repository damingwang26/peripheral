<template>
  <n-config-provider :theme="darkTheme" :themeOverrides="themeOverrides">
    <div>
      <loadingScreen :b-show-loading="bShowLoading" />
      <topBar @loaded="handleLoaded" @loading="handleLoading" />
      <div class="h-40"></div>
      <RouterView @loaded="handleLoaded" @loading="handleLoading" />
    </div>
  </n-config-provider>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { darkTheme } from 'naive-ui'
import topBar from '@/components/topBar.vue'
import loadingScreen from './components/loadingScreen.vue';
import { ref } from 'vue';

const themeOverrides = {
  common: {
    primaryColor: '#81D8D0'
  }
}

const bShowLoading = ref<boolean>(false)

function handleLoaded() {
  bShowLoading.value = false
}

function handleLoading() {
  bShowLoading.value = true
}
</script>

<style lang="less" scoped></style>
