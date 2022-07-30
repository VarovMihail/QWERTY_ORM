import vk_api
#from main_ORM import gender, city, min_age, max_age
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from config import ACCESS_TOKEN, tok
from vkinder_class import VKinder

keyboard = VkKeyboard(inline=True)
keyboard.add_button('start', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('next', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('like', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('list', color=VkKeyboardColor.SECONDARY)
keyboard.add_button('stop', color=VkKeyboardColor.NEGATIVE)

session_vk = vk_api.VkApi(token=ACCESS_TOKEN)  # Подключаем токен и longpoll

def replay(id, text, attachments):  # Создадим функцию для ответа на сообщения в лс группы
    session_vk.method('messages.send', {'user_id': id,
                                     'message': text,
                                     'random_id': 0,
                                     'attachment': ','.join(attachments),
                                     'keyboard': keyboard.get_keyboard()
                                     })

def replay_without_keyboard(id, text):  # Ответ без клавиатуры
    session_vk.method('messages.send', {'user_id': id,
                                     'message': text,
                                     'random_id': 0})

def next_person(items):  # следующий человек(меняется только после start/next)
    try:
        user_data = next(items)
        first_name, last_name, link = user_data[0].replace('\n', '').split(' ')
        user_name = first_name + ' ' + last_name
    except StopIteration:
        print('КОНЕЦ')
        user1 = VKinder(tok, gender, city, min_age, max_age, 5)
        my_list = user1.search()
        items = iter(my_list)
        user_data = next(items)
        first_name, last_name, link = user_data[0].replace('\n', '').split(' ')
        user_name = first_name + ' ' + last_name
        #return user_data, user_name, link
    return user_data, user_name, link
