import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# лист с id пользователей, которым будет отправляться сообщение
user_list = ['user1_id', 'user2_id', 'user3_id']

def main():
    # Авторизация
    vk_session = vk_api.VkApi(token='EPseGHKHvKykCQUEJesK')

    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    # Основной цикл
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            # Если написали нам, то отправим сообщение всем пользователям из списка.
            for user in user_list:
                vk.messages.send(
                    user_id=user,
                    message='Получено новое сообщение:' + event.text,
                    random_id=0
                )

if __name__ == '__main__':
    main()