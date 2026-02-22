def test_shadow_dom(page):

    # Open URL
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # using CSS Selector only (#parent child)
    page.locator("#shadow-host input").fill("Hello Rohit")

    # Optional wait
    page.wait_for_timeout(2000)