def test_wait_for_selector(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    page.click("#WaitVisible")

    # Wait until delayed text appears
    page.wait_for_selector("#delayText")

    print("Text appeared!")
    