import re
from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com/v1/"

def test_login_playwright(page: Page):

    page.goto(URL)

    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.get_by_role("button", name="LOGIN").click()

    expect(page).to_have_url("https://www.saucedemo.com/v1/inventory.html")
    expect(page.locator("div.product_label", has_text="Products")).to_be_visible(timeout=7000)
    expect(page.locator(".peek")).to_be_visible(timeout=7000)

def test_add_products_to_the_cart(page: Page):

    page.goto(URL)

    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.get_by_role("button", name="LOGIN").click()

    page.locator("div").filter(has_text=re.compile(r"^\$29\.99ADD TO CART$")).get_by_role("button").click()
    page.locator("div").filter(has_text=re.compile(r"^\$49\.99ADD TO CART$")).get_by_role("button").click()
    page.locator("div").filter(has_text=re.compile(r"^\$7\.99ADD TO CART$")).get_by_role("button").click()

    page.get_by_role("link", name="3").click()
    page.get_by_role("link", name="CHECKOUT").click()

    expect(page).to_have_url("https://www.saucedemo.com/v1/checkout-step-one.html")
    expect(page.locator("div.subheader", has_text="Checkout: Your Information")).to_be_visible(timeout=5000)