from utils.driver_factory import create_driver
from pages.login_page import LoginPage
import pytest

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_login_valid(driver):
    login = LoginPage(driver)
    login.open()
    login.login("admin", "Admin123")
    assert "Home" in driver.title or "OpenMRS" in driver.title

def test_login_invalid_password(driver):
    login = LoginPage(driver)
    login.open()
    login.login("admin", "wrongPass")
    assert "Invalid username/password" in driver.page_source
