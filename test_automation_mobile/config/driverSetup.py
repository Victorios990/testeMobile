import os
from appium import webdriver

def iniciar_driver():
    device_name = os.getenv("DEVICE_NAME", "emulator-5554")  # Permite alterar via variável de ambiente
    desired_caps = {
        "platformName": "Android",
        "deviceName": device_name,
        "app": "/caminho/do/seu/app.apk",
        "automationName": "UiAutomator2"
    }
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
