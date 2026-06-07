def test_wait_for_load_state(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # wait for DOM to be ready
    page.wait_for_load_state("domcontentloaded")

    # wait for page to load
    page.wait_for_load_state("load")

    print("DOM fully loaded")