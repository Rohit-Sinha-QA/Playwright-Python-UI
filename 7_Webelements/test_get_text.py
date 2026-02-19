def test_get_text(page):
    # Open website
    page.goto("https://rohit-automation.netlify.app/")
    email_box = page.get_by_label("Email")
    email_box.fill("admin@example.com")

    # Way 1 get text
    text1 = page.get_by_role("heading", name="Welcome To Automation With Rohit").inner_text()
    print(text1)

    # Way 2 get text
    text2 = page.get_by_role("heading", name="Welcome To Automation With Rohit").first.text_content()
    print(text2)

    # Way 3 get text
    text3 = page.get_by_role("link").all_inner_texts()
    print(text3)

    # Way 4 get text
    email_value = email_box.input_value()
    print("Input Value:", email_value)

    # Optional wait
    page.wait_for_timeout(2000)
