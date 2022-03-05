import random
class Dado:
    def __init__(self) -> None:
        self.valor=1
        self.valorfinal=6
        self.escrever='vc quer rolar o dado responda sim ou nao '
    def rolar_o_dado(self):
        print(random.randint(self.valor,self.valorfinal))
    def iniciar(self):
        mensagem=input(self.escrever)
        try:
            if mensagem=='sim' or mensagem=='s':
                self.rolar_o_dado()
                self.iniciar()
            elif mensagem=='nao' or mensagem=='n':
                print('obrigado por participar')
            else:
                print('escreva sim ou nao')
                self.iniciar()
        except Exception as err:
            print(err)
dado=Dado()
dado.iniciar()