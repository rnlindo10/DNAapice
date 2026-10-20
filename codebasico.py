from random import choice
bases = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
cores = {'A' : '\033[31mA\033[0m', 'T' : '\033[33mT\033[0m', 'C' : '\033[32mC\033[m', 'G' : '\033[34mG\033[m'}
cores_par = {'A' : '\033[31mA\033[0m', 'T' : '\033[33mT\033[0m', 'C' : '\033[32mC\033[m', 'G' : '\033[34mG\033[m'}
quant = int(input("Quantidade de pares de bases nitrogenadas: "))

for i in range(quant):
    base = choice(list(bases.keys()))
    par = bases[base]
    if base in {'A', 'T'}:
        ponte = '='
    else:
        ponte = '\u2261'
    print(f'|{cores[base]}{ponte}{cores_par[par]}|')