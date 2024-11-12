# area.py
from classDepartamento import Departamento


class Area(Departamento):
    def __init__(self):
        super().__init__()
        self._responsable = None
        self._objetivo_anual = None
        self._proyectos_en_curso = []

    def get_responsable(self):
        return self._responsable

    def set_responsable(self, responsable):
        self._responsable = responsable

    def get_objetivo_anual(self):
        return self._objetivo_anual

    def set_objetivo_anual(self, objetivo):
        self._objetivo_anual = objetivo

    def get_proyectos_en_curso(self):
        return self._proyectos_en_curso

    def set_proyectos_en_curso(self, proyectos):
        self._proyectos_en_curso = proyectos
