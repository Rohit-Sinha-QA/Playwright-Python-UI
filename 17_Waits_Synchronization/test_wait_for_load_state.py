def test_wait_for_load_state(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    page.wait_for_load_state("domcontentloaded")

    print("DOM fully loaded")