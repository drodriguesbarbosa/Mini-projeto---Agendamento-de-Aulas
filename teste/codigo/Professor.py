from Pessoa import Pessoa

class Professor (Pessoa):

    def __init__(self, nome, idade, especialidade, ativo):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.ativo = ativo

p1 = Professor('Joao', 22, 'Farmacologia', True)
p2 = Professor('Simone', 50, 'Homeopatia', False)
p3 = Professor('Marcos', 54, 'Saúde Pública', True)

print(p1.ativo)