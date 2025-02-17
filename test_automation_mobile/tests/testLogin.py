import time
import pytest
from config.driverSetup import iniciar_driver
from pages.loginPage import LoginPage

@pytest.fixture
def driver():
    driver = iniciar_driver()
    yield driver
    driver.quit()

def test_login_sucesso(driver):
    login_page = LoginPage(driver)
    login_page.fazer_login("usuario_teste", "senha123")

    time.sleep(3) 
    assert "Bem-vindo" in login_page.verificar_login_sucesso(), "Erro no login!"
