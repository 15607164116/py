import pytest
from playwright.sync_api import Page, expect


def test_bing_search(page: Page):
    # 1. 访问 Bing 首页
    page.goto("https://cn.bing.com")

    # 2. 定位搜索输入框（Bing 的 input id 是 sb_form_q）
    search_input = page.locator("#sb_form_q")
    search_input.wait_for(state="visible")  # 等待它可见
    search_input.fill("Playwright 自动化测试")

    # 3. 按回车搜索（比找按钮更稳妥）
    search_input.press("Enter")

    # 4. 等待搜索结果加载
    page.wait_for_load_state("networkidle")

    # 5. 验证结果里包含关键字
    expect(page.locator("body")).to_contain_text("Playwright")

    # 6. 截图
    page.screenshot(path="bing_result.png")
    print("\n✅ Bing 搜索自动化测试执行成功！")