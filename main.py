from classDirector import Director
from classGerente import Gerente
from classJefeArea import JefeArea

# main.py

def main():
    # Director
    director = Director()
    director.set_nombre("Ana López")
    director.set_edad(50)
    director.set_salario(6000)
    director.set_nombre_departamento("Tecnología")
    director.set_responsable("Carla Sánchez")
    director.set_proyectos_asignados(["Proyecto A", "Proyecto B"])
    director.set_nivel_influencia("Alto")
    director.set_reporte_anual("Reporte Anual de Tecnología")
    print(director.mostrar_detalle_director())

    # Gerente
    gerente = Gerente()
    gerente.set_nombre("Carlos Mendoza")
    gerente.set_edad(42)
    gerente.set_salario(4000)
    gerente.set_nombre_departamento("Recursos Humanos")
    gerente.set_responsable("Luis García")
    gerente.set_equipo_a_cargo(["Luis", "Marta", "Pedro"])
    gerente.set_estrategia_trimestral("Estrategia de Retención")
    gerente.set_metas_cumplidas("Metas del 2023 cumplidas")
    print(gerente.mostrar_detalle_gerente())

    # Jefe de Área
    jefe_area = JefeArea()
    jefe_area.set_nombre("Elena Ruiz")
    jefe_area.set_edad(35)
    jefe_area.set_salario(3000)
    jefe_area.set_nombre_departamento("Marketing")
    jefe_area.set_responsable("Jorge López")
    jefe_area.set_especialidad("Publicidad Digital")
    jefe_area.set_proyectos_finalizados(["Campaña X", "Campaña Y"])
    jefe_area.set_evaluaciones_recientes("Excelentes")
    print(jefe_area.mostrar_detalle_jefe_area())

if __name__ == "__main__":
    main()
