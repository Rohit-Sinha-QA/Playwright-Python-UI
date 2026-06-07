def test_get_location(page):

    page.goto("https://rohit-automation.netlify.app/")

    textbox = page.get_by_role("textbox", name="Email")

    location = textbox.bounding_box()

    print(location)
