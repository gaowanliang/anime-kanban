<template>
    <article class="full-anime-data-container">
        <main class="anime-container">
            <!-- <div class="close-card-btn" @click="$emit('remove', anime.name)">
                <img src="../assets/img/delete.png" alt="Close card icon" width="16" height="16" />
            </div> -->
            <div class="anime__cover-container" :style="{ backgroundImage: `url(${anime.cover_image_url})` }">
                <div class="anime__cover__title__container">
                    <div class="anime__cover__title">{{ anime.name }}</div>
                </div>
            </div>

            <div class="anime__broadcast-container">
                <h3 class="anime__broadcast__title">放送时间</h3>
                <ul>
                    <li class="anime__broadcast__list__item">
                        <span class="anime__broadcast__list__item__reference">日本放送时间</span>
                        <span class="anime__broadcast__list__item__value">{{ anime.time }}</span>
                    </li>
                    <li class="anime__broadcast__list__item">
                        <span class="anime__broadcast__list__item__reference">中国大陆放送时间</span>
                        <span class="anime__broadcast__list__item__value">待定</span>
                    </li>
                    <li class="anime__broadcast__list__item">
                        <span class="anime__broadcast__list__item__reference">开播时间</span>
                        <span class="anime__broadcast__list__item__value">{{ anime.start_date }}</span>
                    </li>
                </ul>
                <div class="anime__broadcast__platforms">
                    <h4 class="anime__broadcast__platforms__title">放送平台</h4>
                    <div class="anime__broadcast__platforms__list">
                        <span v-for="platform in anime.platforms" :key="platform.platform_name"
                            class="anime__broadcast__platform">
                            <a :href="platform.platform_url" target="_blank">{{ platform.platform_name }}</a>
                        </span>
                    </div>
                </div>
            </div>

            <div class="anime__details-container">
                <h3 class="anime__details__title">番剧详情</h3>
                <div class="anime__details__type">
                    <span class="anime__details__type__reference">番剧类型</span>
                    <span class="anime__details__type__value">{{ anime.anime_type }}</span>
                </div>
                <div class="anime__details__tags">
                    <h4 class="anime__details__tags__title">标签</h4>
                    <div class="anime__details__tags__list">
                        <span v-for="(tag, index) in anime.tags.split('/')" :key="index" class="anime__details__tag"
                            :style="{ backgroundColor: getTagColor(index) }">
                            {{ tag.trim() }}
                        </span>
                    </div>
                </div>
                <div class="anime__details__staff-cast">
                    <div class="anime__details__staff">
                        <h4 class="anime__details__staff__title">Staff</h4>
                        <pre class="anime__details__staff__content">{{ anime.staff_cast.staff }}</pre>
                    </div>
                    <div class="anime__details__cast">
                        <h4 class="anime__details__cast__title">Cast</h4>
                        <pre class="anime__details__cast__content">{{ anime.staff_cast.cast }}</pre>
                    </div>
                </div>
            </div>
        </main>
    </article>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps(['anime'])
const emit = defineEmits(['remove'])

const tagColors = [
    '#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5',
    '#2196F3', '#03A9F4', '#00BCD4', '#009688', '#4CAF50',
    '#8BC34A', '#CDDC39', '#FFEB3B', '#FFC107', '#FF9800',
    '#FF5722', '#795548', '#9E9E9E', '#607D8B'
]

const getTagColor = (index) => tagColors[index % tagColors.length]

</script>

<style scoped>
.full-anime-data-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 2rem 2rem;
    animation: fadeIn 1s;
}

.anime-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 22rem;
    background-color: var(--color-white);
    border-radius: 5px;
    box-shadow: 0px 5px 20px 3px rgba(0, 0, 0, 0.3);
    padding-bottom: 1rem;
    position: relative;
}

.close-card-btn {
    position: absolute;
    top: -0.75rem;
    right: -0.75rem;
    width: 1.5rem;
    height: 1.5rem;
    background-color: var(--color-white);
    box-shadow: 0px 2px 5px 1px rgba(0, 0, 0, 0.5);
    border-radius: 50%;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    justify-content: center;
    align-items: center;
}

.close-card-btn:hover {
    transform: scale(1.2);
}

.anime__cover-container {
    width: 20rem;
    height: 24rem;
    border-radius: 5px;
    margin-top: 0.35rem;
    display: flex;
    align-items: flex-end;
    background-size: cover;
}

.anime__cover__title__container {
    width: 100%;
    height: 4rem;
    background-color: rgba(42, 157, 143, 0.7);
    border-radius: 0 0 5px 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.anime__cover__title {
    color: var(--color-white);
    font-weight: 700;
    font-size: 1.5rem;
    margin: 0.5rem;
}

.anime__broadcast-container,
.anime__details-container {
    width: 20rem;
    margin-top: 1rem;
}

.anime__broadcast__title,
.anime__details__title {
    height: 2rem;
    border-radius: 5px;
    color: var(--color-white);
    display: flex;
    justify-content: center;
    align-items: center;
}

.anime__broadcast__title {
    background-color: #e76f51;
}

.anime__details__title {
    background-color: var(--color-light-green);
}

.anime__broadcast__list__item,
.anime__details__type {
    display: flex;
    justify-content: space-between;
    height: 2rem;
    margin-top: 0.3rem;
    border-radius: 5px;
    padding: 0 1rem;
    align-items: center;
}

.anime__broadcast__list__item {
    background-color: rgba(231, 111, 81, 0.1);
}

.anime__details__type {
    background-color: rgba(42, 157, 143, 0.1);
}

.anime__broadcast__list__item__reference,
.anime__broadcast__list__item__value,
.anime__details__type__reference,
.anime__details__type__value {
    font-size: 1rem;
}

.anime__broadcast__list__item__reference,
.anime__broadcast__list__item__value {
    color: #e76f51;
}

.anime__details__type__reference,
.anime__details__type__value {
    color: var(--color-light-green);
}

.anime__broadcast__platforms,
.anime__details__tags,
.anime__details__staff-cast {
    margin-top: 0.5rem;
}

.anime__broadcast__platforms__title,
.anime__details__tags__title,
.anime__details__staff__title,
.anime__details__cast__title {
    font-size: 1rem;
    margin-bottom: 0.3rem;
}

.anime__broadcast__platforms__list,
.anime__details__tags__list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
}

.anime__broadcast__platform {
    background-color: rgba(231, 111, 81, 0.1);
    padding: 0.2rem 0.5rem;
    border-radius: 3px;
}

.anime__broadcast__platform a {
    color: #e76f51;
    text-decoration: none;
}

.anime__details__tag {
    padding: 0.2rem 0.5rem;
    border-radius: 3px;
    color: white;
    font-size: 0.9rem;
}

.anime__details__staff-cast {
    display: flex;
    justify-content: space-between;
}

.anime__details__staff,
.anime__details__cast {
    width: 48%;
}

.anime__details__staff__content,
.anime__details__cast__content {
    background-color: rgba(42, 157, 143, 0.1);
    padding: 0.5rem;
    border-radius: 3px;
    font-size: 0.8rem;
    white-space: pre-wrap;
    word-wrap: break-word;
    color: var(--color-light-green);
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}
</style>