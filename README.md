# Anime Kanban

Anime Kanban 是一个用于展示新番动画信息的看板应用。

## 安装与运行

1. 克隆仓库：

   ```sh
   git clone https://github.com/gaowanliang/anime-kanban.git
   cd anime-kanban
   ```

2. 安装依赖：

   ```sh
   npm install
   ```

3. 运行开发服务器：

   ```sh
   npm run dev
   ```

4. 构建项目：
   ```sh
   npm run build
   ```

## 主要文件与目录

- `src/App.vue`：主应用组件。
- `src/components/AnimeCard.vue`：用于展示单个动画信息的组件。
- `src/components/BackgroundSwitch.vue`：用于切换背景的组件。
- `src/composables/useAnimeData.js`：包含动画数据的组合式函数。
- `anime_list.json`：包含动画信息的 JSON 文件。

## 使用的技术栈

- Vue 3
- Vite
- JavaScript
- HTML
- CSS

## 贡献

欢迎贡献！请 fork 此仓库并提交 PR。

## 许可证

此项目使用 MIT 许可证。

## 联系

### 设计

原始设计、HTML、CSS 和 JavaScript 代码由 [Damian Demasi](mailto:damian.demasi.1@gmail.com) 编写。

GitHub 链接：[GitHub](https://github.com/Colo-Codes/mini-projects/tree/main/covid-19-dashboard-app)

图标由 [Freepik](https://www.freepik.com) 制作，来自 [Flaticon](https://www.flaticon.com)。

加载动画代码由 [Dmitry Rybalko](https://codepen.io/Testosterone/pen/ZEKEWEr) 编写。

### 数据来源

动画数据来源于以下平台：

- [YuC's AnimeList](https://yuc.wiki/)
- [bgmlist](https://bgmlist.com/)
- [bangumi](https://bgm.tv/)
