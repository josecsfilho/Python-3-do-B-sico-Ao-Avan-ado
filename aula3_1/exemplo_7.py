
#sets
#s1 = {1,2,3,4,5,7}
#s2 = {1,2,3,4,5,6}
#s3 = s1 ^ s2
#print(s3)

l1 = ['Jose', 'Jose', 'Filho']
l2 = ['Jose', 'Silva', 'Carlos',
      'Jose', 'Jose','Jose', 'Jose']

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')