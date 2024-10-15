import { ref, computed } from 'vue'
// 读取同文件夹下的anime_list.json文件
import data from '../assets/anime_list.json'


export function useAnimeData() {
    const animeList = ref(Object.values(data))

    const animes = computed(() => animeList.value.map(data => new AnimeCard(data)))

    const resetAnimes = () => {
        animeList.value = Object.values(data)
    }

    const removeAnime = (animeName) => {
        const index = animeList.value.findIndex(a => a.name === animeName)
        if (index !== -1) {
            animeList.value.splice(index, 1)
        }
    }

    return {
        animes,
        resetAnimes,
        removeAnime
    }
}

class AnimeCard {
    constructor(data) {
        Object.assign(this, data)
    }

    getComparison(field, referenceAnime) {
        // 这里保留比较方法，但暂时不实现具体逻辑
        // 可以在以后根据需要添加具体的比较逻辑
        return 0
    }
}