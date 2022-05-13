from datetime import datetime

from Aluno import Aluno
from Professor import Professor
from Aula import Aula

aluno = Aluno('Daniela', 28, 'superior')
professor = Professor('Jonas', 35, 'Biologia', True)
aula = Aula(aluno, professor, datetime.strptime('2022-04-22 20:00:00', "%Y-%m-%d %H:%M:%S"))

list_aulas = []
list_aulas.append(aula)

print(aula.aluno.nome)
print(aula.professor.nome)
print(aula.horario)

print(list_aulas)