from playwright.sync_api import expect

def test_wait_clickable_manual(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    page.click("#enableRadioBtn")

    # Increase timeout to 10 seconds
    expect(page.locator("#delayedRadio")).to_be_enabled(timeout=10000)

    page.locator("#delayedRadio").click()