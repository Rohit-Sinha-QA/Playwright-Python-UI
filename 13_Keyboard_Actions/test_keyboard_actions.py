def test_keyboard_actions(page):

    # Open URL
    page.goto("https://rohit-automation.netlify.app/")
    page.wait_for_timeout(2000)
    page.locator("#user").click()

    # 1) Type text slowly
    page.keyboard.type("Hello Rohit", delay=150)
    page.wait_for_timeout(1000)

    # 2) Press Enter
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)

    # 3) Select All (CTRL + A)
    page.keyboard.press("Control+A")
    page.wait_for_timeout(1000)

    # 4) Copy (CTRL + C)
    page.keyboard.press("Control+C")
    page.wait_for_timeout(1000)

    # 5) Cut (CTRL + X)
    page.keyboard.press("Control+X")
    page.wait_for_timeout(1000)

    # 6) Paste (CTRL + V)
    page.keyboard.press("Control+V")
    page.wait_for_timeout(1000)

    # 7) Backspace (delete 1 char)
    page.keyboard.press("Backspace")
    page.wait_for_timeout(1000)

    # 8) Delete key
    page.keyboard.press("Delete")
    page.wait_for_timeout(1000)

    # 9) Arrow Keys
    page.keyboard.press("ArrowLeft")
    page.keyboard.press("ArrowRight")
    page.keyboard.press("ArrowUp")
    page.keyboard.press("ArrowDown")
    page.wait_for_timeout(1000)

    # 10) Tab (move to next element)
    page.keyboard.press("Tab")
    page.wait_for_timeout(1000)

    # 11) Shift + Tab (previous element)
    page.keyboard.press("Shift+Tab")
    page.wait_for_timeout(1000)

    # 12) Press and hold keys (like real)
    page.keyboard.down("Shift")
    page.keyboard.type("hello")
    page.keyboard.up("Shift")
    page.wait_for_timeout(1000)

    # 13) Escape
    page.keyboard.press("Escape")
    page.wait_for_timeout(1000)

    # Optional
    page.wait_for_timeout(2000)
