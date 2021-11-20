class Distribuidora:
    Nom = None
    PotT= None
    AreaOp=None
    def __init__(self, Nom_x,AreaOp_x):
        self.Nom = Nom_x
        self.Area = AreaOp_x



class Departamento:
    Nom_Dep = None
    N_Personal = None
    def __init__(self, Nom_Dep_x,N_Personal_x):
        self.Nom_Dep  = Nom_Dep_x
        self.N_Personal = N_Personal_x


class Personal:
    Nom_per = None
    Id_per = None
    Cargo = None
    def __init__(self, Nom_per_x,Id_per_x,car_x):
        self.Nom_per = Nom_per_x
        self.Id_per = Id_per_x
        self.Cargo = car_x

class Barra:
    Nom_bar = None
    Volt = None #[KV]
    def __init__(self,Nom_bar_x,Volt_x):
        self.Nom_bar = Nom_bar_x
        self.Volt = Volt_x
    

class Cliente:
    Nom_Cli = None
    def __init__(self,Nom_cli_x):
        self.Nom_Cli = Nom_cli_x

class C_libre:
    Nom_prop = None
    Mes = None
    Energia = None
    def __init__ (self, Nom_prop_x,Mes_x,Energia_x):
        self.Nom_prop = Nom_prop_x
        self.Mes = Mes_x
        self.Energia = Energia_x


class C_regulados:
    Nom_prop = None
    Mes = None
    Potencia = None
    #Suministrado = None
    def __init__ (self, Nom_prop_x,Mes_x,Potencia_x):
        self.Nom_prop = Nom_prop_x
        self.Mes = Mes_x
        self.Energia = Potencia_x    

class Ubicacion:
    Provincia = None
    Distrito = None
    Agrupacion = None
    Mz = None
    Lt = None

class N_sumistro:
    N_sum = None
    Costo = None
    Impuesto = None

    def __init__ (self, N_sum_x,Costo_x,Imp_x):
        self.N_sum = N_sum_x
        self.Costo  = Costo_x
        self.Impuesto = Imp_x