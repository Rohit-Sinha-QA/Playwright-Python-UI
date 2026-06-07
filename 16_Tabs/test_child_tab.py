def test_child_tabs(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Wait for new tab
    with page.context.expect_page() as new_page_info:
        page.click("#idnewtab")

    new_tab = new_page_info.value
    new_tab.wait_for_load_state()

    new_tab.locator("#user").fill('Admin')
    new_tab.wait_for_timeout(1000)

    new_tab.close()

    print("Back to main page:", page.title())