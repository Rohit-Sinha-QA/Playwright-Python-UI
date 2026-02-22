def test_simple_screenshot(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Simple screenshot (only visible area)
    page.screenshot(path="simple_screenshot.png")

    page.wait_for_timeout(2000)