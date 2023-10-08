import datetime
from playwright.sync_api import Playwright, sync_playwright
import re

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.locator("body").click()
    page.goto("https://coinmarketcap.com/pl/currencies/kaspa/")
    
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Add a delay (optional) to ensure the page loads completely
    page.wait_for_selector("span.sc-16891c57-0.dxubiK.base-text")
    
    # Find the span element by class name
    span_element_locator = page.locator('span.sc-16891c57-0.dxubiK.base-text')
    if span_element_locator.is_visible():
        # Use textContent() method to get the text content
        span_text = span_element_locator.text_content()
        print(f"Value from span element: {span_text} date: {current_date}")
    else:
        print("Span element not found or not visible.")
    
    filename = f"KASPA_price_{current_date}.txt"
    
    # Write the data to a text file
    with open(filename, mode='w') as file:
        file.write(f"Kaspa- date: {current_date}, price: {span_text}\n")
    
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
