import vk_api
import time
import random

token = 'c5484a72441332239935574e64a05dde05d9ac201015566fca92cc865291f0280aa446d740fe2fc4fc214'
vk = vk_api.VkApi(token=token)

while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
    if messages['count'] >= 1:
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        if body.lower() == 'привет':
            vk.method('messages.send', {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
        else:
            vk.method('messages.send', {"peer_id": id, "message": 'Я тебя не понял', "random_id": random.randint(1, 2147483647)})
    time.sleep(1)
