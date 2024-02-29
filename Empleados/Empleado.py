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
    
    def ConsultarDiaCumpleanios(self):
        return self.fechaNacimiento.ConsultarDia()
    
    def CalcularImpuesto(self):
        #Forma 1
        # total = self.CalcularSalarioAnual()
        # total = total * (19.5/100)
        # return total

        #Forma 2
        
        return self.CalcularSalarioAnual()*0.195