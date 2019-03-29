def obtener_complemento(base):
    '''
    (char)->char: complemento de la base ingresada

    >>> obtener_complemento('A')
    T

    >>> obtener_complemento('G')
    C

    :param base: char: base para analizar el complemento
    :return: char: complemento de la base ingresada
    '''
    pass

def generar_cadena_complementaria(adn):
    '''
    (str)-> str: cadena complementaria de la cadena ingresada

    >>> generar_cadena_complementaria('AGATA')
    TCTAT

    >>> generar_cadena_complementaria('TATATA')
    ATATAT

    :param adn: str: cadena a analizar
    :return: str: complemento de la cadena ingresada
    '''
    pass


def calcular_correspondencia(adn1, adn2):
    '''
    (str,str)-> num: calcula el porcentaje de correspondencia de 2 cadenas dadas

    >>> calcular_correspondencia('AGATA','TCTAT')
    100

    :param adn1: str: primera cadena a comparar
    :param adn2: str: segunda cadena a comparar
    :return: num: porcentaje de correspondencia de las cadenas dadas
    '''
    pass


def corresponden(adn1, adn2):
    # retorna Bool
    pass


def es_cadena_valida(adn):

    pass


def es_base(caracter):
    '''

    :param caracter:
    :return:
    '''
    pass



def es_subcadena(adn1, adn2):
    pass


def reparar_dano(adn, base):
    '''
    (str,char)->str:cadena reparada

    >>> reparar_dano('AGAPA','T')
    AGATA

    :param adn: str: la cadena a reparar
    :param base: char: la base a insertar en la cadena
    :return: str: la cadena reparada
    '''
    pass


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

