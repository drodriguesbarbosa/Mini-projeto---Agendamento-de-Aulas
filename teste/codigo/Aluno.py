from Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, idade, grau_escolar):
        super().__init__(nome, idade)
        self.grau_escolar = grau_escolar

a1 = Aluno('Daniela', 28, 'superior')
a2 = Aluno('Julia', 29, 'Pós Graduação')
a3 = Aluno('Gabriel', 16, 'Ensino Médio')

print(a1.grau_escolar)


