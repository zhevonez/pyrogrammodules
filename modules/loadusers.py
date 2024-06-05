# for default bots

def load_users():
    try:
        with open("users.txt", "r", encoding="utf-8") as file: 
            users_data = file.readlines()
            users = {}
            for user_data in users_data:
                user_info = user_data.strip().split(";")
                chat_id = int(user_info[0])
                user = {
                    "name": user_info[1], # any data 
                    "tag": user_info[2],
                }
                users[chat_id] = user
            return users
    except FileNotFoundError:
        return {}
