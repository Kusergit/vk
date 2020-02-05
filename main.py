from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api



token = 'd304af4c022c230927c900bc85d6169451531d38431af637df0bdd4eb0e54fc7d9ffc7ec909b3323d9d94'
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_user and not event.from_me:
            print('Пришло какое-то сообщение')
            print('Текст сообщения: ' + str(event.text))
            vk_session.method('messages.send', {'user_id' : event.user_id, 'message': 'Я бот помошник python джедаев!', 'random_id':0})
    if event.type == VkEventType.USER_TYPING:
        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Я знаю что ты набираешь текст!))$', 'random_id':0})
