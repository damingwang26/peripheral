<template>
  <div class="topBar-container flex h-30">
    <div class="topBar-logo">
      <AkmeUltimateLogo />
    </div>
    <div class="topBar-search flex">
      <input class="topBar-search-input" placeholder="搜索 / Search" type="text">
    </div>
    <div class="flex">
      <div class="topBar-item flex" @click="testLoading">首页</div>
      <div class="topBar-item flex">商品</div>
      <div class="topBar-item flex">服务</div>
      <div class="topBar-item flex">关于</div>
      <div class="topBar-item-icon topBar-item-fold flex">
        <NIcon class="lang-btn"><Menu /></NIcon>
      </div>
      <div class="topBar-item-icon flex">
        <NIcon class="lang-btn"><World /></NIcon>
        <div class="topBar-item-list">
          <div class="topBar-i-list-item">中文</div>
          <div class="topBar-i-list-item">English</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { VueElement } from 'vue';
import { NIcon } from 'naive-ui';
import { World, Menu } from '@vicons/tabler'
import AkmeUltimateLogo from './Logo/AkmeUltimate.vue'

const emit = defineEmits(['loaded', 'loading'])

function testLoading() {
  emit('loading')
  setTimeout(() => {
    emit('loaded')
  }, 1000)
}
</script>

<style lang="less" scoped>
.topBar-logo {
  color: #ffffff;
  width: 100px;
  height: 50px;
}

.topBar-container {
  position: fixed;
  justify-content: space-between;
  width: 100vw;
  padding: 20px 40px;
  background-image: linear-gradient(180deg, var(--dark-gray), #0e605a00 80%);
}

.topBar-item {
  padding: 40px 0;
  margin-left: 40px;
  padding-right: 0;
  cursor: pointer;
  font-size: 1.2rem;
  font-weight: 400;
  justify-content: end;
  text-align: end;
  flex-shrink: 0;
  background-image: linear-gradient(0deg, var(--primary-color), var(--primary-color));
  background-size: 100% 0px;
  background-repeat: no-repeat;
  background-position: 0 100px;
  transition-duration: .4s;
}

.topBar-item:hover {
  background-size: 100% 2px;
  background-position: 0 70px;
}

.topBar-search {
  position: absolute;
  width: 30vw;
  left: 50%;
  transform: translateX((-50%));
}

.topBar-search-input {
  width: 100%;
  background-color: transparent;
  border: 2px solid #ffffff40;
  height: 40px;
  width: 100%;
  padding: 20px;
  outline: none;
  transition-duration: .4s;
}

.topBar-search-input:focus {
  background-color: #ffffff20;
}

.topBar-item-icon {
  margin-left: 40px;
  font-size: 1.8rem;
  background-color: rgba(255, 255, 255, 0.35);
  border-radius: 100px;
  padding: 5px;
  cursor: pointer;
  position: relative;
}

.topBar-item-list {
  position: absolute;
  top: 30px;
  padding-top: 20px;
  pointer-events: none;
  opacity: 0;
  transition-duration: .4s;
}

.topBar-item-icon:hover .topBar-item-list {
  pointer-events: all;
  opacity: 1;
}

.topBar-i-list-item {
  font-size: 1rem;
  padding: 10px;
  text-align: center;
  background-color: rgba(255, 255, 255, 0.2);
}

.topBar-i-list-item:hover {
  background-color: rgba(255, 255, 255, 0.3);
}

.topBar-item-fold {
  display: none;
}

@media (max-width: 1200px) {
  .topBar-item {
    margin-left: 20px;
  }
}

@media (max-width: 1000px) {
  .topBar-item {
    margin-left: 10px;
  }
}

@media (max-width: 900px) {
  .topBar-item {
    display: none;
  }

  .topBar-item-fold {
    display: inherit;
  }

  .topBar-item-icon {
    margin-left: 20px;
  }
}

@media (max-width: 500px) {
  .topBar-search {
    display: none;
  }
}
</style>