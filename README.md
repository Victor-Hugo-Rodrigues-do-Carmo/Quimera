---------
DESCRIÇÃO
---------

Quimera - Quebrador de Senha Wi-Fi Multifuncional

Quimera é sua hacking tool em python capaz de quebrar senhas de wi-fi por meio de:

1. Ataque de dicionário.
2. Ataque de força bruta.
3. Ataque híbrido.

Além disso, também oferece algumas opções interessantes, como:

1. Número específico ou progressivo de posições para combinações com repetição.
2. Inserir caracteres no começo ou final de todos os elementos gerados por combinação.

Disponível para Linux e Windows, e com suporte para interface de linha de comando!

-----------
MODO DE USO
-----------

Abra sua interface de linha de comando, e escreva:

<versão_do_python> <caminho_do_quimera.py> <caminho_do_ficheiro> <opção_1> <opção_2>

Ex. EM LINUX: python3 /home/carmo/quimera.py /home/carmo/lista -p 5 -iC Fatec -iF Araraquara

<caminho_do_ficheiro> caminho absoluto do ficheiro que contém a lista (opcional, a depender da localização)

<opção_1> OU n.º específico de posições '-e' OU n.º progressivo de posições '-p'

Ex. 1: se há [a, b] elementos na lista, então -e 2 devolverá [ab, bb, ba, aa]

Ex. 2: se há [a, b] elementos na lista, então -p 2 devolverá [a, b, bb, ba, aa, ab]

<opção_2> inserir no começo '-iC' E/OU inserir no final '-iF'

Ex. 1: se há [a, b] elementos na lista, então -e 2 -iC x -iF y devolverá [xaby, xbby, xbay, xaay]

Ex. 2: se há [a, b] elementos na lista, então -p 2 -iC x -iF y devolverá [xay, xby, xbby, xbay, xaay, xaby]

OBS. 1: se escrever SOMENTE <versão_do_python> <caminho_do_quimera.py> <caminho_do_ficheiro> então o programa executará um ataque de dicionário.

OBS. 2: se a lista contém SOMENTE elementos formados por UM caractere, então o programa executará um ataque de força bruta, senão, executará um 
ataque híbrido.

---------
REQUISITO
---------

módulo pywifi: https://pypi.org/project/pywifi/

----------------------------
SOLUÇÃO DE PROBLEMA EM LINUX
----------------------------

Se: PermissionError: [Errno 13] Permission denied: '/var/run/wpa_supplicant'

Então escreva no seu terminal: sudo chown -R <usuário>:<usuário> /var/run/wpa_supplicant

-------
CRÉDITO
-------

O trecho de código a partir da linha 184 é uma versão modificada do código escrito por Peng Cao: https://medium.com/@caopengau
