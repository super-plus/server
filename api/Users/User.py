import psutil
from datetime import datetime
import pwd
import grp
import os


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


def get_user_history(user):
    home_dir = "/home/"+str(user) + "/"
    hists = list()
    if os.path.exists(home_dir) and os.path.isdir(home_dir):
        for file in os.listdir(home_dir):
            if file.endswith("sh_history"):
                stat = os.stat(home_dir + file)
                hists.append({
                    "file": file,
                    "st_mtime": stat.st_mtime
                })
        if len(hists) > 0:
            recent = max([hist['st_mtime'] for hist in hists])
            history_file = next(item for item in hists if item["st_mtime"] == recent)["file"]
            get_file = open(home_dir + history_file, "r+")
            return get_file.readlines()
    return False
