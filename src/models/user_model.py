# src/models/user_model.py

users_db = []
current_id = 1


def get_all_users():
    return users_db


def get_user_by_id(user_id):
    return next((u for u in users_db if u["id"] == user_id), None)


def get_user_by_email(email):
    return next((u for u in users_db if u["email"] == email), None)


def create_user(name, email):
    global current_id
    user = {"id": current_id, "name": name, "email": email}
    users_db.append(user)
    current_id += 1
    return user


def update_user(user_id, name, email):
    user = get_user_by_id(user_id)
    if not user:
        return None
    user["name"] = name
    user["email"] = email
    return user


def delete_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return False
    users_db.remove(user)
    return True

