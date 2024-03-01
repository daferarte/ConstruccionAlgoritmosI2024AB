from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    # aqui va el codigo
    '''----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------'''
    
    cedula = ''
    nombre = ''
    mesActual = 0
    
    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    ahorros = CuentaAhorros()
    corriente = CuentaCorriente()
    cdt = CDT()
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def CalcularSaldoToTal(self):
        #Forma 1
        return self.ahorros.ConsultarSaldo() + self.corriente.ConsultarSaldo()
        # #forma 2
        # total = self.ahorros.ConsultarSaldo() + self.corriente.ConsultarSaldo()
        # return total
        # # forma 3 - Forma no recomendada
        # total = self.ahorros.saldo + self.corriente.saldo
        # return total
        
    def ConsignarCuentaCorriente(self, monto):
        self.corriente.ConsignarMonto(monto)
        
    def ConsignarCuentaAhorros(self, monto):
        self.ahorros.ConsignarMonto(monto)
    
    def TransferirAhorrosACorriente(self):
        self.ConsignarCuentaCorriente(self.ahorros.ConsultarSaldo())
        self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
    
    def DuplicarAhorro(self):
        self.ConsignarCuentaAhorros(self.ahorros.ConsultarSaldo())
    
    def RetirarCuentaCorriente(self, monto):
        self.corriente.RetirarMonto(monto)
    
    def RetirarCuentaAhorros(self, monto):
        self.ahorros.RetirarMonto(monto)
    
    def RetirarTodo(self):
        
        total = self.CalcularSaldoToTal()
        self.TransferirAhorrosACorriente()
        self.RetirarCuentaCorriente(total)
        
        return total
    
    
    