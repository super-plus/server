import psutil
from api.Utils import BytesUtil


def get_virtual_memory():
    mem = psutil.virtual_memory()
    return {
        "total": mem.total,
        "available": mem.available,
        "percent": mem.percent,
        "used": mem.used,
        "free": mem.free,
        "active": mem.active,
        "inactive": mem.inactive,
        "buffers": mem.buffers,
        "cached": mem.cached,
        "shared": mem.shared,
        "slab": mem.slab,
        "status": get_virtual_memory_status()
    }


def get_virtual_memory_status():
    available = BytesUtil.__b_to_mb(psutil.virtual_memory().available)
    if available > (available / 10):
        return True
    return False
