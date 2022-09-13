
while True:
   # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]         #Elimina os dois últimos digitos  do CPF
    reverso = 10        # Contador reverso
    total = 0
    for index in range(19):
        if index > 8:       # Primeiro índice vai de 0 a 9,
            index -= 9      # São  os 9 primeiros digitos do CPF
    #    print(cpf[index], index, reverso)

        total += int(novo_cpf[index]) * reverso         # Valor total da multiplicação

        reverso -= 1        # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    if cpf == novo_cpf:
        print('Válido')
    else:
        print('Inválido')



