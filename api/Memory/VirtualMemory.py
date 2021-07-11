import psutil
from api.Utils import BytesUtil


def get_virtual_memory():
    return psutil.virtual_memory()


def get_virtual_memory_status():
    if BytesUtil.__b_to_mb(get_virtual_memory().available) <= 100:
        return False
    return True

