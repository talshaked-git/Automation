from playwright.sync_api import sync_playwright, Page, Playwright
import pytest

@pytest.fixture(scope='function')
def setup(page: Page) -> Page:
    page.goto("https://playwright.dev/python/")

    return page


def test_playwright_python_docs(setup):
    page = setup
    page.get_by_role(role='link', name='docs').click()
    page.wait_for_timeout(3000)
    page.screenshot(path='screenshot.png')

    



def test_playwright_python_api(setup):
    page = setup
    page.locator('.navbar__item.navbar__link[href="/python/docs/api/class-playwright"]').click()
    page.wait_for_timeout(3000)
    page.screenshot(path='screenshot_API.png')
