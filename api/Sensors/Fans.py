import psutil


def get_num_fans():
    if len(psutil.sensors_fans()) == 0:
        return False
    return len(psutil.sensors_fans())
