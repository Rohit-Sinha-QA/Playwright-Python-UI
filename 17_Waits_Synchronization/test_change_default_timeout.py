def test_dynamic_dropdown(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # All waits now default to 10 seconds
    page.set_default_timeout(10000)  

    page.get_by_placeholder("Type and Select State").click()
    page.get_by_placeholder("Type and Select State").fill("m")
    page.locator("#suggestionsList").get_by_text("Maharashtra").click()

    # Optional
    page.wait_for_timeout(1000)
