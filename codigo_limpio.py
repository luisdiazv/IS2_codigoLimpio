# Librerias necesarias para el manejo de clases abstractas en Python
from abc import ABC, abstractmethod

#-------------------------------------------------------------------------------
# PRINCIPIO ABIERTO/CERRADO
# Clase abstracta relacionada con los envios desarrollada para que nuevas subclases
# (como nuevos tipos de envio) puedan agregarse sin modificar el codigo
# existente.

from abc import ABC, abstractmethod

class Envio(ABC):
    def __init__(self, distancia, peso):
        self.distancia = distancia
        self.peso = peso

    @abstractmethod
    def calcular_base(self):
        """Metodo abstracto que define
        el calculo el costo base del envio."""
        pass

#-------------------------------------------------------------------------------
# HERENCIA
# Clases hijas de 'Envio' para el calculo de los diferentes metodos de envio.

class EnvioTerrestre(Envio):
    def __init__(self, distancia, peso):
        super().__init__(distancia, peso)

    def calcular_base(self):
        return self.distancia * 0.5 + self.peso * 0.2

class EnvioAereo(Envio):
    def __init__(self, distancia, peso):
        super().__init__(distancia, peso)

    def calcular_base(self):
        return self.distancia * 1.0 + self.peso * 0.5

class EnvioMaritimo(Envio):
    def __init__(self, distancia, peso):
        super().__init__(distancia, peso)

    def calcular_base(self):
        return self.distancia * 0.3 + self.peso * 0.1

#-------------------------------------------------------------------------------
# STRATEGY
# Interface que implementa Strategy para las distintas opciones del servicio.

class ICalculoEnvioStrategy(ABC):
    @abstractmethod
    def calcular_costo(self, envio):
        """Calcula el costo final del envio
            a partir del costo base."""
        pass

class CalculoUrgenteStrategy(ICalculoEnvioStrategy):
    def calcular_costo(self, envio):

        return envio.calcular_base() * 1.5 + 10

class CalculoEstandarStrategy(ICalculoEnvioStrategy):
    def calcular_costo(self, envio):

        return envio.calcular_base()

class CalculoEconomicoStrategy(ICalculoEnvioStrategy):
    def calcular_costo(self, envio):

        return envio.calcular_base() * 0.8

# Clase que implementa ICalculoEnvioStrategy para calcular el envio de forma dinamica.
class CalculadorEnvio:
    def __init__(self, strategy = None):
        self.strategy = strategy

    def setStrategy(self, strategy):
        self.strategy = strategy

    def calcular(self, envio):
        if not self.strategy:
            raise ValueError(
                "No se ha establecido una estrategia de calculo."
            )
        return self.strategy.calcular_costo(envio)


#-------------------------------------------------------------------------------
# main de la modulo de Python
if __name__ == "__main__":
    def solicitar_valor(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor <= 0:
                    raise ValueError
                return valor
            except ValueError:
                print("Entrada invalida. Por favor, ingrese un numero positivo.")

    distancia = solicitar_valor("Ingrese la distancia en km: ")
    peso = solicitar_valor("Ingrese el peso en kg: ")

    metodos_envio = {
        "terrestre": EnvioTerrestre,
        "aereo": EnvioAereo,
        "maritimo": EnvioMaritimo
    }

    calculador = CalculadorEnvio()

    for nombre_metodo, clase_metodo in metodos_envio.items():
        envio = clase_metodo(distancia, peso)
        print(f"\nOpciones para envio {nombre_metodo.capitalize()}:")

        calculador.setStrategy(CalculoUrgenteStrategy())
        costo_urgente = calculador.calcular(envio)
        print(f"  Servicio Urgente: ${costo_urgente:.2f}")

        calculador.setStrategy(CalculoEstandarStrategy())
        costo_estandar = calculador.calcular(envio)
        print(f"  Servicio Estandar: ${costo_estandar:.2f}")

        calculador.setStrategy(CalculoEconomicoStrategy())
        costo_economico = calculador.calcular(envio)
        print(f"  Servicio Economico: ${costo_economico:.2f}")