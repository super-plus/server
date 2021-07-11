import psutil
from datetime import datetime


def get_all_users():
    users_list = list()
    users = psutil.users()
    for i in range(len(users)):
        user = users[i]
        users_list.append({
            "name": user.name,
            "terminal": user.terminal,
            "host": user.host,
            "epoch_login": user.started,
            "datetime_login": datetime.fromtimestamp(user.started).strftime('%Y-%m-%d %H:%M:%S'),
            "pid": user.pid,
        })
    return users_list
