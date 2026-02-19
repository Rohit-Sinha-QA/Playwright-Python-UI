def test_clear_text_multiple_ways(page):

    # Open website
    page.goto("https://rohit-automation.netlify.app/")

    # Locate textbox
    email_box = page.get_by_role("textbox", name="Email")

    # First enter some text
    email_box.fill("admin@example.com")

    # Optional wait for demo
    page.wait_for_timeout(2000)

    # Way 1 to clear
    email_box.fill("")

    # Optional wait for demo
    page.wait_for_timeout(2000)

    # Enter again
    email_box.fill("test1@example.com")

    # Optional wait for demo
    page.wait_for_timeout(2000)

    # Way 2 to clear
    email_box.clear()    # Clears text

    # Optional wait for demo
    page.wait_for_timeout(2000)
