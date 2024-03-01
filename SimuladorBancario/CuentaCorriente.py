class CuentaCorriente:
    # aqui va el codigo
    '''----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------'''
    saldo = 0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    def ConsultarSaldo(self):
        return self.saldo
    
    def ConsignarMonto(self, monto):
        # Forma 1
        self.saldo += monto
        # Forma 2
        # self.saldo = self.saldo + monto
        
    def RetirarMonto(self, monto):
        # Forma 1
        self.saldo -= monto
        # Forma 2
        # self.saldo = self.saldo - monto