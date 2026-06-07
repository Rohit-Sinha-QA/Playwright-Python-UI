def test_full_page_screenshot(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    page.screenshot(path="fullpage.png", full_page=True)