import psutil
from cpuinfo import get_cpu_info


def get_num_proc(logical=True):
    return psutil.cpu_count(logical=logical)


def get_proc_name():
    return get_cpu_info()["brand_raw"]


def get_proc_info():
    return get_cpu_info()