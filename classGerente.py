# gerente.py
from classArea import Area
from classEmpleado import Empleado


class Gerente(Area, Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self._equipo_a_cargo = []
        self._estrategia_trimestral = None
        self._metas_cumplidas = None

    def get_equipo_a_cargo(self):
        return self._equipo_a_cargo

    def set_equipo_a_cargo(self, equipo):
        self._equipo_a_cargo = equipo

    def get_estrategia_trimestral(self):
        return self._estrategia_trimestral

    def set_estrategia_trimestral(self, estrategia):
        self._estrategia_trimestral = estrategia

    def get_metas_cumplidas(self):
        return self._metas_cumplidas

    def set_metas_cumplidas(self, metas):
        self._metas_cumplidas = metas

    def mostrar_detalle_gerente(self):
        return (f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, "
                f"Salario: {self.get_salario()}, Departamento: {self.get_nombre_departamento()}, "
                f"Responsable: {self.get_responsable()}, Equipo a Cargo: {self.get_equipo_a_cargo()}, "
                f"Estrategia Trimestral: {self.get_estrategia_trimestral()}, Metas Cumplidas: {self.get_metas_cumplidas()}")
