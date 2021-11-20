#%%
class persona:
    nombre = None
    dni = None
    
    def __init__(self,nomx,dnix):
        
        self.nombre = nomx
        self.dni    = dnix
        
    def caminar(self):
        print("caminando ando")
        

class estudiante(persona):
    nota = None
    codigo = None 
    
    def __init__(self,nomx,dnix,notx,codx):
        super().__init__(nomx,dnix)
        self.nota = notx
        self.codigo = codx
        
        
class alumnoFiee(estudiante):
    
    centroC = None
    especialidad = None
    
    def __init__(self,nomx,dnix,notx,codx,cx,ex):
        super().__init__(nomx,dnix,notx,codx)
        self.centroC = cx
        self.especialidad = ex
        
    
    
e1 = estudiante("Julio",38938,15,"0003")
print(e1.nombre)

e1.caminar()


aFiee = alumnoFiee("Orlando",72727,17,"0001","Pedro Paulet","electrica")
print(aFiee.nombre)

# %%
from abc import abstractmethod, ABCMeta

class vehiculo(metaclass=ABCMeta):
    
    @abstractmethod
    def quien_eres(self):
        print("soy una clase ")

#v1 = vehiculo()
#v1.quien_eres()

class auto(vehiculo):
    
    placa = None
    modelo = None
    
    def __init__(self,plax,modx):
        super().__init__()
        self.placa = plax
        self.modelo = modx
        
    def quien_eres(self):
        print("Ahora soy clase hija")
        
        
a1 = auto("rzr","vw")
print(a1.placa)
a1.quien_eres()

#%%
from abc import abstractmethod , ABCMeta

class figuraGeometrica(metaclass = ABCMeta):
    
    @abstractmethod
    def calcularArea(self):
        pass
    
    @abstractmethod
    def calcularPerimetro(self):
        pass
    
    
class cuadrado(figuraGeometrica):
    
    def __init__(self,lx):
        super().__init__()
        self.lado = lx
        
    def mostrandoArea(self):
        pass
    
    def calcularArea(self):
        a = self.lado*self.lado
        return a
    
    def calcularPerimetro(self):
        p = 4*self.lado
        return p
    
    
class triangulo(figuraGeometrica):
    
    def __init__(self,ld):
        super().__init__()
        self.lado = ld
        
    def cualquierMetodo(self):
        pass
    
    
    def calcularArea(self):
        a = self.lado*self.lado*self.lado/3
        return a
    
    def calcularPerimetro(self):
        p = 3*self.lado
        return p
    
c1 = cuadrado(5)
print(c1.lado)
t1 = triangulo(4)
print(t1.lado)
# %%
