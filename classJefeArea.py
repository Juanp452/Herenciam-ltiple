# jefe_area.py
from classArea import Area
from classEmpleado import Empleado


class JefeArea(Area, Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self._especialidad = None
        self._proyectos_finalizados = []
        self._evaluaciones_recientes = None

    def get_especialidad(self):
        return self._especialidad

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

    def get_proyectos_finalizados(self):
        return self._proyectos_finalizados

    def set_proyectos_finalizados(self, proyectos):
        self._proyectos_finalizados = proyectos

    def get_evaluaciones_recientes(self):
        return self._evaluaciones_recientes

    def set_evaluaciones_recientes(self, evaluaciones):
        self._evaluaciones_recientes = evaluaciones

    def mostrar_detalle_jefe_area(self):
        return (f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, "
                f"Salario: {self.get_salario()}, Departamento: {self.get_nombre_departamento()}, "
                f"Responsable: {self.get_responsable()}, Especialidad: {self.get_especialidad()}, "
                f"Proyectos Finalizados: {self.get_proyectos_finalizados()}, Evaluaciones Recientes: {self.get_evaluaciones_recientes()}")
