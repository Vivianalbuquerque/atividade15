# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR
retaA =float(input("qual o valor da reta A?"))
retaB =float(input("qual o valor da reta B?"))
retaC =float(input("qual o valor da reta C?"))
if retaA + retaB + retaC and retaA + retaC > retaB and retaB + retaC > retaA:
    print("forma um triângulo :)")
else:
    print("não forma um triângulo :(")