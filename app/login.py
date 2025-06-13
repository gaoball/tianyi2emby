from playwright.sync_api import sync_playwright

def tianyi_login(username, password, save_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://cloud.189.cn/")
        page.click("text=登录")
        page.fill("input#username", username)
        page.fill("input#password", password)
        page.click("text=登 录")
        page.wait_for_timeout(5000)
        context.storage_state(path=save_path)
        browser.close()
    return True