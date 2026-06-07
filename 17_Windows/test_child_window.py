def test_child_windows(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    with page.context.expect_page() as new_page_info:
        page.click("#idnewwindow")

    new_window = new_page_info.value
    new_window.wait_for_load_state()

    new_window.locator("#user").fill('Admin')
    new_window.wait_for_timeout(1000)

    new_window.close()

    print("Back to main page:", page.title())