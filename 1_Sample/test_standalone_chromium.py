# Import Playwright sync API
from playwright.sync_api import sync_playwright

# Start Playwright engine
with sync_playwright() as p:

    # Launch Chromium browser (chrome-like), headless=False means browser will be visible
    browser = p.chromium.launch(headless=False)
    
    # Create a new browser tab/page
    page = browser.new_page()

    # Open URL
    page.goto("https://rohit-automation.netlify.app/")

    page.wait_for_timeout(3000)  # just to see the page
    browser.close()
