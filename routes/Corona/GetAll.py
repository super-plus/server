from flask import Blueprint, jsonify
from api.Users import User
from api.Drives import Partitions
from api.Memory import VirtualMemory, Swap
from api.OS import Linux
from api.Processes import Process
from api.Processors import Processor

all_routes = Blueprint('all', __name__)


@all_routes.route('/')
def get():
    data = {
        "users": User.get_all_users(),
        "drives": Partitions.get_all(),
        "virtual_memory": VirtualMemory.get_virtual_memory(),
        "swap": Swap.get_swap_memory(),
        "os": {
            "distribution": Linux.__get_distribution(),
            "kernel": Linux.get_kernel_version(),
            "hostname": Linux.get_hostname()
        },
        "processes": Process.get_processes(),
        "processor": Processor.get_proc_info()
    }
    return jsonify(data)
