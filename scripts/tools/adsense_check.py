from playwright.sync_api import sync_playwright
import time

def run_diagnostic():
    print("🔍 Starting AdSense Diagnostic for https://amazingjames.ca ...")
    
    with sync_playwright() as p:
        # We use headless=True for background execution in this environment
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1280, 'height': 800},
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # Capture console messages
        console_logs = []
        page.on("console", lambda msg: console_logs.append(f"[{msg.type}] {msg.text}"))
        
        # Capture failed requests
        failed_requests = []
        page.on("requestfailed", lambda request: failed_requests.append(f"{request.method} {request.url} - {request.failure}"))

        try:
            # Navigate to the site
            print("🌐 Navigating to site...")
            page.goto("https://amazingjames.ca", wait_until="networkidle", timeout=60000)
            
            # Wait a bit more for Auto Ads to initialize
            time.sleep(5)
            
            print("\n--- Console Logs ---")
            for log in console_logs:
                print(log)
            
            # Check if AdSense script is present
            script_present = page.evaluate("() => !!document.querySelector('script[src*=\"pagead2\"]')")
            print(f"\n✅ AdSense Script Present: {script_present}")

            # Final screenshot
            page.screenshot(path="adsense_diagnostic.png")
            print("\n📸 Screenshot saved as 'adsense_diagnostic.png'")

        except Exception as e:
            print(f"❌ Error during diagnostic: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    run_diagnostic()
