# empleado.py
from persona import Persona


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self._salario = None
        self._cargo = None
        self._fecha_contratacion = None

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario

    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_fecha_contratacion(self):
        return self._fecha_contratacion

    def set_fecha_contratacion(self, fecha):
        self._fecha_contratacion = fecha
