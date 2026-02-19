def test_datepicker(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # fill value directly
    page.locator("#datePicker").fill("2001-01-01")

    # Optional
    page.wait_for_timeout(1000)
