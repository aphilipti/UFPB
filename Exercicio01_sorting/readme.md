# Ordenação por Comparação

## 📚 Disciplina

Estrutura de Dados e Complexidade de Algoritmos
Universidade Federal da Paraíba (UFPB)

---

## 🎯 Objetivo

Implementar e testar os algoritmos de ordenação por comparação:

* Selection Sort
* Insertion Sort

---

## 📁 Estrutura do Projeto

```
sorting/
│
├── main.py
├── selection_sort.py
├── insertion_sort.py
└── data/
```

---

## ▶️ Como Executar

Execute o programa via linha de comando informando:

* o arquivo de entrada (.in)
* o algoritmo desejado

### Sintaxe:

```
python main.py <arquivo> <algoritmo>
```

### Exemplos:

```
python main.py data/num.1000.2.in selection
python main.py data/num.1000.2.in insertion
```

---

## 📄 Formato dos Arquivos de Entrada

Os arquivos `.in` seguem o padrão:

```
n
valor1
valor2
valor3
...
```

Onde:

* A primeira linha (`n`) indica a quantidade de elementos
* As linhas seguintes representam os valores do vetor

---

## ⚙️ Algoritmos Implementados

### 🔹 Selection Sort

* Complexidade: O(n²)
* Não depende da ordem inicial dos dados

### 🔹 Insertion Sort

* Melhor caso: O(n)
* Pior caso: O(n²)
* Mais eficiente para listas quase ordenadas

---

## 📊 Saída do Programa

O programa exibe:

* Tamanho da entrada
* Tempo de execução
* Primeiros 10 elementos ordenados

Exemplo:

```
Tamanho da entrada: 1000
Tempo: 0.002345 segundos
Primeiros 10 elementos ordenados: [-50, -49, -48, ...]
```

---

## 🛠️ Requisitos

* Python 3.x

---

## 👨‍💻 Autor

Anderson Philip
