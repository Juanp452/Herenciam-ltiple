# departamento.py
class Departamento:
    def __init__(self):
        self._nombre_departamento = None
        self._presupuesto = None
        self._ubicacion = None
        self._num_empleados = None

    def get_nombre_departamento(self):
        return self._nombre_departamento

    def set_nombre_departamento(self, nombre):
        self._nombre_departamento = nombre

    def get_presupuesto(self):
        return self._presupuesto

    def set_presupuesto(self, presupuesto):
        self._presupuesto = presupuesto

    def get_ubicacion(self):
        return self._ubicacion

    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def get_num_empleados(self):
        return self._num_empleados

    def set_num_empleados(self, num_empleados):
        self._num_empleados = num_empleados
