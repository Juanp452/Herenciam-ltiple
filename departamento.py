# departamento.py
class Departamento:
    def __init__(self):
        self._nombre_departamento = None
        self._presupuesto = None

    def get_nombre_departamento(self):
        return self._nombre_departamento

    def set_nombre_departamento(self, nombre):
        self._nombre_departamento = nombre

    def get_presupuesto(self):
        return self._presupuesto

    def set_presupuesto(self, presupuesto):
        self._presupuesto = presupuesto

    def asignar_presupuesto(self, monto):
        self.set_presupuesto(monto)
