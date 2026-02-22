def test_child_windows(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    with page.context.expect_page() as new_window_info:
        page.click("#idnewwindow")

    new_window = new_window_info.value
    new_window.wait_for_load_state()

    print("New Window URL:", new_window.url)

    new_window.close()