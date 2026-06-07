from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Microsoft Edge is based on Chromium engine so using p.chromium
    browser = p.chromium.launch(channel="msedge", headless=False)
    page = browser.new_page()

    page.goto("https://rohit-automation.netlify.app/")
    page.wait_for_timeout(3000)

    browser.close()
