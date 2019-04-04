def obtener_complemento(base):
    '''
    (char)->char: complemento de la base ingresada

    >>> obtener_complemento('A')
    'T'

    >>> obtener_complemento('G')
    'C'

    >>> obtener_complemento('T')
    'A'

    >>> obtener_complemento('C')
    'G'


    :param base: char: base para analizar el complemento
    :return: char: complemento de la base ingresada
    '''
    if len(base)!= 1 or str != type(base) or not es_base(base) :
        raise TypeError("La base no es valida")

    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'

    return 'G'

def generar_cadena_complementaria(adn):
    '''
    (str)-> str: cadena complementaria de la cadena ingresada

    >>> generar_cadena_complementaria('AGATA')
    'TCTAT'

    >>> generar_cadena_complementaria('TATATA')
    'ATATAT'

    :param adn: str: cadena a analizar
    :return: str: complemento de la cadena ingresada
    '''
    if not es_cadena_valida(adn):
        raise ValueError("La cadena " + str(adn) + " no es valida")
    adncomplemento = ''
    for base in adn:
        adncomplemento+= obtener_complemento(base)

    return adncomplemento


def calcular_correspondencia(adn1, adn2):
    '''
    (str,str)-> num: calcula el porcentaje de correspondencia de 2 cadenas dadas

    >>> calcular_correspondencia('AGATA','TCTAT')
    100

    :param adn1: str: primera cadena a comparar
    :param adn2: str: segunda cadena a comparar
    :return: num: porcentaje de correspondencia de las cadenas dadas
    '''
    if not es_cadena_valida(adn1):
        raise ValueError("La cadena " + str(adn1) + " no es valida")
    if not es_cadena_valida(adn2):
        raise TypeError("La cadena " + str(adn2) + " no es valida" )
    complemento = adn2
    porcentaje = 0
    cont = 0
    longitud = len(complemento)
    for base in adn1:
        if obtener_complemento(base) == complemento[cont]:
            porcentaje += (1/ len(adn1))*100
        cont+=1
        if(cont==longitud):
            break
    return int(porcentaje)


def corresponden(adn1, adn2):
    '''
    (str, str) -> bool: valida la correspondencia entre dos cadenas

    >>> corresponden('AGATA','TCTAT')
    True

    >>> corresponden('AGATA','GACCG')
    False

    :param adn1: str: primera cadena a comparar
    :param adn2: str: segunda cadena a comparar
    :return: bool: validacion de la correspondencia
    '''
    if not es_cadena_valida(adn1) or not es_cadena_valida(adn2):
        raise TypeError("Alguna de las cadenas no es valida")

    if not es_cadena_valida(adn1) or not es_cadena_valida(adn2):
        raise TypeError('Alguna cadena no es valida')

    if adn2 == generar_cadena_complementaria(adn1):
        return True
    else:
        return False


def es_cadena_valida(adn):
    '''
    (str) -> bool: validar si todos las bases son validas en la cadena

    >>> es_cadena_valida('AGATA')
    True

    >>> es_cadena_valida('AGATS')
    False

    :param adn: str: cadena a validar
    :return: bool: validacion de la cadena
    '''
    if str != type(adn):
        raise TypeError("Ingrese una cadena valida")

    for base in adn:
        if not es_base(base):
            return False

    return True


def es_base(caracter):
    '''
    (char) -> bool: la funcion es base

    >>> es_base('B')
    False

    >>> es_base('A')
    True

    >>> es_base('AGATA')
    ValueError('AGATAtiene más de un caracter')

    :param caracter: str: base a validar
    :return: bool: validacion de la base
    '''
    base = 'ACGTacgt'
    if len(caracter) != 1:
        return ValueError(str(caracter) + 'tiene más de un caracter')
    elif caracter in base:
        return True
    else:
        return False


def es_subcadena(adn1, adn2):
    '''
    (str, str) -> bool: Una funcion es subacdena

    >>> es_subcadena('AGATA', 'AGA')
    True

    >>> es_subcadena('AGA', 'GCAC')
    False

    :param adn1: str: primera cadena a comparar
    :param adn2: str: segunda cadena a comparar
    :return: bool: validacion y verificacion si una es una subcdena de la otra
    '''
    if not es_cadena_valida(adn1) or not es_cadena_valida(adn2):
        raise TypeError("Las cadenas no son validas")

    if adn2 in adn1:
        return True;
    else:
        return False


def reparar_dano(adn, base):
    '''
    (str,char)->str:cadena reparada

    >>> reparar_dano('AGAPA','T')
    'AGATA'

    :param adn: str: la cadena a reparar
    :param base: char: la base a insertar en la cadena
    :return: str: la cadena reparada
    '''
    adnToFix = adn
    adnfixed = ''
    for baseinadn in adnToFix:
        if es_base(baseinadn):
            adnfixed += baseinadn
        else:
            adnfixed += base

    return adnfixed

