from flask import Flask, request, json
import weather_module
import vk_api
import vkMethods
import randomCommands

vk = vk_api.VkApi(token="myToken")

app = Flask(__name__)


@app.route('/', methods = ["POST"])
def main():
    data = json.loads(request.data)
    if data["type"] == "confirmation":
        return "97fdacc1"
    elif data["type"] == "message_new":
        object = data["object"]
        id = object["peer_id"]
        body = object["text"]
        body = body.lower()
        from_id = object["from_id"]

        if body == "команды" or body == "что я могу" or body == "возможности":
            commands = ["1. Погода", "2. ЦСКА", "3. Flip/Монетка", "4. Roll/Ролл", "5. Привет", "6. Команды"]
            message_to_send = ""
            for command in commands:
                message_to_send = message_to_send + command + "\n"
            vkMethods.send_message(vk,id, message_to_send)


        if body == "привет" or body == "здарова" or body == "доброе утро":
            names = vk.method("users.get", {"user_ids": from_id })
            for name in names:
                message_to_send = body + ", " + name["first_name"]
            vkMethods.send_message(vk,id, message_to_send)


        if body.lower() == "цска":
            message_to_send = "Сосет"
            vkMethods.send_message(vk,id, message_to_send)

        if body == "погода":
             message_to_send = weather_module.get_weather()
             vkMethods.send_message(vk,id, message_to_send)

        if body == "flip" or body == "монетка":
            message_to_send = randomCommands.flip()
            vkMethods.send_message(vk,id, message_to_send)

        if body == "roll" or body == "ролл":
            message_to_send = randomCommands.roll()
            vkMethods.send_message(vk,id, message_to_send)


    return "ok"