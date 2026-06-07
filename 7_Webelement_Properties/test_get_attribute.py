def test_get_attribute(page):
    # Open website
    page.goto("https://rohit-automation.netlify.app/")

    placeholder = page.get_by_label("Email").get_attribute("placeholder")
    print("Placeholder:", placeholder)

    # Optional wait
    page.wait_for_timeout(2000)
