from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.usuario_input = (AppiumBy.ID, "com.seuapp:id/campo_usuario")
        self.senha_input = (AppiumBy.ID, "com.seuapp:id/campo_senha")
        self.botao_login = (AppiumBy.ID, "com.seuapp:id/botao_login")
        self.mensagem_sucesso = (AppiumBy.ID, "com.seuapp:id/mensagem_boas_vindas")

    def fazer_login(self, usuario, senha):
        self.driver.find_element(*self.usuario_input).send_keys(usuario)
        self.driver.find_element(*self.senha_input).send_keys(senha)
        self.driver.find_element(*self.botao_login).click()

    def verificar_login_sucesso(self):
        return self.driver.find_element(*self.mensagem_sucesso).text
