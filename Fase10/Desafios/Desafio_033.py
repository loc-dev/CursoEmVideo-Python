#   Fase 10 - Condições ( Parte 1 )
#   Desafio 33
#   Faça um programa que pergunte salário de um funcionário
#   e calcule o valor do seu aumento.
#   Para salários superiores a R$ 1200,00, calcule um aumento de 10%.
#   Para os inferiores ou iguais, o aumento é de 15%.

nome = str(input('Digite o seu nome: '))
salario = float(input('Olá {}, digite o seu salário : R$ '.format(nome)))


if salario <= 1200.00:
    n_salario = ((salario * 15) / 100) + salario
    print('{}, receberá um aumento de 15%,'
          ' então, o seu salário será R$ {:.2f}'.format(nome, n_salario))
else:
    n_salario = ((salario * 10) / 100 + salario)
    print('{}, receberá um aumento de 10%,'
          ' então, o seu salário será R$ {:.2f}'.format(nome, n_salario))
