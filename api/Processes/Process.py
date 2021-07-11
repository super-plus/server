import psutil


def get_processes():
    processes = list()
    for proc in psutil.process_iter(['name', 'pid', 'username', 'status']):
        processes.append(proc.info)
    return processes


def get_pids():
    return psutil.pids()


def get_processes_by_username(username):
    processes = list()
    for proc in psutil.process_iter(['name', 'pid', 'username', 'status']):
        if proc.info["username"] == username:
            processes.append(proc.info)
    return processes


def get_processes_by_name(name):
    processes = list()
    for proc in psutil.process_iter(['name', 'pid', 'username', 'status']):
        if proc.info["name"] == name:
            processes.append(proc.info)
    return processes


def get_process_by_pid(pid):
    for proc in psutil.process_iter(['name', 'pid', 'username', 'status']):
        if proc.info["pid"] == pid:
            return proc.info


def get_processes_by_status(status):
    processes = list()
    for proc in psutil.process_iter(['name', 'pid', 'username', 'status']):
        if proc.info["status"] == status:
            processes.append(proc.info)
    return processes

