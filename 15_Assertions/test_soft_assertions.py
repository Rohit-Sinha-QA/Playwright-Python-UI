# install pip install pytest_check
import pytest_check as check

def test_soft_assertions(page):

    # Open website
    page.goto("https://rohit-automation.netlify.app/")

    # ----- Page Assertions -----
    check.equal(page.url, "https://rohit-automation.netlify.app/")
    check.equal(page.title(), "Login")

    # ----- Heading Assertions -----
    heading = page.locator("h2")
    check.is_true(heading.is_visible())
    check.equal(heading.inner_text(), "Welcome To Automation With Rohit")

    # ----- Radio Button Assertions -----
    employee_radio = page.locator("#employee")
    student_radio = page.locator("#student")

    check.is_true(employee_radio.is_checked())
    check.is_false(student_radio.is_checked())

    # ----- Input Field Assertions -----
    email_input = page.locator("#user")
    password_input = page.locator("#pass")

    check.is_true(email_input.is_visible())
    check.is_true(password_input.is_visible())
    check.equal(
        email_input.get_attribute("placeholder"),
        "✉ Enter your email"
    )

    # ----- Button Assertions -----
    login_button = page.locator(".login-button")

    check.is_true(login_button.is_visible())
    check.is_true(login_button.is_enabled())

    # ----- Link Assertion -----
    forgot_link = page.locator("#forgotPasswordLink")

    check.is_true(forgot_link.is_visible())
    check.equal(
        forgot_link.get_attribute("href"),
        "forgotPassword.html"
    )