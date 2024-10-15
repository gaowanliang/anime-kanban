import requests
import re
import json
import difflib

headers_raw = """User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
TE: trailers"""

headers = {}
for line in headers_raw.split("\n"):
    key, value = line.split(": ", 1)
    headers[key] = value


# 目标网址
url = "https://yuc.wiki/202410/"

# 获取网页内容
response = requests.get(url)
response.encoding = "utf-8"  # 确保编码正确
html_content = response.text


def data1(html_content):
    # Find all the anime blocks
    anime_blocks = re.findall(
        r'<div style="float:left">(.*?)</div></div>', html_content, re.DOTALL
    )

    # Initialize a list to store the extracted data
    anime_list = []

    for block in anime_blocks:
        # Extract Start Date
        start_date_match = re.search(r'<p class="imgtext.*?">(.*?)</p>', block)
        if start_date_match:
            start_date = start_date_match.group(1)
        else:
            start_date = ""

        # Extract Time
        time_match = re.search(r'<p class="imgep.*?">(.*?)</p>', block)
        if time_match:
            time = time_match.group(1)
        else:
            time = ""

        # Extract Cover Image
        image_match = re.search(r'<img width="120px" src="(.*?)"', block)
        if image_match:
            image_url = image_match.group(1)
        else:
            image_url = ""

        # Extract Anime Chinese Name
        name_match = re.search(
            r'<td colspan="3" class=".*?">(.*?)</td>', block, re.DOTALL
        )
        if name_match:
            name = re.sub(r"<br>", " ", name_match.group(1))
            name = re.sub(r"<.*?>", "", name).strip()
        else:
            name = ""

        # Extract Broadcasting platforms
        platforms = re.findall(
            r'<td.*?><a href="(.*?)" target="_blank"><img src=".*?" referrerPolicy="no-referrer"><br><p class=".*?">(.*?)</p></a></td>',
            block,
            re.DOTALL,
        )
        platform_dict = {}
        for platform in platforms:
            platform_url = platform[0]
            platform_name = platform[1].strip()
            # 判断platform_name是否存在于platform_dict中
            if platform_name in platform_dict:
                platform_dict[platform_name].append(platform_url)
            else:
                platform_dict[platform_name] = [platform_url]

        # Append the extracted data to the anime_list
        anime_list.append(
            {
                "name": name,
                "image_url": image_url,
                "start_date": start_date,
                "time": time,
                "platforms": platform_dict,
            }
        )

    return anime_list


def data2(html_content):

    # Find all the anime blocks
    anime_blocks = re.findall(
        r'(<div style="float:left"><img.*?</div>\s*<div><table.*?</table></div>\s*<div style="clear:both"></div>)',
        html_content,
        re.DOTALL,
    )

    anime_list = []

    for block in anime_blocks:
        # Extract cover image URL
        img_match = re.search(
            r'<div style="float:left"><img.*?src="(.*?)".*?></div>', block, re.DOTALL
        )
        if img_match:
            image_url = img_match.group(1)
        else:
            image_url = ""

        # Extract Chinese title
        cn_title_match = re.search(r'<p class="title_cn_.*?">(.*?)</p>', block)
        if cn_title_match:
            cn_title = cn_title_match.group(1).strip()
            cn_title = re.sub(r"<br>", " ", cn_title)
            cn_title = re.sub(r"<.*?>", "", cn_title)
        else:
            cn_title = ""

        # Extract Japanese title
        jp_title_match = re.search(r'<p class="title_jp_.*?">(.*?)</p>', block)
        if jp_title_match:
            jp_title = jp_title_match.group(1).strip()
        else:
            jp_title = ""

        # Extract start date
        start_date_match = re.search(r'<p class="broadcast_r">(.*?)</p>', block)
        if start_date_match:
            start_date = start_date_match.group(1).strip()
        else:
            start_date = ""

        # Extract total episodes
        total_episodes_match = re.search(r'<p class="broadcast_ex_r">(.*?)</p>', block)
        if total_episodes_match:
            total_episodes = total_episodes_match.group(1).strip()
        else:
            total_episodes = ""

        # Extract animation type
        type_match = re.search(r'<td class="type_[a-z]_r">(.*?)</td>', block)
        if type_match:
            anime_type = type_match.group(1).strip()
        else:
            anime_type = ""

        # Extract tags
        tags_match = re.search(r'<td class="type_tag_r.*?">(.*?)</td>', block)
        if tags_match:
            tags = tags_match.group(1).strip()
        else:
            tags = ""

        # Extract staff
        staff_match = re.search(
            r'<td rowspan="2" class="staff_r.*?">(.*?)</td>', block, re.DOTALL
        )
        if staff_match:
            staff = staff_match.group(1).strip()
            # Replace <br> with newline and remove other HTML tags
            staff = re.sub(r"<br>", "\n", staff)
            staff = re.sub(r"<.*?>", "", staff)
            staff = staff.strip()
        else:
            staff = ""

        # Extract cast
        cast_match = re.search(
            r'<td rowspan="2" class="cast_r.*?">(.*?)</td>', block, re.DOTALL
        )
        if cast_match:
            cast = cast_match.group(1).strip()
            # Replace <br> with newline and remove other HTML tags
            cast = re.sub(r"<br>", "\n", cast)
            cast = re.sub(r"<.*?>", "", cast)
            cast = cast.strip()
        else:
            cast = ""

        anime_data = {
            "name": cn_title,
            "japanese_title": jp_title,
            "cover_image_url": image_url,
            "start_date": start_date,
            "total_episodes": total_episodes,
            "anime_type": anime_type,
            "tags": tags,
            "staff_cast": {"staff": staff, "cast": cast},
        }

        anime_list.append(anime_data)

    return anime_list


