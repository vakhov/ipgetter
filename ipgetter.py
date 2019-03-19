#!/usr/bin/env python3
import socket
import os
from urllib import request


class MyIP(object):
    """
    Получение внешнего ip без использования сторонних библиотек
    ip = MyIP()
    """

    # Набор ссылок на сервисы
    ifconfig_services_urls = {
        'ifconfig.ru': 'http://ifconfig.ru',
        'ifconfig.me': 'http://ifconfig.me/ip',
        'ident.me': 'http://ident.me',
        'ipify.org': 'https://api.ipify.org',
        'icanhazip.com': 'http://icanhazip.com/',
    }

    IP = dict()

    def __init__(self, url=ifconfig_services_urls['ifconfig.ru']):
        if not self.IP:
            self.IP['local'] = socket.gethostbyname(socket.gethostname())  # Локальный IP
            self.IP['external'] = self.get_ip(url)  # Внешний IP

    def __repr__(self):
        return f'Local IP address {self.IP["local"]}, external IP address {self.IP["external"]}'

    def get_ip(self, url=ifconfig_services_urls['ifconfig.ru']):
        """
        Получение внешнего ip через интернет сервисы.
        """
        external_ip = request.urlopen(url).read().decode('utf8').strip()
        return external_ip

    def check_external_ip(self):
        """
        Проверка по разным сервисам того что внешний IP везде одинаков
        :return True если по всем провереным сервисам будет один и тот же ip адрес
        :return False если по всем провереным сервисам будут разные ip адреса
        """
        result = set()
        for url in self.ifconfig_services_urls.values():
            result.add(self.get_ip(url))

        return False if len(result) - 1 else True


def get_ip_from_shell(url='icanhazip.com'):
    """
    Ещё один способ получения ip адреса
    :param url:
    :return:
    """
    return os.system(f'wget -q -O- {url}')


if __name__ == '__main__':
    print(MyIP('http://ident.me'))
