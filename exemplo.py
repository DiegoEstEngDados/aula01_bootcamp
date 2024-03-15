CONSTANTE_BONUS = 1000

nome_usuario = str(input("Digite seu nome: "))
salario = float(input("Informe seu salário: "))
bonus = float(input("Informe seu bonus: "))
valor_bonus = CONSTANTE_BONUS + salario * bonus
print (f'O usuário {nome_usuario} possui o valor de bonus de {valor_bonus}')
