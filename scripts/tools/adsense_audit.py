from playwright.sync_api import sync_playwright
import time

def check_adsense():
    print("🚀 Starting AdSense Audit...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Monitor console logs
        page.on("console", lambda msg: print(f"BROWSER CONSOLE: {msg.type}: {msg.text}"))
        
        # 1. Check ads.txt
        print("Checking ads.txt...")
        try:
            resp = page.goto("https://amazingjames.ca/ads.txt", timeout=15000)
            if resp.status == 200:
                print(f"✅ ads.txt Status: 200")
                print(f"Content Preview: {resp.text()[:50]}...")
            else:
                print(f"❌ ads.txt Status: {resp.status}")
        except Exception as e:
            print(f"❌ Failed to reach ads.txt: {e}")

        # 2. Check Homepage Ad Units
        print("\nChecking Homepage Ad Units...")
        try:
            page.goto("https://amazingjames.ca/", wait_until="networkidle", timeout=30000)
            
            # Check for AdSense script
            script_count = page.evaluate("() => document.querySelectorAll('script[src*=\"pagead2\"]').length")
            print(f"AdSense Scripts Found: {script_count}")
            
            # Check for <ins class="adsbygoogle">
            ins_count = page.evaluate("() => document.querySelectorAll('ins.adsbygoogle').length")
            print(f"Ad Units Found: {ins_count}")
            
            # Check if ads are populated (iframe inside <ins>)
            populated = page.evaluate("() => document.querySelectorAll('ins.adsbygoogle iframe').length")
            print(f"Populated Ad Units (iframes): {populated}")
            
            page.screenshot(path="adsense_audit.png")
            print("Audit screenshot saved to adsense_audit.png")
            
        except Exception as e:
            print(f"❌ Failed to audit homepage: {e}")
            
        browser.close()
        print("\n✅ Audit Complete!")

if __name__ == "__main__":
    check_adsense()
