import vk_api, os, json
import handlers
from User import User as usr

def login():
    val = os.path.isfile("settings.json")
    if val == True:
        f = open("settings.json","r")
        userFromJsonDict = json.load(f)
        number = userFromJsonDict["number"]
        password = userFromJsonDict["password"]
        user = usr(number,password)
        return user
    else:
        number = input("Введите номер: ")
        try:
            int(number)
        except ValueError:
            print("Ошибка... Вводите только цифры!")
            return 0
        
        passwrd = input("Введите пароль: ")
        user = usr(number,passwrd)
        userDict = {"number":number,"password":passwrd}
        f = open("settings.json","w")
        json.dump(userDict,f)
        return user

def authication(user):
    vk_session = vk_api.VkApi(
        user.number,
        user.password,
        auth_handler=handlers.auth_handler,
        captcha_handler=handlers.captcha_handler
    )
    vk_session.auth()

    vk = vk_session.get_api()
    return vk

def workWithVk(vk):
    title = "SavedPhotos"
    photos = vk.photos.get(album_id="saved")
    idsOfPhotos = list()
    albums = vk.photos.getAlbums()
    albumsItems = albums['items']
    albumNeeded = ""
    for i in albumsItems:
        if i['title'] == title:
            albumNeeded = i

    if albumNeeded == "":
        vk.photos.createAlbum(title=title)
        workWithVk(vk)

    for i in photos['items']:
        idsOfPhotos.append(i['id'])
    
    print(idsOfPhotos)
    idOfAlbum = albumNeeded['id']
    for i in idsOfPhotos:
        print(vk.photos.move(photo_id=i,target_album_id=idOfAlbum))

if __name__ == "__main__":
    user = login()
    if user == 0:
        user = login()

    vk = authication(user)
    workWithVk(vk)
    input()