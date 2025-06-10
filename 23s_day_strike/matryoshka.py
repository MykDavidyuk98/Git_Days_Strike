def matryoshka(n: int) -> None:
    if n == 1:
        print('Матроха')
    else:
        print(f'Верх матрьошки n =', n)
        matryoshka(n-1)
        print(f'Низ матрьошки n =', n)
