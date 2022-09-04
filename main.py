class ControleRemoto:
    def __init__(self, cor, material, altura, profundidade, largura):
        self.cor = cor
        self.material = material
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == '+':
            print('Aumentar o Canal')
        elif botao == '-':
            print('Diminuir o Canal')


controle_remoto = ControleRemoto("preto", "plástico", "15cm", "2cm", "2cm")
print(controle_remoto.cor)
controle_remoto.passar_canal('+')

controle_remoto2 = ControleRemoto("cinza", "plástico", "16cm", "3cm", "3cm")
print(controle_remoto2.cor)
controle_remoto2.passar_canal('-')
