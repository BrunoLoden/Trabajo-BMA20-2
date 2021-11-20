class curso:
    nombre = None
    idCurso = None
    listaDepartamento = None
    
    def __init__(self,nomx,idx):
        self.nombre = nomx
        self.idCurso = idx
        #self.listaDepartamento = lx
        
    
class estudiante:
    nombre = None
    idEstudiante = None
    listaCursos = None
    
    def __init__(self,nomx,idx,lx):
        self.nombre = nomx
        self.idEstudiante = idx
        self.listaCursos = lx
        
    
class profesor:
    nombre = None
    listaCursos = None
    
    def __init__(self,nomx,lx):
        self.nombre = nomx
        self.listaCursos = lx
        
       
class departamento:
    
    nombre = None
    listaProfesores = None
    listaCursos = None
    
    def __init__(self,nomx,lx,lc):
        self.nombre = nomx
        self.listaProfesores = lx
        self.listaCursos = lc
      
    def anhadirProfesor(self):
        p1 = profesor("champion",listaCursos[0])
        p2 = profesor("Genaro",listaCursos[1])
        p3 = profesor("Julio",listaCursos[2])
        
        self.listaProfesores.append(p1)
        self.listaProfesores.append(p2)
        self.listaProfesores.append(p3)

    
    def quitarProfesor(self):
        nomx = input("Ingrese el nombre del profesor a quitar: ")
        for i in range(len(self.listaProfesores)):
            if(self.listaProfesores[i].nombre == nomx):
                ix = i
        del self.listaProfesores[ix]
            
    
    def obtenerProfesor(self):
        
        nomx = input("Ingrese el nombre del profesor a obtener: ")
        for i in range(len(self.listaProfesores)):
            if(self.listaProfesores[i].nombre == nomx):
                ix = i
        
        print(self.listaProfesores[ix].nombre)
    
    def obtenerTodosProfesores(self):
        
        #print("======================================================")
        
        for i in range(len(self.listaProfesores)):
            print("======================================================")
            print("Profesor--->",self.listaProfesores[i].nombre)
            print("------------------------------------------------------")
            
            
            for j in range(len(self.listaCursos[i])):
                print(self.listaProfesores[i].listaCursos[j].nombre)
            
    
    
    
    
m1 = curso("Antenas",1)
m2 = curso("Campos",2)
m3 = curso("Telecomunicaciones",3)
m4 = curso("electronicos",4)

b1 = curso("matematicas",1)
b2 = curso("fisica",2)
b3 = curso("programacion",3)
b4 = curso("mate5",4)

e1 = curso("redes",1)
e2 = curso("industrial",2)

listaCursos = list()
listaCursosIngenieria= list()
listaCursosBasicos= list()
listaCursosEspecialidad = list()

listaCursosIngenieria.append(m1)
listaCursosIngenieria.append(m2)
listaCursosIngenieria.append(m3)
listaCursosIngenieria.append(m4)

print(listaCursosIngenieria[0].nombre)

listaCursosBasicos.append(b1)
listaCursosBasicos.append(b2)
listaCursosBasicos.append(b3)
listaCursosBasicos.append(b4)

print(listaCursosBasicos[0].nombre)

listaCursosEspecialidad.append(e1)
listaCursosEspecialidad.append(e2)

print(listaCursosEspecialidad[0].nombre)


listaCursos.append(listaCursosIngenieria)
listaCursos.append(listaCursosBasicos)
listaCursos.append(listaCursosEspecialidad)

#print(listaCursos[0])
#print(listaCursos[1])
#print(listaCursos[2])
        
e1 = estudiante("Oscar",1,listaCursos)
e2 = estudiante("Mateo",2,listaCursos)
e3 = estudiante("July",3,listaCursos)
e4 = estudiante("Hector",4,listaCursos)


print("-------------------------------------------------")

listaProfesores = list()    
elec = departamento("electrica",listaProfesores,listaCursos)
elec.anhadirProfesor()
elec.obtenerTodosProfesores()