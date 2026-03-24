import sys
import time
import os
from selection_sort import selection_sort
from insertion_sort import insertion_sort


def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split()

    n = int(lines[0])                 # primeira linha = tamanho
    data = list(map(int, lines[1:]))  # resto = valores

    if len(data) != n:
        print("Aviso: tamanho informado diferente da quantidade de dados")

    return data


def init_log():
    if not os.path.exists("resultados.txt"):
        with open("resultados.txt", "w") as f:
            f.write("arquivo | algoritmo | tempo\n")
            f.write("--------------------------------\n")


def main():
    if len(sys.argv) < 3:
        print("Uso: python main.py <arquivo> <algoritmo>")
        print("Algoritmos: selection | insertion")
        return

    file_path = sys.argv[1]
    algorithm = sys.argv[2]

    data = read_file(file_path)

    print(f"Tamanho da entrada: {len(data)}")

    start = time.time()

    if algorithm == "selection":
        result = selection_sort(data.copy())
    elif algorithm == "insertion":
        result = insertion_sort(data.copy())
    else:
        print("Algoritmo inválido")
        return

    end = time.time()

    execution_time = end - start

    print(f"Tempo: {execution_time:.6f} segundos")
    print("Primeiros 10 elementos ordenados:", result[:10])

    # 🔽 Inicializa arquivo de log (se não existir)
    init_log()

    # 🔽 Escreve no log
    file_name = os.path.basename(file_path)
    log_line = f"{file_name} | {algorithm} | {execution_time:.6f}\n"

    with open("resultados.txt", "a") as f:
        f.write(log_line)


if __name__ == "__main__":
    main()