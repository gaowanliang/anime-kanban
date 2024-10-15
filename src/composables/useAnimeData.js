import { ref, computed } from 'vue'

const simulatedData = {
    "鸭乃桥论的禁忌推理第2期": {
        "name": "鸭乃桥论的禁忌推理 第2期",
        "image_url": "http://s2.hdslb.com/bfs/new_dyn/5647287ad67c4a81a19fa6f10a3a3784512995925.jpg",
        "start_date": "10/7周一晚间",
        "time": "21:30~",
        "platforms": [
            {
                "platform_name": "大陆",
                "platform_url": "https://www.bilibili.com/bangumi/media/md22878448"
            },
            {
                "platform_name": "港台",
                "platform_url": "https://acg.gamer.com.tw/acgDetail.php?s=129279"
            }
        ],
        "japanese_title": "鴨乃橋ロンの禁断推理 2nd Season",
        "cover_image_url": "http://s2.hdslb.com/bfs/new_dyn/5647287ad67c4a81a19fa6f10a3a3784512995925.jpg",
        "total_episodes": "<(全13话)",
        "anime_type": "漫画改编动画",
        "tags": "侦探/刑警/悬疑",
        "staff_cast": {
            "staff": "原作：天野明\n\n(少年Jump+/集英社)\n\n　　导演：井畑翔太\n\n　　编剧：渡航\n\n动画人设：石川雅一\n\n　　音乐：辻阳\n\n动画制作：diomedéa",
            "cast": "阿座上洋平　榎木淳弥\n\n　日笠阳子　八代拓\n\n　　福山润　东山奈央\n\n花守由美里　松冈祯丞\n\n　小原好美"
        }
    }, "夏目友人帐第7期": {
        "name": "夏目友人帐 第7期",
        "image_url": "http://s2.hdslb.com/bfs/new_dyn/e33533ed70b54a844d7b6db8b05699b4512995925.jpg",
        "start_date": "10/7周一深夜",
        "time": "23:00~",
        "platforms": [
            {
                "platform_name": "环大陆",
                "platform_url": "https://www.netflix.com/title/81032481"
            }
        ],
        "japanese_title": "夏目友人帳 漆",
        "cover_image_url": "http://s2.hdslb.com/bfs/new_dyn/e33533ed70b54a844d7b6db8b05699b4512995925.jpg",
        "total_episodes": "(全12话)",
        "anime_type": "漫画改编动画",
        "tags": "妖怪/日常/治愈",
        "staff_cast": {
            "staff": "原作：绿川幸\n\n(LaLa/白泉社)\n\n　总导演：大森贵弘\n\n　　导演：伊藤秀树\n\n　　编剧：村井贞之\n\n动画人设：高田晃\n\n　　音乐：吉森信\n\n动画制作：朱夏",
            "cast": "神谷浩史　井上和彦\n\n小林沙苗　石田彰\n\n堀江一真　木村良平\n\n菅沼久义　泽城美雪\n\n佐藤利奈　伊藤美纪\n\n伊藤荣次　诹访部顺一"
        }
    }, "平凡职业造就世界最强第3期": {
        "name": "平凡职业造就世界最强 第3期",
        "image_url": "http://s2.hdslb.com/bfs/new_dyn/6b88ca90ff198cbcba966b13fb8381c0512995925.jpg",
        "start_date": "10/14周一深夜",
        "time": "22:00~",
        "platforms": [
            {
                "platform_name": "港台",
                "platform_url": "https://acg.gamer.com.tw/acgDetail.php?s=127096"
            }
        ],
        "japanese_title": "ありふれた職業で世界最強 3rd season",
        "cover_image_url": "http://s2.hdslb.com/bfs/new_dyn/6b88ca90ff198cbcba966b13fb8381c0512995925.jpg",
        "total_episodes": "(全16话)",
        "anime_type": "小说改编动画",
        "tags": "穿越/冒险/后宫",
        "staff_cast": {
            "staff": "原作：白米良\n\n插画：takayaKi\n\n(Overlap文库/Overlap)\n\n　　导演：岩永彰\n\n　　编剧：佐藤胜一\n\n动画人设：小岛智加\n\n　　音乐：高桥谅\n\n动画制作：asread.",
            "cast": "深町寿成　桑原由气\n\n高桥未奈美　日笠阳子\n\n　大西沙织　花守由美里\n\n　柿原彻也　木岛隆一\n\n　伊藤彩沙　芝崎典子\n\n　　小仓唯　加隈亚衣"
        }
    }, "Re:从零开始的异世界生活第3期": {
        "name": "Re:从零开始的异世界生活 第3期",
        "image_url": "http://s2.hdslb.com/bfs/new_dyn/25db51d0aeb240d2c5e6ff0fc9c24f6a512995925.jpg",
        "start_date": "10/2周三晚间",
        "time": "21:30~",
        "platforms": [
            {
                "platform_name": "港台",
                "platform_url": "https://www.iq.com/album/15uhkad3vv5"
            },
            {
                "platform_name": "港台",
                "platform_url": "https://acg.gamer.com.tw/acgDetail.php?s=131251"
            },
            {
                "platform_name": "香港",
                "platform_url": "https://www.viu.com/ott/hk/zh/vod/2434039/"
            }
        ],
        "japanese_title": "Re:ゼロから始める異世界生活 3rd season",
        "cover_image_url": "http://s2.hdslb.com/bfs/new_dyn/25db51d0aeb240d2c5e6ff0fc9c24f6a512995925.jpg",
        "total_episodes": "(分割/8+8话)",
        "anime_type": "小说改编动画",
        "tags": "穿越/冒险/轮回",
        "staff_cast": {
            "staff": "原作：长月达平\n\n插画：大冢真一郎\n\n(MF文库J/角川)\n\n　　导演：篠原正宽\n\n　　编剧：横谷昌宏\n\n动画人设：佐川遥\n\n　总作监：佐川遥\n\n　　音乐：末广健一郎\n\n动画制作：WHITE FOX",
            "cast": "小林裕介　高桥李依\n\n新井里美　冈本信彦\n\n天崎滉平　赤崎千夏\n\n中村悠一　井口裕香\n\n堀江由衣　堀内贤雄\n\n植田佳奈　江口拓也\n\n　关智一　田村由香里\n\n　山根绮　西山宏太朗\n\n石毛翔弥　津田健次郎\n\n安济知佳　石田彰\n\n河西健吾　悠木碧"
        }
    },
}

export function useAnimeData() {
    const animeList = ref(Object.values(simulatedData))

    const animes = computed(() => animeList.value.map(data => new AnimeCard(data)))

    const resetAnimes = () => {
        animeList.value = Object.values(simulatedData)
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