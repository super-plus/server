import psutil


def get_hw_temps(fahrenheit=False):
    if len(psutil.sensors_temperatures()) > 0:
        return psutil.sensors_temperatures(fahrenheit=fahrenheit)
    return False
