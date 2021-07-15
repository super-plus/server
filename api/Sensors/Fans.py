import psutil


def get_fans():
    return psutil.sensors_fans()


def get_num_fans():
    if len(psutil.sensors_fans()) == 0:
        return False
    return len(psutil.sensors_fans())


def get_fan_rpm(fan):
    fans = psutil.sensors_fans()
    return fans[fan][0].current
