'''print('''  Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0                      A
      Entre 7.5 e 9.0                        B
      Entre 6.0 e 7.5                        C
      Entre 4.0 e 6.0                        D
      Entre 4.0 e zero                      E
    ''')
nota1=float(input("informe numero?"))
nota2=float(input("informe numero?"))
media= (nota1+nota2)/2
if media>=9.0 and media <= 10.0:
    print(f"o aluno se enconra no conceito A com a media {media}")
elif media>=7.5 and media < 9.0:
    print(f"o aluno se enconra no conceito b com a media {media}")
elif media >= 6.0 and media < 7.5:
        print(f"o aluno se enconra no conceito c com a media {media}")
elif media>=6.0 and media < 4.0:
    print(f"o aluno se enconra no conceito d com a media {media}")
elif media >= 0.0 and media < 4.0:
        print(f"o aluno se enconra no conceito e com a media {media}")'''

nota=float(input("informe a nota?"))
while nota <0 and nota > 10:
    print(nota)
    nota = float(input("informe a nota?"))












