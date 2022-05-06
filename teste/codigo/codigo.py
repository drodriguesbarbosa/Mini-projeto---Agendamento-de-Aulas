class professor:

    def __init__(self, nome, especialidade, ativo):
        self.nome = nome
        self.especialidade = especialidade
        self.ativo = ativo

professor1 = professor('Prof. João', 'Biologia', True)
professor2 = professor('Prof. José', 'Matemática', True)
professor3 = professor('Prof. Maria', 'Português', True)

vetor_professores = []
vetor_professores.append(professor1)
vetor_professores.append(professor2)
vetor_professores.append(professor3)

class aluno:

    def __init__(self, nome, idade, grau_escolar):
        self.nome = nome
        self.idade = idade
        self.grau_escolar = grau_escolar

aluno1 = aluno('Pedro', 18, 'Ensino médio completo')
aluno2 = aluno('Carla', 15, 'Ensino médio cursando')
aluno3 = aluno('Isa', 26, 'Ensino superior cursando')

vetor_alunos = []
vetor_alunos.append(aluno1)
vetor_alunos.append(aluno2)
vetor_alunos.append(aluno3)

print(vetor_alunos[1].grau_escolar)

