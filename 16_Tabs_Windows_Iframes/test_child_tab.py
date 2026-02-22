def test_child_tabs(page):

    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Wait for new tab
    with page.context.expect_page() as new_page_info:
        page.click("#idnewtab")

    new_tab = new_page_info.value
    new_tab.wait_for_load_state()

    print("New Tab Title:", new_tab.title())

    new_tab.close()