



def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)


lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
print(*lista, *lista2)