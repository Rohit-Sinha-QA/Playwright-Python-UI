def test_slider(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Move slider (set value)
    page.locator("#slider").fill("80")

    # Optional
    page.wait_for_timeout(2000)
