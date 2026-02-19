def test_maximize(page):

    page.goto("https://rohit-automation.netlify.app/")

    # Need to set custom size
    page.set_viewport_size({"width": 1920, "height": 1080})
