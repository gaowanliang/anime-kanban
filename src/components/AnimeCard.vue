<template>
    <article class="full-anime-data-container" v-if="!showTodayOnly || weekDayIsToday">
        <main class="anime-container">
            <!-- <div class="close-card-btn">
                {{ weekDays[weekDay] }}
            </div> -->
            <h3 class="anime-weekday" :style="{ backgroundColor: tagColors[weekDay] }">
                {{ weekDays[weekDay] }}
            </h3>
            <div class="anime__cover-container" :style="{ backgroundImage: `url(${anime?.image_url ?? ''})` }">
                <div class="anime__cover__title__container">
                    <div class="anime__cover__title">{{ anime?.name ?? '未知' }}</div>
                </div>
            </div>
            <div>
                <h5 class="anime__japanese-title">{{ anime?.japanese_title ?? '未知' }}</h5>
            </div>

            <div class="anime__broadcast-container">
                <h3 class="anime__broadcast__title">放送时间</h3>
                <ul>
                    <li class="anime__broadcast__list__item">
                        <span class="anime__broadcast__list__item__reference">日本</span>
                        <span class="anime__broadcast__list__item__value">{{ anime?.time ?? '待定'
                            }}</span>
                    </li>
                    <li class="anime__broadcast__list__item">
                        <span class="anime__broadcast__list__item__reference">中国大陆</span>
                        <span class="anime__broadcast__list__item__value">{{ anime?.bilibili ?? '暂无' }}</span>
                    </li>
                    <li class="anime__broadcast__list__item">
                        <span class="anime__broadcast__list__item__reference">开播时间</span>
                        <span class="anime__broadcast__list__item__value">{{ formatDate(anime?.bgmlist?.begin) ??
                            anime?.start_date
                            ?? '待定' }}</span>
                    </li>
                </ul>
                <div class="anime__broadcast__platforms">
                    <h4 class="anime__broadcast__platforms__title">放送平台</h4>
                    <div class="anime__broadcast__platforms__list">
                        <span v-for="(platform, index) in getPlatformsLogo(anime?.platforms ?? {})" :key="index"
                            class="anime__broadcast__platform">
                            <h5>{{ index }}</h5>
                            <div class="anime__broadcast__platforms__items">
                                <div v-for="(item, index1) in platform" :key="index1"
                                    class="anime__broadcast__platforms__item">
                                    <a :href="item[0]" target="_blank">
                                        <img :src="item[1]" alt="platform logo" width="40" height="40" />
                                    </a>
                                </div>
                            </div>

                        </span>
                    </div>
                </div>
            </div>

            <div class="anime__details-container">
                <h3 class="anime__details__title">番剧详情</h3>
                <div class="anime__details__type">
                    <span class="anime__details__type__reference">番剧类型</span>
                    <span class="anime__details__type__value">{{ anime?.anime_type ?? '未知' }}</span>
                </div>
                <div class="anime__details__tags">
                    <h4 class="anime__details__tags__title">标签</h4>
                    <div class="anime__details__tags__list">
                        <span v-for="(tag, index) in splitTags(anime?.tags ?? '')" :key="index"
                            class="anime__details__tag" :style="{ backgroundColor: getTagColor(tag) }">
                            {{ tag.trim() }}
                        </span>
                    </div>
                </div>
                <div class="anime__details__staff-cast">
                    <div class="anime__details__staff">
                        <h4 class="anime__details__staff__title">Staff</h4>
                        <pre class="anime__details__staff__content">{{ anime?.staff_cast?.staff ?? '未知' }}</pre>
                    </div>
                    <div class="anime__details__cast">
                        <h4 class="anime__details__cast__title">Cast</h4>
                        <pre class="anime__details__cast__content">{{ anime?.staff_cast?.cast ?? '未知' }}</pre>
                    </div>
                </div>
            </div>
        </main>
    </article>
</template>

<script setup>
import { ref } from 'vue'
import SparkMD5 from 'spark-md5'
import { useRoute } from 'vue-router'

const props = defineProps(['anime'])
const emit = defineEmits(['remove'])

const route = useRoute()
const showTodayOnly = ref(route.query.today === '1')

const weekDay = ref(7)

const tagColors = [
    '#F44336', '#E91E63', '#9C27B0', '#673AB7', '#3F51B5',
    '#2196F3', '#03A9F4', '#00BCD4', '#009688', '#4CAF50',
    '#8BC34A', '#CDDC39', '#FFEB3B', '#FFC107', '#FF9800',
    '#FF5722', '#795548', '#9E9E9E', '#607D8B'
]

