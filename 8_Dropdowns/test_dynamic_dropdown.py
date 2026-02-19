def test_dynamic_dropdown(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Click on dropdown and open options
    page.get_by_placeholder("Type and Select State").click()

    # pass value
    page.get_by_placeholder("Type and Select State").fill("m")

    # click on correct option
    page.locator("#suggestionsList").get_by_text("Maharashtra").click()

    # Optional
    page.wait_for_timeout(1000)
