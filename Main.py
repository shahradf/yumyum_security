from time import sleep
import mudel as yum


def banner():
    print('''
 __ __  __ __  ___ ___      __ __  __ __  ___ ___       _____   ___    __  __ __  ____   ____  ______  __ __ 
|  |  ||  |  ||   |   |    |  |  ||  |  ||   |   |     / ___/  /  _]  /  ]|  |  ||    \ |    ||      ||  |  |
|  |  ||  |  || _   _ |    |  |  ||  |  || _   _ |    (   \_  /  [_  /  / |  |  ||  D  ) |  | |      ||  |  |
|  ~  ||  |  ||  \_/  |    |  ~  ||  |  ||  \_/  |     \__  ||    _]/  /  |  |  ||    /  |  | |_|  |_||  ~  |
|___, ||  :  ||   |   |    |___, ||  :  ||   |   |     /  \ ||   [_/   \_ |  :  ||    \  |  |   |  |  |___, |
|     ||     ||   |   |    |     ||     ||   |   |     \    ||     \     ||     ||  .  \ |  |   |  |  |     |
|____/  \__,_||___|___|    |____/  \__,_||___|___|      \___||_____|\____| \__,_||__|\_||____|  |__|  |____/ 

''')
    print("""
    }--------------{+} Yum Yum Securty {+}--------------{
    }--------{+}  GitHub.com/............. {+}--------{
    \n""")


sleep_time = 0.1


def main():
    while True:
        print('    [*]  Choose one of the options below  [*]\n')
        sleep(0.3)

        print('    [1]  Admin Page Finder \n')
        sleep(sleep_time)

        print('    [2]  Subdomain Finder \n')
        sleep(sleep_time)

        print('    [3]  location Finder \n')
        sleep(sleep_time)

        print('    [4]  CMS Detection \n')
        sleep(sleep_time)

        print('    [5]  OS Detection  \n')
        sleep(sleep_time)

        print('    [6]  Shell Finder \n')
        sleep(sleep_time)

        print('    [7]  IP Finder \n')
        sleep(0.1)

        print('    [8]  Auto Updater  \n')
        sleep(0.1)

        print('    [0]  Exit ...  \n')

        choose = input('Yum~# ')

        if choose == '1':
            ssite = input('\n    [*]  please enter site example (https://site.com): ')
            if ssite[-1] != '/':
                ssite = ssite + '/'
            with open('admin.txt', 'r') as f:
                line = f.read().splitlines()

            for i in line:
                check_site = ssite + i
                yum.Main.find_somthing(check_site, 'admin')
            x = input('[*]    Back To Menu ? (Y/n) ')
            if x == 'y' or x == '':
                yum.Main.clear()
                banner()
            else:
                exit()

        elif choose == '2':
            ssite = input('\n    [*]  please enter site example (site.com): ')
            list_sub = yum.Main.find_subdomain(ssite)
            print('{*}======================================{*}')
            for i in list_sub:
                print('     [+] ' + i)
            print('{*}======================================{*}\n')
            x = input('[*]    Back To Menu ? (Y/n) ')
            if x == 'y' or x == '':
                yum.Main.clear()
                banner()
            else:
                exit()
        elif choose == '3':
            yum.Main.slowprint('coming soon')
        elif choose == '4':
            ssite = input('\n    [*]  please enter site example (site.com): ')
            res_cms = yum.Main.find_cms(ssite)
            print('\n{*}======================================{*}')
            print('[*]    CMS Detection : {}'.format(res_cms))
            print('{*}======================================{*}\n')
        elif choose == '5':
            ssite = input('\n    [*]  please enter site example (site.com): ')
            res = yum.Main.find_ttl(ssite)
            if res == 'linux':
                print('\n{*}======================================{*}')
                print('[*]    OS Detection : Linux')
                print('{*}======================================{*}\n')
            elif res == 'win':
                print('\n{*}======================================{*}')
                print('[*]    OS Detection : Windows')
                print('{*}======================================{*}\n')
            else:
                print('\n{*}======================================{*}')
                print('[*]    OS Detection : Unknow\n')
                print('{*}======================================{*}\n')
            x = input('[*]    Back To Menu ? (Y/n) ')
            if x == 'y' or x == '':
                yum.Main.clear()
                banner()
            else:
                exit()

        elif choose == '6':
            with open('shell.txt', 'r') as a:
                lines = a.read().splitlines()
            ssite = input('\n    [*]  please enter site example (https://site.com): ')
            if ssite[-1] != '/':
                ssite = ssite + '/'
            for i in lines:
                check_site = ssite + i
                yum.Main.find_somthing(check_site, 'shell')
            x = input('[*]    Back To Menu ? (Y/n) ')
            if x == 'y' or x == '':
                yum.Main.clear()
                banner()
            else:
                exit()
        # elif choose == '7':
        #    slowprint('coming soon')

        elif choose == '7':
            print('eneter nuber one for fiend with subdomain or with api')
            chooseip = int(input('wich one you want ? 1 for sub 2 for api : '))
            if chooseip == 1:
                ssite = input('\n    [*]  please enter site example (site.com): ')
                print('{*}======================================{*}')
                yum.Main.find_ip_with_sub(ssite)
                print('{*}======================================{*}\n')
                x = input('[*]    Back To Menu ? (Y/n) ')
                if x == 'y' or x == '':
                    yum.Main.clear()
                    banner()
                else:
                    exit()
            elif chooseip == 2:
                yum.Main.slowprint('coming soon')
                x = input('[*]    Back To Menu ? (Y/n) ')
                if x == 'y' or x == '':
                    yum.Main.clear()
                    banner()


        elif choose == '8':
            yum.Main.auto_update()
        elif choose == '0':
            exit()
        else:
            pass


banner()
main()
