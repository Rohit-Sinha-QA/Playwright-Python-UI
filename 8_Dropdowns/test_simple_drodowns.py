def test_simple_dropdown(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Select by visible text
    page.locator("#state").select_option("Bihar")
    page.wait_for_timeout(1000)

    # Select by value
    page.locator("#state").select_option("AP")
    page.wait_for_timeout(1000)

    # Select by index (index not supported directly, give like index=5)
    page.locator("#state").select_option(index=5)
    page.wait_for_timeout(1000)
