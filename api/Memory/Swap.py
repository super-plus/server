import psutil
from api.Utils import BytesUtil


def get_swap_memory():
    return psutil.swap_memory()


def get_swap_memory_status():
    available = BytesUtil.__b_to_mb(get_swap_memory().available)
    if available > (available / 10):
        return True
    return False