const logo = {
    "bilibili": "/src/assets/img/bilibili.svg",
    "iqiyi": "/src/assets/img/iqiyi.svg",
    "iq.com": "/src/assets/img/iqiyi.svg",
    "youku": "/src/assets/img/youku.svg",
    "acg.gamer.com.tw": "/src/assets/img/Bahamut.png",
    "netflix": "/src/assets/img/netflix.svg",
    "viu.com": "/src/assets/img/viu.svg",
    "crunchyroll": "/src/assets/img/crunchyroll.svg",
}
const weekDays = ['周日', '周一', '周二', '周三', '周四', '周五', '周六', '未知']

const splitTags = (tags) => {
    if (typeof tags !== 'string') return []
    return tags.split('/').map(tag => tag.trim()).filter(tag => tag)
}

const getTagColor = (tag) => {
    const hash = SparkMD5.hash(tag)
    const index = parseInt(hash.slice(0, 8), 16) % tagColors.length
    return tagColors[index]
}
// 将2024-10-14T14:00:00.000Z 转换为 2024-10-14 14:00
const formatDate = (date) => {
    if (!date) return null
    return new Date(date).toLocaleString('zh-CN', { hour12: false })
}

// 获取每周几播放
const getWeekDayFromString = (weekDay) => {
    if (!weekDay) return 7

    console.log(weekDay, 1)
    for (let key in weekDays) {
        if (weekDay.includes(weekDays[key])) {
            return key
        }
    }
    return 7
}
// 将2024-10-14T14:00:00.000Z 转换为 周五
const getWeekDayFromDateString = (dateString) => {
    if (!dateString) return 7
    const date = new Date(dateString)
    return date.getDay()

}

const getPlatformsLogo = (platforms) => {
    const platformsLogo = {}
    for (const [key, value] of Object.entries(platforms)) {
        platformsLogo[key] = value.map(item => {
            for (let key in logo) {
                if (item.includes(key)) {
                    return [item, logo[key]]
                }
            }
            return [item, '']
        })
    }
    console.log(platformsLogo)
    return platformsLogo

}

console.log(props.anime)

if (props.anime?.bgmlist?.begin) {
    weekDay.value = getWeekDayFromDateString(props.anime?.bgmlist.begin)
} else {
    weekDay.value = getWeekDayFromString(props.anime?.start_date)
}

const weekDayIsToday = weekDay.value === new Date().getDay()

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
    height: 1.5rem;
    background-color: var(--color-white);
    box-shadow: 0px 2px 5px 1px rgba(0, 0, 0, 0.5);
    border-radius: 25%;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1rem;
    font-weight: 700;
    color: var(--color-light-green);
    padding: 0.2rem;
}

.anime-weekday {
    font-size: 1.5rem;
    font-weight: 700;
    color: white;
    width: 91%;
    text-align: center;
    border-radius: 5rem;
    margin-top: 0.5rem;
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
    height: 4.6rem;
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
}

.anime__japanese-title {
    font-family: "Noto Serif JP", serif;
    font-optical-sizing: auto;
    font-style: normal;
    font-weight: 700;
    background-color: #f5f2f2;
    padding: 0.2rem 0.5rem;
    border-radius: 5px;
    color: #2a9d8f;
    margin: 0.5rem 1rem;
    text-align: center;
}

.anime__broadcast__title,
.anime__details__title {
    height: 3.0rem;
    border-radius: 5px;
    color: var(--color-white);
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: "Ma Shan Zheng", cursive;
    font-size: 1.5rem;
    letter-spacing: 0.5rem;
}

.anime__broadcast__title {
    background-color: #e76f51;
}

.anime__details__title {
    background-color: var(--color-light-green);
    margin-top: 1rem;
}

.anime__broadcast__list__item,
.anime__details__type {
    display: flex;
    justify-content: space-between;
    margin-top: 0.3rem;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    align-items: center;
}

.anime__broadcast__list__item {
    background-color: rgba(231, 111, 81, 0.1);
    padding: 0.5rem;
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

.anime__details__type__value {
    font-weight: 700;
}

.anime__broadcast__list__item__reference,
.anime__broadcast__list__item__value {
    color: #e76f51;
}

.anime__broadcast__list__item__value {
    font-weight: 700;
    width: 60%;
    text-align: right;

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
    justify-self: center;
    text-align: center;
}



.anime__broadcast__platforms__items {
    display: flex;
    flex-direction: row;
}

.anime__broadcast__platforms__item {
    margin: 0.5rem;
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