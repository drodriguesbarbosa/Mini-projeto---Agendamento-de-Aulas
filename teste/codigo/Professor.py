
class Professor (Pessoa):

    def __init__(self, nome, especialidade, ativo):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.ativo = ativo

professor1 = Professor('Prof. João', 'biologia', True)
professor2 = Professor('Prof. josé', 'matemática', True)
professor3 = Professor('Prof. Maria', 'português', True)

vetor_professores = []
vetor_professores.append(professor1)
vetor_professores.append(professor2)
vetor_professores.append(professor3)

print(professor3.nome)