def obtener_secciones(adn, n):
    '''
    (str, num) -> [str]: obtiene lista de secciones segun numero ingresado

    >>> obtener_secciones('agtctatcggatagc', 5)
    ['agt', 'cta', 'tcg', 'gat', 'agc']

    >>> obtener_secciones('gagatctcagtc', 4)
    ['gag', 'atc', 'tca', 'gtc']

    >>> obtener_secciones('agtgtc', 3)
    ['ag', 'tg', 'tc']

    >>> obtener_secciones('gtgtgtcacacataga', 4)
    ['gtgt', 'gtca', 'caca', 'taga']

    :param adn: cadena de adn
    :param n: numero de secciones que desea de la cadena
    :return:cadena de adn en secciones
    '''
    if not es_cadena_valida(adn):
        raise TypeError('la cadena no es valida')
    elif int != type(n):
        raise TypeError(str(n) + 'no es un numero')
    elif n < 0:
        raise TypeError('los numeros negativos no son validos')
    elif n == 0:
        raise ZeroDivisionError('No se puede dividir por 0')
    elif int != type(len(adn)//n):
        raise TypeError('la cadena no se puede dividir en esa cantidad de secciones')

    tamano = len(adn)//n
    cont = 0
    cont2 = 0
    arreglo = ['']*n
    adntoAnalise = str(adn)
    while cont2 < n:
        for base in adntoAnalise:
            arreglo[cont2]+= base
            cont+=1
            if(cont==tamano):
                break
        adntoAnalise =  adntoAnalise.replace(str(arreglo[cont2]), '')
        cont = 0
        cont2 += 1

    return arreglo

def obtener_complementos(lista_adn):
    '''
    (list of str) -> list of str

    >>> obtener_complementos(['gtgt','gtca','caca','taga'])
    ['CACA', 'CAGT', 'GTGT', 'ATCT']

    :param lista_adn: str secciones de una cadena de adn
    :return: secciones complementarias complemetaria de una cadena de adn

    '''

    contf= 0
    lista_complemento= lista_adn

    for cadena in lista_adn:
        if not es_cadena_valida(cadena):
            raise TypeError('la cadena'+ str(cadena) + "no es valida")
        cadenaComplemento = generar_cadena_complementaria(cadena)
        lista_complemento[contf] = cadenaComplemento
        contf+=1

    return lista_complemento


def unir_cadena(lista_adn):
    '''
    (List of str)-> str

    >>> unir_cadena(['agta','ttaa','gcta'])
    'agtattaagcta'

    >>> unir_cadena(['gccc','ttgg','gata'])
    'gcccttgggata'



    :param lista_adn: lista de secciones de una cadena de adn
    :return:cadena de adn
    '''
    k= len(lista_adn)
    cadena_resultante = ''
    contg= 0

    for cadena in lista_adn:
        if not es_cadena_valida(cadena):
            raise TypeError('la cadena'+ str(cadena) + "no es valida")

        cadena_resultante +=cadena
        contg+=1


    return cadena_resultante

def complementar_cadenas(lista_adn):
    '''
    (list of str) -> str:
    >>> complementar_cadenas(['agta','ttaa','gcta'])
    'TCATAATTCGAT'

    >>> complementar_cadenas(['gccc','ttgg','gata'])
    'CGGGAACCCTAT'


    :param lista_adn: lista de secciones de una cadena de adn
    :return: cadena complementaria de adn
    '''

    lista_complementos = obtener_complementos(lista_adn)

    return unir_cadena(lista_complementos)


def validar_complentos_de_archivos():
    '''
    (doc.txt)-> []str

    lee un archivo y verifica la correspondencia de sus cadenas

    :return: str: mensaje con la correspondencia de las cadenas
    '''
    f = open("cadenas.txt", "r")
    cadena = f.readline()
    cadena = cadena.rstrip()
    if (es_cadena_valida(cadena)):
        complemento = generar_cadena_complementaria(cadena)
        cadena2 = f.readline()
        cadena2 = cadena2.rstrip()
        if not es_cadena_valida(cadena2):
            return 'la cadena dos no es valida'
        if (complemento == cadena2):
            return 'Las cadenas son correspondientes al 100%'
        else:
            correspondencia = calcular_correspondencia(cadena, cadena2)
            return 'La corespondencia de las cadenas es del ' + str(correspondencia) + '%'
    else:
        return 'la cadena ' + cadena + ' no es valida'


validar_complentos_de_archivos()