Compiladores - TEORIA DOS CONJUNTOS E LINGUAGENS

Wesley de Oliveira Mendes - 828.507


Atividade do dia 02/10/2020 - Linguagens (Introdução)

1. (UNESP) Numa classe de 30 alunos, 16 gostam de Matemática e 20 gostam de História. O número de alunos desta classe que gostam de Matemática e História é:
a) exatamente 16
b) exatamente 10
c) no máximo 6
d) no mínimo 6
e) exatamente 18

> RESPOSTA: (D)


2. (PUC) Numa pesquisa de mercado, verificou-se que 15 pessoas utilizam pelo menos um dos produtos A ou B. Sabendo que 10 destas pessoas não usam o produto B e que 2 destas pessoas não usam o produto A, qual é o número de pessoas que utilizam os produtos A e B?

> RESPOSTA: Pelo menos 3 pessoas


3. Numa pesquisa realizada, verificou-se que, das pessoas consultadas 100 liam o jornal A, 150 liam o jornal B, 20 liam os dois jornais A e B e 110 não liam nenhum dos jornais. Quantas pessoas foram consultadas? 
a) 250 b) 230 c) 340 d) 380

> RESPOSTA: (C)


4. Numa cidade são consumidos três refrigerantes: Coca-Cola, Fanta e Guaraná. Feito um levantamento de mercado sobre o consumo destes refrigerantes, obteve-se o seguinte resultado disposto na tabela a seguir:

Pergunta-se, quantas pessoas consomem apenas Coca-Cola

| PRODUTOS                   | NÚMERO DE CONSUMIDORES |
| -------------------------- | :--------------------: |
| Coca-Cola                  |          1500          |
| Fanta                      |          2000          |
| Guaraná                    |          2500          |
| Coca-Cola e Guaraná        |          700           |
| Coca-Cola e Fanta          |          900           |
| Fanta e Guaraná            |          800           |
| Coca-Cola, Fanta e Guaraná |          600           |
| NENHUM DOS TRÊS            |          1800          |

a) 500 b) 600 c) 800 d) 1000

> RESPOSTA: (A)


5. Sobre a terminologia de Linguagens Formais, define e apresente três exemplos dos conceitos de: 
- Alfabeto: ou também vocabulário, é um conjunto finito, não vazio, de simbolos (elementos).
  - Exemplo:
    - V = {a, b, c, ..., z }
    - V = {0, 1}
    - V = {a, e, i, o, u}

- Símbolo: são elementos de um alfabeto, representam uma unidade dentro do alfabeto
  - Exemplo: V = {0, 1}, Q = {a, e, i, o, u}, S = {=, #}
    - 0, 1 são simbolos de V
    - a, e, i, o, u são simbolos de Q
    - =, # são simbolos de S

- Cadeias: são palavras que são contruidas por meio dos simbolos do alfabeto, concatenação dos simbolos do alfabeto
  - Exemplo:
    - Alfabeto: V = {a, b}, são cadeias:
      - a, b, aab, abbb, ...
    - Alfabeto: Q = {#, =, -}, são cadeias:
      - #=-, #==, ===#, ...
    - Alfabeto: L = {0, 1}, são cadeias:
      - 1, 0, 110, 0001, 1011, ...


- Cadeia vazia: sentença que não possui simbolos, uma sentença de tamanho 0.
  - Exemplo:
    - |ε| = 0

- Fechamento do alfabeto: é o conjunto das cadeias de qualquer comprimento sobre o alfabeto, representado por V* e V+ (fechamento positivo).
  - Exemplo: V = {0, 1}
    - V* = {λ, 0, 1, 00, 01, 11, 000,...}
    - V+ = {0, 1, 00 ,01, 11, 000,...}

- Concatenação do alfabeto: junção de caracteres
  - Exemplo: dado o alfabeto: Σ = {a, b, c, d} e as cadeias: α = abc, β = dbaca e σ = a
    - α·β = αβ = abcdbaca
    - β·α = βα = dbacaabc
    - α·σ = ασ = abca

- Comprimento da cadeia: é o número de elementos que existe na cadeia.
  - Exemplo: dado o alfabeto: Σ = {a, b, c, d} e as cadeias: α = abc, β = dbaca e σ = a
    - |αβ| = |α| + |β| = 3 + 5 = 8
    - |βα| = |β| + |α| = 5 + 3 = 8
    - |ασ| = |α| + |σ| = 3 + 1 = 4

- Número de ocorrências de um símbolo: é o número de elementos de um simbolo.
  - Exemplo: α = {z, x}
    - |zzzxx| = 5
    - |λ| = 0
    - |xxzzz|x = 2
    - |zxx|z = 1

- Potência de um alfabeto: β^n é a repetição um sentença β, n vezes.
  - Exemplo:
    - x = ab, então x^3 = ababab
    - β = {0, 1}, então β^2 {00, 01, 010, 11}
    - β = {0, 1}, então β^3 {000, 001, 010, 011, 100, 101, 110, 111}

- Linguagem: uma linguagem L sobre um alfabeto V, é um subconjunto de V*.
  - Exemplo: seja V o alfabeto {a, b}, uma linguagem constituída pelas 15 palavras mais curtas de V*:
    - A = {λ, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb}
    - A = {s ∈ V* | λ <= |s| <= 3}
