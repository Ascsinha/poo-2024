class Aluno:
    
    def __init__ (self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie

aluno1 = Aluno('Maria José', 'Informática', '1º ano')
print (f'Série do aluno 1: {aluno1.serie}.')

aluno1.serie = '3º ano'
print (f'Nova série do aluno 1: {aluno1.serie}.')

aluno2 = Aluno('Carlos Felipe', 'Comércio', '3º ano')
print (f'Série do aluno 2: {aluno2.serie}.')

aluno2.serie = '4º ano'
print (f'Nova série do aluno 2: {aluno2.serie}.')

aluno3 = Aluno('Bianca Cruz', 'Comércio', '2º ano')
print (f'Série do aluno 3: {aluno3.serie}.')