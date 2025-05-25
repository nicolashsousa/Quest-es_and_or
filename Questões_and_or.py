#Questão1
media = float(input("Digite a sua media:"))
frequencia = float(input("Digite sua porcentagem de frequencia:"))
if media > 7 and frequencia > 75:
    print("Aprovado")
else:
    print("Reprovado")
#Questão2
nota1 = float(input("Digite a 1° nota:"))
nota2 = float(input("Digite a 2° nota:"))
nota3 = float(input("Digite a 3° nota:"))
carga_horaria = float(input("Digite a carga horaria da materia:"))
faltas = float(input("Digite o n° de aulas que faltou:"))
media = (nota1 + nota2 + nota3)/3
frequencia = (1-(faltas/carga_horaria))*100
if media > 7 and frequencia > 75:
    print("Aprovado")
else:
    print("Reprovado")
#Questão3
print("Segunda = 1 até domingo = 7")
dia = int(input("Digite o n° do dia da semana:"))
if dia == 1 or dia == 3 or dia == 5:
    print("Dia de academia")
else:
    print("Não é dia de academia")
#Questão4
periodo = int(input("Digite o seu periodo:"))
if periodo == 1 or periodo == 2 or periodo == 3 or periodo == 4:
    print("Pode participar do PIBID")
else:
    print("Não pode participar do PIBID")
#Questão5
salario = float(input("Digite seu salario:"))
if 1000 <= salario and salario <= 3000:
    print("Imposto de 100R$")
else:
    print("Não paga imposto")
#Questão6
nota = input("Digite sua nota:").title()
if nota == "A" or nota == "B":
    print("Medalha de Ouro")
elif nota == "C" or nota == "D":
    print("Medalha de Prata")
else:
    print("Medalha de Bronze")
#Questão7
nota = float(input("Digite sua nota:"))
if 9 <= nota <= 10:
    print(nota,"= A")
elif 7 <= nota <= 8.9:
    print(nota,"= B")
elif 5 <= nota <= 6.9:
    print(nota,"= C")
elif 3 <= nota <= 4.9:
    print(nota,"= D")
else:
    print(nota,"= E")
#Questão8
salario = float(input("Digite seu salario:"))
if salario <= 2428.8:
    imposto = salario*0
    print("Imposto:",imposto,"R$")
elif 2428.81 <= salario <= 2826.65:
    imposto = salario*0.075
    print("Imposto:",imposto,"R$")
elif 2826.66 <= salario <= 3751.05:
    imposto = salario*0.15
    print("Imposto:",imposto,"R$")
elif 3751.06 <= salario <= 4664.68 :
    imposto = salario*0.225
    print("Imposto:",imposto,"R$")
else:
    imposto = salario*0.275
    print("Imposto:",imposto,"R$")
