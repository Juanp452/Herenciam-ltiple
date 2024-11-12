# director.py
from classArea import Area
from classEmpleado import Empleado


class Director(Area, Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self._proyectos_asignados = []
        self._nivel_influencia = None
        self._reporte_anual = None

    def get_proyectos_asignados(self):
        return self._proyectos_asignados

    def set_proyectos_asignados(self, proyectos):
        self._proyectos_asignados = proyectos

    def get_nivel_influencia(self):
        return self._nivel_influencia

    def set_nivel_influencia(self, nivel):
        self._nivel_influencia = nivel

    def get_reporte_anual(self):
        return self._reporte_anual

    def set_reporte_anual(self, reporte):
        self._reporte_anual = reporte

    def mostrar_detalle_director(self):
        return (f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, "
                f"Salario: {self.get_salario()}, Departamento: {self.get_nombre_departamento()}, "
                f"Responsable: {self.get_responsable()}, Nivel de Influencia: {self.get_nivel_influencia()}, "
                f"Proyectos Asignados: {self.get_proyectos_asignados()}, Reporte Anual: {self.get_reporte_anual()}")
