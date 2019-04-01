def obtener_complemento(base):
    '''
    (char)->char: complemento de la base ingresada

    >>> obtener_complemento('A')
    T

    >>> obtener_complemento('G')
    C

    >>> obtener_complemento('T')
    A

    >>> obtener_complemento('C')
    G


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
    '''
    (str, str) -> bool: valida la correspondencia entre dos cadenas

    >>> correspondencia('AGATA','TCTAT')
    True

    >>> correspondencia('AGATA','GACCG')
    False


    :param adn1: str: primera cadena a comparar
    :param adn2: str: segunda cadena a comparar
    :return: bool: validacion de la correspondencia
    '''


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
    ValueError

    :param caracter: str: base a validar
    :return: bool: validacion de la base
    '''


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


def reparar_dano(adn, base):
    '''
    (str,char)->str:cadena reparada

    >>> reparar_dano('AGAPA','T')
    AGATA

    :param adn: str: la cadena a reparar
    :param base: char: la base a insertar en la cadena
    :return: str: la cadena reparada
    '''

def obtener_secciones(adn, n):
    '''

    (str, num) -> list of str

    >>>obtener_secciones('agtctatcggatagc', 5)
     ('agt','cta','tcg','gat','agc')

    >>>obtener_secciones('gagatctcagtc', 4)
    ('gag','atc','tca','gtc')

    >>>obtener_secciones('agtgtc', 3)
    ('ag','tg','tc')

    >>>obtener_secciones('gtgtgtcacacataga', 4)
    ('gtgt','gtca','caca','taga')

    :param adn: cadena de adn
    :param n: numero de secciones que desea de la cadena
    :return:cadena de adn en secciones
    '''

def obtener_complementos(lista_adn):
    '''
    (list of str) -> list of str

    >>> obtener_complementos('gtgt','gtca','caca','taga')
    ['caca', 'cagt', 'gtgt', 'atct']

    :param lista_adn: str secciones de una cadena de adn
    :return: secciones complementarias complemetaria de una cadena de adn

    '''


def unir_cadena(lista_adn):
    '''

    (List of str)-> str

    >>>unir_cadena('agta','ttaa','gcta')
    'agtattaagcta'

    >>>unir_cadena('gccc','ttgg','gata')

    'gcccttgggata'


    :param lista_adn: lista de secciones de una cadena de adn
    :return:cadena de adn
    '''

def complementar_cadenas(lista_adn):
    '''

    (list of str) -> str
    >>>complementar_cadenas('agta','ttaa','gcta')
    'tcataattcgat'

    >>>complementar_cadenas('gccc','ttgg','gata')

    'cgggaaccctat'


    :param lista_adn: lista de secciones de una cadena de adn
    :return: cadena complementaria de adn
    '''


