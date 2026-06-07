from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch real chrome browser, headless=False means browser will be visible
    browser = p.chromium.launch(channel="chrome", headless=False)
    page = browser.new_page()

    page.goto("https://rohit-automation.netlify.app/")
    page.wait_for_timeout(3000)

    browser.close()
