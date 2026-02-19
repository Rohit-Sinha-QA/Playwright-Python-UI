def test_resizable(page):

    # Open Url
    page.goto("https://rohit-automation.netlify.app/dashboard/dashboard.html")

    # find resizable handle
    resizer = page.locator("div.resizer")

    # move mouse to resizable handle
    resizer.hover()

    # Presses the mouse left button (like clicking and holding).
    page.mouse.down()

    # Moves the mouse to screen coordinates x=600, y=600
    page.mouse.move(600, 600) 

    # Releases the mouse click.
    page.mouse.up()

    # Optional
    page.wait_for_timeout(2000)
