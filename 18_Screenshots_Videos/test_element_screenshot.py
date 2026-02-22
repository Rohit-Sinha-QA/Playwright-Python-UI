def test_element_screenshot(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    page.locator("#resizableBox").screenshot(path="element.png")