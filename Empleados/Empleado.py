from Fecha import Fecha

class Empleado:
    #aqui va el codigo
    
    '''-------------------------------------
    # Atributos
    -------------------------------------'''
    
    nombres=''
    apellidos=''
    '''-------------------------------------
    # 1 = Masculino y 2 = Femenino
    -------------------------------------'''
    sexo=0
    salario=0
    
    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    fechaNacimiento = Fecha()
    fechaIngreso = Fecha()
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def CambiarSalario(self, nSalario):
        #aqui va el codigo
        self.salario = nSalario
        return "Su nuevo salario es: " + self.salario
    
    def ConsultarSalario(self):
        # Aqui va el codigo
        return self.salario
    
    def AumentoSalario(self):
        # aqui va el codigo
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return "Su nuevo salario es: " + self.salario
        
    def DuplicarSalario(self):
        # Forma 1
        nuevoSalario = self.salario * 2
        self.salario = nuevoSalario
        
        # # Forma2
        # self.salario *= 2
        
    def CalcularSalarioAnual(self):
        #Forma 1
        salarioAnual=self.salario*12
        return salarioAnual
        #Forma2
        # return self.salario*12
    
    