def test_get_size(page):

    page.goto("https://rohit-automation.netlify.app/")

    # Locate element
    button = page.get_by_role("button", name="Login")

    # Get location
    box = button.bounding_box()

    print("Width:", box["width"])
    print("Height:", box["height"])
