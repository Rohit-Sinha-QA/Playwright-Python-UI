def test_double_click(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Double click
    page.locator("#dblClick").dblclick()

    # Optional
    page.wait_for_timeout(2000)
