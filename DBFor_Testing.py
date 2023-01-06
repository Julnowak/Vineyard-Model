from typing import List, Dict

def make_Testing_Pack() -> List:
    dataPack = []
    #       SOL_FLAG INFO:
    #   [1] - 0 ograniczeń
    #   [2] - 50% ograniczeń górnych
    #   [3] - jedynie ograniczenia dolne
    #   [4] - skupiony na zapotrzebowanie
# 1------------------------------------------------------------------
    ch_types = {1: 'Barbera', 6: 'Cortese', 7: 'Grignolino'}
    magCap = 600
    maxFCap = [800, 800, 800]
    minFCap = [100, 100, 100]
    simYears = 2
    sol_flag = 1
    store_needs = [150, 150, 150]
# -------------------------------------------------------------------
    test = [ch_types, magCap, maxFCap, minFCap, simYears, store_needs, sol_flag]
    dataPack.append(test)
# 2------------------------------------------------------------------
    ch_types = {2: 'Chardonnay', 3: 'Arneis', 4: 'Erbaluce'}
    magCap = 500
    maxFCap = [800, 800, 800]
    minFCap = [100, 100, 100]
    simYears = 2
    sol_flag = 2
    store_needs = [100, 100, 100]
# -------------------------------------------------------------------
    test = [ch_types, magCap, maxFCap, minFCap, simYears, store_needs, sol_flag]
    dataPack.append(test)
# 3------------------------------------------------------------------
    ch_types = {7: 'Barbera', 8: 'Dolcetto', 6: 'Arneis'}
    magCap = 1000
    maxFCap = [800, 800, 800]
    minFCap = [100, 100, 100]
    simYears = 2
    sol_flag = 4
    store_needs = [200, 200, 200]
# -------------------------------------------------------------------
    test = [ch_types, magCap, maxFCap, minFCap, simYears, store_needs, sol_flag]
    dataPack.append(test)
# -------------------------------------------------------------------
    ch_types = {1: 'BROWAR-AGH', 3: 'Cortese', 4: 'Grignolino', 7:'Dzika-Morena'}
    magCap = 800
    maxFCap = [800, 800, 800, 300, 300]
    minFCap = [100, 100, 100, 100, 100]
    simYears = 3
    sol_flag = 3
    store_needs = [1000, 1000, 1000, 1000, 1000]
# -------------------------------------------------------------------
    test = [ch_types, magCap, maxFCap, minFCap, simYears, store_needs, sol_flag]
    dataPack.append(test)
# -------------------------------------------------------------------
    return dataPack



