def test_span_dropdown(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # click on dropdown and open options
    page.locator("//span[text()='Select State']").click()

    # Optional
    page.locator("li[data-value='Br']").wait_for(state="visible")

    # Click on option
    page.locator("li[data-value='Br']").click()

    # Optional
    page.wait_for_timeout(1000)