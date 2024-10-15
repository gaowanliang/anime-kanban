from playwright.sync_api import sync_playwright, expect

url = "http://localhost:5174/"

expect.set_options(timeout=1000000)

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=True)

context = browser.new_context(viewport={"width": 3120, "height": 1080})
page = context.new_page()
page.goto(url)
# 截图
page.screenshot(path="screenshot.jpg", full_page=True)


browser.close()
playwright.stop()
