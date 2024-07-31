import re

class ValidaCpf:
    def __init__(self, cpf):
        self.cpf = cpf

    def valida(self):
        if not self.cpf:
            return False
        
        novo_cpf = self.calcula_digitos(self.cpf[:9])
        novo_cpf = self.calcula_digitos(novo_cpf)

        if novo_cpf == self.cpf:
            return True
        return False
    

    @staticmethod   
    def calcula_digitos(fatia_cpf):
        if not fatia_cpf:
            return False
        
        sequencia = fatia_cpf[0] * len(fatia_cpf)
        
        if sequencia == fatia_cpf:
            return False
        
        soma = 0
        for chave, multiplicador in enumerate(range(len(fatia_cpf) + 1 ,1,-1)):
            soma += int(fatia_cpf[chave]) * multiplicador


        resto = 11 - (soma % 11)
        resto = resto if resto <= 9 else 0

        return fatia_cpf + str(resto)
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self.so_numeros(cpf)

    @staticmethod
    def so_numeros(cpf):
        return re.sub('[^0-9]', '', cpf)