def extract_anime_info(html_content):
    url = "https://bgm.tv/index/63762"
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    html_content = response.text
    print(html_content)

    # 匹配番剧名和上映情况的正则表达式
    pattern = (
        r'<a href="/subject/\d+" class="l">(.*?)</a>.*?<div class="text">(.*?)</div>'
    )

    # 使用正则表达式查找所有匹配项
    matches = re.findall(pattern, html_content, re.DOTALL)

    # 处理匹配结果
    anime_list = [(title, info.strip()) for title, info in matches]
    anime_dict = {}

    for anime in anime_list:
        title, info = anime
        anime_dict[title] = info

    print(anime_dict)

    return anime_dict


def merge_anime_lists(list1, list2):
    merged_dict = {}

    def normalize_name(name):
        return re.sub(r"\s+", "", name).lower()

    def is_similar(name1, name2, threshold=0.8):
        return (
            difflib.SequenceMatcher(None, name1, name2).ratio() > threshold
            or name1 in name2
            or name2 in name1
        )

    def normalize_url(url):
        return url.strip().lower()

    for anime in list1:
        image_url = normalize_url(anime["image_url"])
        name = anime["name"]
        if image_url not in merged_dict:
            merged_dict[image_url] = anime
        else:
            merged_dict[image_url].update(anime)

    for anime in list2:
        cover_image_url = normalize_url(anime["cover_image_url"])
        name = anime["name"]
        if cover_image_url in merged_dict:
            merged_dict[cover_image_url].update(anime)
        else:
            merged_dict[cover_image_url] = anime

    # Convert merged_dict to use names as keys
    final_dict = {}
    for anime in merged_dict.values():
        name = anime["name"]
        final_dict[name] = anime

    url = "https://bgmlist.com/api/v1/bangumi/onair"
    response = requests.get(url)
    response.encoding = "utf-8"
    html_content_1 = json.loads(response.text)["items"]

    name_to_japanese_title = {}
    for name, anime in final_dict.items():
        if "japanese_title" in anime:
            name_to_japanese_title[normalize_url(anime["japanese_title"])] = name

    unmatched_items = []
    for item in html_content_1:
        title = normalize_url(item["title"])
        matched = False
        for existing_title in name_to_japanese_title:
            if is_similar(title, existing_title):
                name = name_to_japanese_title[existing_title]
                final_dict[name]["bgmlist"] = item
                matched = True
                break
        if not matched:
            unmatched_items.append(item)

    # Match unmatched items using zh-Hans
    for item in unmatched_items:
        for zh_hans in item.get("zh-Hans", []):
            title = normalize_url(zh_hans)
            for existing_title in name_to_japanese_title:
                if is_similar(title, existing_title):
                    name = name_to_japanese_title[existing_title]
                    final_dict[name]["bgmlist"] = item
                    break

    extract_anime_data = extract_anime_info(html_content)
    # Integrate extract_anime_data into final_dict
    for japanese_name, data in extract_anime_data.items():
        normalized_japanese_name = normalize_name(japanese_name)
        for name, anime in final_dict.items():
            if anime.get("japanese_title") and is_similar(
                normalized_japanese_name, normalize_name(anime["japanese_title"])
            ):
                final_dict[name]["bilibili"] = data
                break

    return final_dict


if __name__ == "__main__":
    # 整合成一个json
    anime_list1 = data1(html_content)
    anime_list2 = data2(html_content)
    merged_anime_list = merge_anime_lists(anime_list1, anime_list2)

    with open("src/assets/anime_list.json", "w", encoding="utf-8") as f:
        # 将i0.hdslb.com替换为s2.hdslb.com
        f.write(
            json.dumps(merged_anime_list, ensure_ascii=False, indent=4).replace(
                "i0.hdslb.com", "s2.hdslb.com"
            )
        )
