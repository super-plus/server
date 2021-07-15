import psutil


def get_all():
    drives = psutil.disk_partitions()
    parsed = list()
    for i in range(len(drives)):
        drive = get_drive(drives[i].device)
        if drive is not None:
            parsed.append(drive)
    return parsed


def get_drive(drive):
    drives = psutil.disk_partitions()
    for i in range(len(drives)):
        if drive in drives[i].device and "snap" not in drives[i].mountpoint:
            return {
                "device": drives[i].device,
                "mount": drives[i].mountpoint,
                "type": drives[i].fstype,
                "opts": drives[i].opts,
                "total": psutil.disk_usage(drives[i].mountpoint).total,
                "used": psutil.disk_usage(drives[i].mountpoint).used,
                "free": psutil.disk_usage(drives[i].mountpoint).free,
                "percentage": psutil.disk_usage(drives[i].mountpoint).percent,
            }
