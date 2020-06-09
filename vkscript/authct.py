import vk_api
import PyQt5
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QMessageBox

someWin = None

def auth(user, somewin):
    someWin = somewin
    vk_session = vk_api.VkApi(
        user[0],
        user[1],
        auth_handler=auth_handler,
        captcha_handler=captcha_hanlder
    )
    try:
        vk_session.auth()
    except vk_api.exceptions.BadPassword:
        QMessageBox.question(someWin, "ошибка","Неправильный логин или пароль",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        return 1
        
    vk = vk_session.get_api()
    return vk

def auth_handler():
    text, ok = QInputDialog.getText(someWin,'Двухфакторная авторизация','Введите код двухфакторной авторизации: ')
    if ok:
        return text, True
    
def captcha_hanlder():
    pass
