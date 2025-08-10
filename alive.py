import time
from playwright.sync_api import sync_playwright

# Start playwright and launch browser only once
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # headless=False to make it behave like a real user
    
    page1 = browser.new_page()
    # Navigate to the URL
    page1.goto('https://pdtest.streamlit.app/')
    # Stay on the page for 5 seconds
    time.sleep(10)
    # Reload the page
    page1.reload()
    # Stay on the page for another 5 seconds after reload
    time.sleep(5)

    page2 = browser.new_page()
    # Navigate to the URL
    page2.goto('https://tgbotapi.streamlit.app/')
    # Stay on the page for 5 seconds
    time.sleep(10)
    # Reload the page
    page2.reload()
    # Stay on the page for another 5 seconds after reload
    time.sleep(5)

    # (Optional) Wait for 10 minutes before ending the script
    time.sleep(100)  # Uncomment this if you want a forced 10-min delay

    # Close the browser
    browser.close()
