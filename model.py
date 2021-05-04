class Pessoas:
    def __init__(self, cpf, nome, dataNascimento, UsaOculos):
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.UsaOculos = UsaOculos


class Marca:
    def __init__(self, nome, sigla):
        self.id = None
        self.nome = nome
        self.sliga = sigla


class Veiculos:
    def __init__(self, placa, ano, cor, motor, proprietario, marca):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.proprietario = proprietario
        self.marca = marca
