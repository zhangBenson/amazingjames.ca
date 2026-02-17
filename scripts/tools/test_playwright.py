from playwright.sync_api import sync_playwright
import time

def run():
    print("🚀 Playwright Starting...")
    with sync_playwright() as p:
        # 启动浏览器 (headless=False 让你可以看到过程)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 1. 打开 Google
        print("Navigate to Google...")
        page.goto("https://www.google.com")
        
        # 2. 输入
        print("Typing query...")
        # 寻找输入框 (Google 的输入框通常是 textarea[name="q"])
        page.fill('textarea[name="q"]', "Capybara")
        
        # 3. 回车
        print("Press Enter...")
        page.press('textarea[name="q"]', "Enter")
        
        # 4. 等待结果
        page.wait_for_load_state("networkidle")
        
        # 5. 截图
        path = "playwright_result.png"
        page.screenshot(path=path)
        print(f"Screenshot saved to {path}")
        
        # 6. 关闭
        browser.close()
        print("✅ Done!")

if __name__ == "__main__":
    run()