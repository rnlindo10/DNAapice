import time
import math
from random import choice

print("DNApice -> Emanuel, Gabriela, Isadora, Júlia, Lourdes, Pedro, Ryan, Sarah, Sophia - INFO1A")

bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
basesRNA = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

coresDNA = {
    'A': '\033[31mA\033[0m',
    'T': '\033[33mT\033[0m',
    'C': '\033[32mC\033[0m',
    'G': '\033[34mG\033[0m'
}

coresRNA = {
    'A': '\033[31mA\033[0m',
    'U': '\033[33mU\033[0m',
    'C': '\033[32mC\033[0m',
    'G': '\033[34mG\033[0m'
}

tipo = input("DNA ou RNA? ").strip().upper()
quant = int(input("Quantidade de pares de bases: "))

if tipo == 'DNA':
    bases_escolhidas = bases
    cores = coresDNA
elif tipo == 'RNA':
    bases_escolhidas = basesRNA
    cores = coresRNA
else:
    print("Digite DNA ou RNA!")
    raise SystemExit

modo = input(
    "A - Mostrar de 10 em 10\n"
    "B - Mostrar tudo de uma vez\n"
    "Escolha: "
).strip().upper()

contagem = {base: 0 for base in bases_escolhidas}


for i in range(quant):
    base = choice(list(bases_escolhidas.keys()))
    par = bases_escolhidas[base]
    contagem[base] += 1

    angulo = i * 0.65

    #posição das duas fitas
    x1 = math.sin(angulo)
    x2 = math.sin(angulo + math.pi)

    pos1 = round((x1 + 1) * 12)
    pos2 = round((x2 + 1) * 12)

    #escolhe a ligação entre as bases
    ponte = '=' if base in {'A', 'T', 'U'} else '≡'

    #monta a linha com as letras coloridas
    largura = 27
    linha = [' '] * largura

    inicio = min(pos1, pos2)
    fim = max(pos1, pos2)

    #ligações entre as fitas
    for j in range(inicio + 1, fim):
        linha[j] = '-'

    linha[pos1] = cores[base]
    linha[pos2] = cores[par]

    #coloca a ligação no centro
    meio = (pos1 + pos2) // 2
    linha[meio] = ponte

    print(''.join(linha))

    if modo == 'A' and (i + 1) % 10 == 0:
        input("\nPressione Enter para continuar...")
    elif modo == 'A':
        time.sleep(0.1)

print("\nPorcentagem das bases:")

for base, total in contagem.items():
    porcentagem = total / quant * 100 if quant else 0
    print(f"Base {base}: {total} vez(es) - {porcentagem:.1f}%")