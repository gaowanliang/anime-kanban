<script setup>
import { ref } from 'vue'
import BackgroundSwitch from '../components/BackgroundSwitch.vue'
import AnimeCard from '../components/AnimeCard.vue'
import { useAnimeData } from '../composables/useAnimeData'

const showBackground = ref(true)
const { animes, resetAnimes, removeAnime } = useAnimeData()

const toggleBackground = () => {
  showBackground.value = !showBackground.value
}
</script>

<template>
  <div class="background">
    <div :class="['background__image', { hidden: !showBackground }]"></div>
  </div>



  <h1 class="title">新番列表</h1>

  <div class="animes-container">
    <AnimeCard v-for="anime in animes" :key="anime.name" :anime="anime" :referenceAnime="animes[0]"
      @remove="removeAnime" />
  </div>
</template>


<style>
:root {
  --color-light-green: #2a9d8f;
  --color-dark-green: #264653;
  --color-background: #96a5ac;
  --color-white: #fff;
  --transparency-white: rgba(255, 255, 255, 0.5);
  --shadow-white-transparent: 0 0 0 10px rgba(255, 255, 255, 0.5);
  --font: "Noto Sans SC", sans-serif;
}

html {
  box-sizing: border-box;
  font-size: 16px;
  font-family: var(--font);

}

*,
*:before,
*:after {
  box-sizing: inherit;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--color-background);
}

.background__image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #8EC5FC;
  background-image: linear-gradient(62deg, #8EC5FC 0%, #E0C3FC 50%, #ffffff 100%);
  background-size: cover;
  filter: blur(0.5rem);
  z-index: -1;
}

.hidden {
  display: none;
}

.title {
  text-align: center;
  color: var(--transparency-white);
  font-size: 2rem;
  font-weight: 700;
  margin: 2rem 0;
}

.animes-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.reset-btn {
  display: block;
  width: 13rem;
  height: 2.5rem;
  background-color: var(--color-white);
  margin: 2rem auto;
  border-radius: 20px;
  border: none;
  box-shadow: var(--shadow-white-transparent);
  font-family: var(--font);
  font-size: 1rem;
  color: var(--color-light-green);
  transition: all 0.2s;
  cursor: pointer;
}

.reset-btn:hover {
  background-color: var(--color-dark-green);
  color: var(--color-white);
}

footer {
  text-align: center;
  padding: 1rem 0;
  font-size: 0.8rem;
  color: var(--color-dark-green);
  background-color: var(--transparency-white);
}

footer a {
  color: var(--color-light-green);
}

footer img {
  width: 32px;
  height: 32px;
  margin: 0.5rem 0;
}

@media (min-width: 800px) {
  .title {
    font-size: 3.4rem;
  }
}
</style>