<template>
  <div class="home-container">
    <!-- 滚动展示 -->
    <div class="home-slide-container flex">
      <div v-for="(item, index) in slideList" :key="index" :class="slideViewClassEnum[(index == currentDisplaySlide) ? 1 : 0]">
        <img class="home-slide-item-img flex-1" :src="serverURL + '/images/' + item.image" />
        <div class="home-slide-item-right flex-1 flex-col">
          <div class="home-slide-item-name">{{ item.name }}</div>
          <div class="home-slide-item-desc">{{ item.description }}</div>
          <NButton type="primary" class="home-slide-item-btn">立即选购</NButton>
        </div>
      </div>
    </div>

    <!-- 滚动指示器 + 切换器 -->
    <div class="home-slide-indicator-container flex w-full mt-6">
      <NIcon @click="handleSlideSwitch(currentDisplaySlide > 0 ? currentDisplaySlide - 1 : slideListLength - 1)" class="home-s-i-arrow p-2 m-2"><ChevronLeft /></NIcon>
      <NIcon v-for="(item, index) in slideList" :key="index" @click="handleSlideSwitch(index)" :class="slideIndicatorClassEnum[(index == currentDisplaySlide) ? 1 : 0]">
        <Circle />
      </NIcon>
      <NIcon @click="handleSlideSwitch(currentDisplaySlide < slideListLength - 1 ? currentDisplaySlide + 1 : 0)" class="home-s-i-arrow p-2 m-2"><ChevronRight /></NIcon>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { getListData, postListData } from '@/global/global_api';
import globalEnvSettings from '@/global/global_arg';
import { NButton, NIcon } from 'naive-ui';
import { Circle, ChevronLeft, ChevronRight } from '@vicons/tabler';

const serverURL = globalEnvSettings.server
const slideList = ref<any>([])
const slideListLength = ref<number>(0)
const currentDisplaySlide = ref<number>(0)

interface classType {
  [key: string | number] : any
}

const slideViewClassEnum = ref<classType>({
  0: 'home-slide-item home-slide-item-hide flex',
  1: 'home-slide-item flex'
})

const slideIndicatorClassEnum = ref<classType>({
  0: 'home-slide-indicator p-2',
  1: 'home-slide-indicator home-slide-indicator-current p-2'
})

const emit = defineEmits(['loaded', 'loading'])

function handleSlideSwitch(target: number) {
  currentDisplaySlide.value = target
}

onMounted(() => {
  try {
    emit('loading')
    getListData('/products').then((res) => {
      slideList.value = res.data
      slideListLength.value = res.data.length
      emit('loaded')
    })
  }
  catch(e) {
    console.log(e)
  }
})
</script>

<style lang="less" scoped>
.home-slide-item {
  overflow: hidden;
  width: 100%;
  transition: all .4s, width 0s;
}

.home-slide-item-hide {
  opacity: 0;
  background-color: transparent;
  width: 0px;
  height: 100%;
  filter: blur(10px);
}

.home-slide-item-hide .home-slide-item-img {
  transform: translateX(-100px);
  opacity: 0;
}

.home-container {
  width: 90vw;
  max-width: 1300px;
  margin: auto;
}

.home-slide-container {
  width: 100%;
  height: 400px;
  overflow: hidden;
  background-color: rgba(255, 255, 255, 0.136);
  transition: all .4s;
}

.home-slide-container:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

.home-slide-item-img {
  max-height: 400px;
  width: auto;
  object-fit: cover;
  filter: drop-shadow(10px 10px 5px #00000040);
  transition: all 2s;
}

.home-slide-item-name {
  font-size: 2.2rem;
  font-weight: 900;
  transition: all 1s;
}

.home-slide-item-desc {
  transition: all 1s .2s;
}

.home-slide-item-btn {
  margin-top: 20px;
  font-weight: 700;
  transition: all 1s .7s;
}

.home-slide-item-hide .home-slide-item-name,
.home-slide-item-hide .home-slide-item-desc,
.home-slide-item-hide .home-slide-item-btn {
  transform: translateY(50px);
  opacity: 0;
}

.home-slide-item-right {
  flex-shrink: 0;
  min-width: 500px;
}

.home-slide-indicator {
  color: var(--light-gray);
  cursor: pointer;
  box-sizing: content-box;
}

.home-slide-indicator-current {
  color: white;
  cursor: default;
}

.home-s-i-arrow {
  border-radius: 20px;
  box-sizing: content-box;
  transition-duration: .4s;
  cursor: pointer;
}

.home-s-i-arrow:hover {
  background-color: var(--bkg-white-t);
}

@media (max-width: 900px) {
  .home-slide-container {
    height: 600px;
  }
  
  .home-slide-item {
    overflow: hidden;
    flex-direction: column;
    height: 100%;
    justify-content: start;
  }

  .home-slide-item-img {
    width: 100%;
    max-height: 380px;
    object-fit: cover;
    flex: 1;
  }

  .home-slide-item-right {
    width: 100%;
    min-width: 0px;
    box-sizing: border-box;
    padding: 20px;
    justify-content: start;
    flex-shrink: 0;
    flex: 0;
  }
}
</style>