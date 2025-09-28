class Registros:
    def __init__(self):
        self.paciente= []
        self.especialidad= []
        self.horario= []
        self.Turnos= []
        
    def registrar_turno(self,paciente,especialidad,horario):
        self.paciente.append(paciente)
        self.especialidad.append(especialidad)
        self.horario.append(horario)
        turno= [paciente,especialidad,horario]
        self.Turnos.append(turno)
        
    def validacion(self,horario):
        horario= int(horario)
        if 8 <= horario <= 18:
            return True
        else:
            return False
        
    def mostrar_turnos(self):
        print("Turnos Pendientes:")
        print(f"Pacientes: {self.paciente}")
        print(f"Especialidades: {self.especialidad}")
        print(f"Horario: {self.horario}")
        num= 0
        for i in self.Turnos:
            num += 1
            print(f"Registro de cada paciente: Paciente {num} - {i}")
         
    
    def vacia(self):
        if len(self.Turnos) == 0:
            return True
        else:
            return False
        
    def cancel_turno(self):
        if self.vacia():
            print("No hay turnos registrados!!")
        else:
            print(f"Ultimo turno eliminado!",self.Turnos.pop())

    

        
    def menu(self):
        while True:
            print("______MENU_____")
            print("Que desea hacer?")
            print("1-Registrar Turno")
            print("2-Mostrar turnos pendientes")
            print("3-Cancelar el ultimo turno")
            print("4-Salir")
            opcion= input("Ingrese la opcion deseadad: ")
            if opcion == "1":
                paciente= input("Ingrese el nombre del Paciente: ").capitalize()
                especialidad= input("Ingrese la especialidad que necesita: ").capitalize()
                try:
                    horario= int(input("Ingrese el horario: "))
                    if self.validacion(horario):
                        self.registrar_turno(paciente,especialidad,horario)
                        print("Turno guardado con exito!")
                    
                    else:
                        print("Ingrese un horario entre las 8:00 am y 18:00 pm.")
                        continue
                except UnboundLocalError:
                    print("Ingrese un horario valido en formato numerico.")
                except ValueError:
                    print("Ingrese un horario valido en formato numerico.")
            elif opcion == "2":
                if self.vacia():
                    print("No hay turnos registrados!")
                else:
                    self.mostrar_turnos()
            elif opcion == "3":
                self.cancel_turno()
            elif opcion == "4":
                print("Dia finalizado!")
                print("Turnos del dia:")
                print(self.Turnos)
                break
            else:
                print("Ingrese una opcion valida!")

                

Medicina= Registros()
Medicina.menu()