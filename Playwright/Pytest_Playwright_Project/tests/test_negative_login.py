from playwright.sync_api import Page, expect
import pytest




test_data = [
    ('', '', 'Epic sadface: Username is required'),
    ('kajsd', '', 'Epic sadface: Password is required'),
    ('', '1234', 'Epic sadface: Username is required'),
    ('kajsd', '123','Epic sadface: Username and password do not match any user in this service'),
    ('locked_out_user', 'secret_sauce111', 'Epic sadface: Username and password do not match any user in this service'),
    ('locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.'),
]

@pytest.mark.parametrize('username, password, contain_text', test_data)
def test_invalid_logins(page: Page, username: str, password: str, contain_text: str) -> None:
    url = "https://www.saucedemo.com/"
    page.goto(url)

    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text(contain_text)

    expect(page).to_have_url(url)
    # page.wait_for_timeout(2000)
