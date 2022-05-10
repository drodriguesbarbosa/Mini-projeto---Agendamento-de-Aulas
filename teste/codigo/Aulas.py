from Aluno import Aluno
from Professor import Professor

class Aula(object):

    def __init__(self, nome, horario):
        self.nome = nome
        self.horario = horario

aula1 = Aula('Pedro', 'Prof.João', '12/05/2022 10:00')
aula2 = Aula('Carla', 'Prof. José', '24/05/2022 12:00')
aula3 = Aula('Isa', 'Prof. Maria', '15/05/2022 11:00')

vetor_aulas = []
vetor_aulas.append(aula1)
vetor_aulas.append(aula2)
vetor_aulas.append(aula3)

print(aula3.horario)

