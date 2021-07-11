import lsb_release_ex as distrib
import platform
import psutil


def __get_distribution():
    return distrib.get_distro_information()


def get_os_distribution_name():
    return __get_distribution().get('ID')


def get_os_distribution_description():
    return __get_distribution().get('DESCRIPTION')


def get_os_distribution_version():
    return __get_distribution().get('RELEASE')


def get_kernel_version():
    return platform.release()


def get_num_users():
    return len(psutil.users())
