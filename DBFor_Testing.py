from typing import List, Dict

def make_Testing_Pack() -> List:
    dataPack = []
# -------------------------------------------------------------------
    ch_types = {1: 'Barbera', 6: 'Cortese', 7: 'Grignolino'}
    magCap = 600
    maxFCap = [800, 800, 800]
    minFCap = [100, 100, 100]
    simYears = 2
# -------------------------------------------------------------------
    test = [ch_types, magCap, maxFCap, minFCap, simYears]
    dataPack.append(test)
# -------------------------------------------------------------------
    ch_types = {1: 'BROWAR-AGH', 3: 'Cortese', 4: 'Grignolino', 7:'Dzika-Morena'}
    magCap = 800
    maxFCap = [800, 800, 800, 300, 300]
    minFCap = [100, 100, 100, 100, 100]
    simYears = 3
# -------------------------------------------------------------------
    test = [ch_types, magCap, maxFCap, minFCap, simYears]
    dataPack.append(test)
# -------------------------------------------------------------------
    '''
    ch_types = {2: 'BROWAR-AGH', 5: '1234', 6: '&$@Q%', 8:' '}
    magCap = 1000
    maxFCap = [800, 800, 800, '###', 300, 500, 600, 150]
    minFCap = [100, 100, 100, 100, 100, 100, 100, 100]
    simYears = "X"
# -------------------------------------------------------------------
    test = [ch_types, magCap, maxFCap, minFCap, simYears]
    dataPack.append(test)
    '''
    return dataPack



