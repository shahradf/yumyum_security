from requests import get
from os import system
from sys import stdout
from time import sleep
from sys import exit
from platform import system as osname
import urllib
import re
from socket import gethostbyname
from subprocess import run
from json import loads

__version__ = '1.0.0'


class Color:
    def black(inp):
        print('\033[30m' + inp)

    def red(inp):
        print('\033[31m' + inp)

    def green(inp):
        print('\033[32m' + inp)

    def yellow(inp):
        print('\033[33m' + inp)

    def blue(inp):
        print('\033[34m' + inp)

    def magenta(inp):
        print('\033[35m' + inp)

    def cyan(inp):
        print('\033[36m' + inp)

    def white(inp):
        print('\033[37m' + inp)

    def rest(inp):
        print('\033[39m' + inp)


class Main:
    @staticmethod
    def clear():
        if osname == 'nt':
            system('cls')
        else:
            system('clear')

    @staticmethod
    def slow_print(vorody):
        for c in vorody + '\n':
            stdout.write(c)
            stdout.flush()
            sleep(10. / 100)

    @staticmethod
    def find_somthing(site, idk):

        try:
            openurl = urllib.request.urlopen(site)
            print('----------------------')
            Color.green(f"{idk} found >>> " + site)
            print("----------------------")
        except:
            print(f"{idk} not found >>> " + site)

    @staticmethod
    def find_cms(site):

        if site[-1] != '/':
            site = site + '/'
        r = get(site)
        source1 = r.text

        if 'wp-content' in source1:
            return ('wordprees')
            check_cms_done = True

        if 'joomla' in source1:
            check_cms_done = True
            return ('joomla')

        if 'Drupal' in source1:
            check_cms_done = True
            return ('Drupal')

        if 'Modx' in source1:
            check_cms_done = True
            return ('Modx')

        if 'Bitrix' in source1:
            check_cms_done = True
            return ('Bitrix')

        if 'Opencart' in source1:
            check_cms_done = True
            return ('Opencart')

        else:
            check_cms_done = False
        if check_cms_done == False:

            try:
                r = get(f'{site}/robot.txt')
                source = r.text

                if 'WordPrees' in source:
                    return ('wordprees')
                    check_cms_done = True

                if 'joomla' in source:
                    check_cms_done = True
                    return ('joomla')

                if 'Drupal' in source:
                    check_cms_done = True
                    return ('Drupal')

                if 'Modx' in source:
                    check_cms_done = True
                    return ('Modx')

                if 'Bitrix' in source:
                    check_cms_done = True
                    return ('Bitrix')

                if 'Opencart' in source:
                    check_cms_done = True
                    return ('Opencart')

                else:
                    check_cms_done = False

                if check_cms_done == False:
                    pass

            except:
                check_cms_done = False
                pass

    @staticmethod
    def find_ttl(site):

        host = gethostbyname(site)

        response_ping = run(['ping', '-c', '1', host], capture_output=True, timeout=2)

        response = re.search(r'ttl=([0-9]+)', str(response_ping)).group(1)

        if int(response) >= 100:

            return 'linux'

        elif int(response) < 100:

            return 'win'

        else:

            pass

    @staticmethod
    def find_subdomain(domain):
        def crt_find():
            request = get("https://crt.sh/?q={}&output=json".format(domain))

            res_json = loads(request.text)

            list_res = []

            for num in range(0, len(res_json)):
                ress = res_json[num]['name_value'].splitlines()

                for num in range(0, len(ress)):
                    if '*' not in ress[num]:
                        list_res.append(ress[num])
                        res = []
                        for i in list_res:
                            if i not in res:
                                res.append(i)
                        response_crt = []
                        for i in res:
                            if not i.startswith("www."):
                                response_crt.append(i)

            return response_crt

        return crt_find()

    @staticmethod
    def auto_update():
        print(__version__)
        system('git pull origin main')

    @staticmethod
    def find_ip_with_sub(site):
        site_lis = Main.find_subdomain(site)
        for i in site_lis:
            sleep(2)
            try:
                print(f'[ {i} ]   --->  [ {gethostbyname(i)} ]')
            except:
                print(f'[ {i} ]   --->  [ Error ! ]')
