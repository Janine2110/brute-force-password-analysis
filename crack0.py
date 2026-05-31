from itertools import product
from string import digits, ascii_letters, punctuation
import time


def test_charset(name, charset, length):
    start = time.time()

    count = 0
    for _ in product(charset, repeat=length):
        count += 1

    elapsed = time.time() - start

    print(f"\n{name}")
    print(f"Caracteres disponíveis: {len(charset)}")
    print(f"Tamanho da senha: {length}")
    print(f"Combinações geradas: {count:,}")
    print(f"Tempo: {elapsed:.4f} segundos")


PASSWORD_LENGTH = 4

test_charset("Somente números", digits, PASSWORD_LENGTH)
test_charset("Somente letras", ascii_letters, PASSWORD_LENGTH)
test_charset(
    "Letras + números + símbolos",
    ascii_letters + digits + punctuation,
    PASSWORD_LENGTH
)