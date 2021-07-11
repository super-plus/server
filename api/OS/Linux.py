import lsb_release_ex as distrib


def __get_distribution():
    return distrib.get_distro_information()


def get_os_distribution_name():
    return __get_distribution().get('ID')


def get_os_distribution_description():
    return __get_distribution().get('DESCRIPTION')
