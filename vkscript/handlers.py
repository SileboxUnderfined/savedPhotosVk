def auth_handler():
    key = input("Введите код двухфакторной авторизации: ")
    remember_device = True
    return key, remember_device

def captcha_handler(captcha):
    key = input("Введите код капчи{}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)
