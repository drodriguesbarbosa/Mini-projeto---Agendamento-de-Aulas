class Aluno:

    def __init__(self, nome, idade, grau_escolar):
        self.nome = nome
        self.idade = idade
        self.grau_escolar = grau_escolar

aluno1 = Aluno('Pedro', 18, 'Ensino médio completo')
aluno2 = Aluno('Carla', 15, 'Ensino médio cursando')
aluno3 = Aluno('Isa', 26, 'Ensino superior cursando')

vetor_alunos = []
vetor_alunos.append(aluno1)
vetor_alunos.append(aluno2)
vetor_alunos.append(aluno3)   

