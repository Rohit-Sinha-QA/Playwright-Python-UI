def test_right_click(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Right click (Context click)
    page.locator("#rightClick").click(button="right")

    # Optional
    page.wait_for_timeout(2000)
