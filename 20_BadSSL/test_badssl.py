from playwright.sync_api import sync_playwright

def test_badssl_ignore_ssl(playwright):

    browser = playwright.chromium.launch(headless=False)

    # Ignore SSL errors here
    context = browser.new_context(ignore_https_errors=True)

    page = context.new_page()

    page.goto("https://expired.badssl.com/")

    print("Page Title:", page.title())

    page.wait_for_timeout(3000)

    browser.close()