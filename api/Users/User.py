import psutil
from datetime import datetime
import pwd
import grp


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


def get_user_procs(username):
    from api.Processes import Process
    return Process.get_processes_by_username(username)


def get_user_groups(user):
    groups = [g.gr_name for g in grp.getgrall() if user in g.gr_mem]
    gid = pwd.getpwnam(user).pw_gid
    groups.append(grp.getgrgid(gid).gr_name)

    return groups
