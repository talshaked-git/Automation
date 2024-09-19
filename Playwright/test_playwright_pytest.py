from playwright.sync_api import sync_playwright, Page, Playwright
import pytest


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=500,args=["--start-maximized"]) #slow_mo=500 (or more) for debugging purposes. args=["--start-maximized"]

    page = browser.new_page(no_viewport=True) #when using maximized mode, change manually to no_viewport=True

    page = browser.new_page(no_viewport=True)
    page.goto("https://playwright.dev/python/")
    page.get_by_role(role='link', name='docs').click()
    page.screenshot(path='screenshot.png')
    page.wait_for_timeout(3000)

    page.goto("https://playwright.dev/python/")
    page.locator('.navbar__item.navbar__link[href="/python/docs/api/class-playwright"]').click()
    page.screenshot(path='screenshot_API.png')
    page.wait_for_timeout(3000)
