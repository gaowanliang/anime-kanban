import requests
import re
import json

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
        platform_list = []
        for platform in platforms:
            platform_url = platform[0]
            platform_name = platform[1].strip()
            platform_list.append(
                {"platform_name": platform_name, "platform_url": platform_url}
            )

        # Append the extracted data to the anime_list
        anime_list.append(
            {
                "name": name,
                "image_url": image_url,
                "start_date": start_date,
                "time": time,
                "platforms": platform_list,
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


def merge_anime_lists(list1, list2):
    merged_dict = {}

    def normalize_name(name):
        return re.sub(r"\s+", "", name)

    for anime in list1:
        name = normalize_name(anime["name"])
        if name not in merged_dict:
            merged_dict[name] = anime
        else:
            merged_dict[name].update(anime)

    for anime in list2:
        name = normalize_name(anime["name"])
        if name not in merged_dict:
            merged_dict[name] = anime
        else:
            merged_dict[name].update(anime)

    return merged_dict


if __name__ == "__main__":
    # 整合成一个json
    anime_list1 = data1(html_content)
    anime_list2 = data2(html_content)
    merged_anime_list = merge_anime_lists(anime_list1, anime_list2)
    print(merged_anime_list)

    with open("anime_list.json", "w", encoding="utf-8") as f:
        json.dump(merged_anime_list, f, ensure_ascii=False, indent=4)
