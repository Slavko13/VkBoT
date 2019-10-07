import random
def send_message(vk,id, message_to_send):
    vk.method("messages.send", {"peer_id": id, "message": message_to_send, "random_id": random.randint(1, 187264123)})