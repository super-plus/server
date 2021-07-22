import psutil
from api.Utils import BytesUtil


def get_swap_memory():
    swap = psutil.swap_memory()
    return {
        "total": swap.total,
        "used": swap.used,
        "free": swap.free,
        "percent": swap.percent,
        "sin": swap.sin,
        "sout": swap.sout,
        "status": get_swap_memory_status()
    }


def get_swap_memory_status():
    available = BytesUtil.__b_to_mb(psutil.swap_memory().free)
    if available > (available / 10):
        return True
    return False
