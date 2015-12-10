class TablaLetraDni():

    def __init__(self):
        self.tablaLetraDni = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

    def getPosicionLetra(self, letra):
        posicion = self.tablaLetraDni.index(letra)
        return posicion

    def getLetra(self, posicion):
        return self.tablaLetraDni[posicion]

    def letraPermitida(self, letra):
        return letra in self.tablaLetraDni

    def mostrarTabla(self):##CASO TEST???
        print(self.tablaLetraDni)

#getLetra, letraPermitida (True o False) y getTabla/muestraTabla (print)#

##CASOS TEST##

if __name__ == '__main__':
    
    tablaLetraDni = TablaLetraDni()

#getPosicionLetra(self, letra)

    if tablaLetraDni.getPosicionLetra('A') == 3:
        print('OK')
    else:
        print('FAIL')

#getLetra(self, posicion)

    if tablaLetraDni.getLetra(2) == 'W':
        print('OK')
    else:
        print('FAIL')

#letraPermitida(self, posicion)

    if tablaLetraDni.letraPermitida('A'):
        print('OK')
    else:
        print('FAIL')

# mostrarTabla(self)

