import numpy as np

#dane do rozwiązania
numberOfmonths=12
numberOfYears=5
numberOfFields=15
typesOfWine=4
operationMap={0:"nawóź",1:"siejtyp1",2:"siejtyp2",3:"siejtyp3",4:"siejtyp4"}
solution1=np.ndarray(shape=(numberOfmonths*numberOfYears,numberOfFields), dtype=float)
sellingSolution=np.ndarray(shape=(numberOfmonths*numberOfYears,typesOfWine), dtype=float)


#warunki poczatkowe
maksStorage=200
# vineGrowCoeff = np.ndarray(shape=(numberOfmonths*numberOfYears,numberOfFields), dtype=float)
fertilizerCoeff=1.2
vinePrice = np.ndarray(shape=(numberOfmonths*numberOfYears,typesOfWine), dtype=float)

storageCost=np.ndarray(shape=(maksStorage), dtype=float)
wineOnSoilGrow=np.ndarray(shape=(numberOfFields,typesOfWine,2), dtype=float)#2 nawozone neinawozone
gatheringCost=2#per winogrono
transportCost=3#tak samo jak butla liczone
#dojrzewarka ewentualnie

def rozw(rozw: np.ndarray,numberOfYears:int):
    growrate = np.ndarray(shape=(numberOfFields), dtype=float)

    # 0-100 rośnei winogrono
    # ponad to zbiory
    #doimplementować jak wzime sie sieje to umiera
    # do wizualizacji koszty i zyski/miesiac


