def test_drag_and_drop(page):

    # Open url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # Store draggable
    source = page.locator("#draggable")

    # Stor droppable
    target = page.locator("#droppable")

    # Drag n Drop
    source.drag_to(target)

    # Optional
    page.wait_for_timeout(2000)
