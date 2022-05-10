class Aula(object):

    def __init__(self, nomeAluno, nomeProfessor, horario):
        self.nomeAluno = nomeAluno
        self.nomeProfessor = nomeProfessor
        self.horario = horario

class Professor(Aula):
    def __init__(self, nomeProfessor, especialidade, ativo):
        super().__init__(nomeProfessor)
        self.especialidade = especialidade
        self.ativo = ativo

class Aluno:

    def __init__(self, nomeAluno, idade, grau_escolar):
        self.nome = nomeAluno
        self.idade = idade
        self.grau_escolar = grau_escolar

from Professor import Professor
from Aluno import Aluno

aula1 = Professor (nomeProfessor = 'João', especialidade = 'Português', ativo = True)


