def Aprovação(nome, nota_1, nota_2, nota_3,total_faltas):
#calculando a porcentagem de faltas:
    faltas = float(100*(total_faltas/80))
#calculando média:
    média = float((nota_1+nota_2+nota_3)/3)
#condições e situações de aprovação:
    if faltas <= 25 and média >= 7.0:
        print("Nome: ",nome,"Média: ",média, "Faltas:% ",faltas, "Aprovado")
    elif faltas > 25:
        print("Nome: ",nome,"Média: ",média, "Faltas:% ",faltas, "Reprovado por Falta")
    elif média <= 7.0 and faltas <= 25:
        print("Nome: ",nome,"Média: ",média, "Faltas:% ",faltas, "Reprovado por Média")


nome=input("Nome do Aluno:")
notas= [float(i) for i in input("Digite as 3 notas separadas por um espaço:").split()]
if len(notas)!= 3:
    print("Erro: Digite apenas 3 notas")
    quit()
faltas=int(input("Número de faltas:"))

Aprovação(nome,notas[0],notas[1],notas[2],faltas)