def obtener_complemento(base):
    '''

    :param base:
    :return:
    '''
    # retorna caracter
    pass


def generar_cadena_complementaria(adn):
    pass


def calcular_correspondencia(adn1, adn2):
    # retorna num
    pass


def corresponden(adn1, adn2):
    '''
    (str, str) -> bool: valida la correspondencia entre dos cadenas

    >>> corresponden('AGATA', 'TCTAT')
    True

    >>> corresponden('AGATA', 'GACCG')
    False

    :param adn1: primera cadena a comparar
    :param adn2: segunda cadena a comparar
    :return: bool: validacion de la correspondencia
    '''
    if adn2 == generar_cadena_complementaria(adn1):
        return True
    else:
        return False


def es_cadena_valida(adn):
    '''
    (str) -> bool: validar si todos las bases son validas en la cadena

    >>> es_cadena_valida(AGATA)
    True

    >>> es_cadena_valida(AGATS)
    False

    :param adn: str: cadena a validar
    :return: bool: validacion de la cadena
    '''
    if adn == obtener_complemento(base):
        return True
    else:
        return False

def es_base(caracter):
    '''
    (char) -> bool: la funcion es base

    >>> es_base('B')
    False

    >>> es_base('A')
    True

    >>> es_base('AGATA')
    ValueError

    :param caracter: base a validar
    :return: bool: validacion de la base
    '''
    if len(caracter) != 1
        return ValueError(caracter + 'tiene más de un caracter');
    elif caracter in base:
        return True
    else:
        return False

def es_subcadena(adn1, adn2):
    '''
    (str, str) -> bool: Una funcion es subacdena

    >>> es_subcadena('AGA', 'AGATA')
    True

    >>> es_subcadena('AGA', 'GCAC')
    False

    :param adn1: str: primera cadena a comparar
    :param adn2: str: segunda cadena a comparar
    :return: bool: validacion y verificacion si una es una subcdena de la otra
    '''
    if adn1 in adn2:
        return True;
    elif adn2 in adn1:
        return True
    else:
        return False

def reparar_dano(adn, base):
    pass


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

