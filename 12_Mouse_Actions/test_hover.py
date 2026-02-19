def test_hover(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Mouse hover
    page.locator("#hoverBtn").hover()

    # Optional
    page.wait_for_timeout(2000)
