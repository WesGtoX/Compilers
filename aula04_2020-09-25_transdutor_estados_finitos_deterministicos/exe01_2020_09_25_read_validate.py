# -*- coding: utf-8 -*-
"""exe01_2020_09_25_read_validate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18KmuBUfhgJwml0z6EDVWXv9pjoDUrkE_

## COMPILADORES
#### WESLEY DE OLIVEIRA MENDES - 828.507

### Atividade:

- Desenvolva um programa na linguagem de programação de sua preferência que reconheça as seguintes palavras:

> ```
> { a,b , uma sequência impar de c(s), d,e }
> ```

### 1. Definir o autômato (formal, incluindo a tabela de transição).

M = ( estados, alfabeto, transições, inicial, final )

M = ( Q, Σ, δ, s, F )

Q: { s0, s1, s2, s3, s4, s5, s6 }

Σ: { a, b, c, d, e }

δ: 
> |   δ    |   a   |   b   |   c   |   d   |   e   |
> | :----: | :---: | :---: | :---: | :---: | :---: |
> | **s0** | _s1_  |   -   |   -   |   -   |   -   |
> | **s1** |   -   | _s2_  |   -   |   -   |   -   |
> | **s2** |   -   |   -   | _s3_  |   -   |   -   |
> | **s3** |   -   |   -   | _s4_  | _s5_  |   -   |
> | **s4** |   -   |   -   | _s3_  |   -   |   -   |
> | **s5** |   -   |   -   |   -   |   -   | _s6_  |
> | **s6** |   -   |   -   |   -   |   -   |   -   |

s: { s0 }

F: { s6 }

### 2. Escrever o programa que irá ler as palavras e validá-las por meio deste autômato.

#### Pytest
"""

# Commented out IPython magic to ensure Python compatibility.
!pip -q install pytest pytest-sugar

# move to tdd directory
from pathlib import Path
if Path.cwd().name != 'tdd':
#     %mkdir tdd
#     %cd tdd

# %pwd

# cleanup all files
# %rm *.py

"""#### Main Code"""

# Commented out IPython magic to ensure Python compatibility.
# %%file main.py
# 
# 
# class Automato:
# 
#     def __init__(self, values):
#         self.values = values
#         self.size = self.validate_entry()
#         self.states = {}
#         self.count_c = 0
# 
#     def validate_entry(self):
#         size = len(self.values)
#         if size >= 5:
#             return size
#         return self.fail()
# 
#     def run(self):
#         for k, v in enumerate(self.values):
# 
#             if not self.alphabet(v):
#                 break
# 
#             self.validate_transitions(v, k)
#         return self.final()
# 
#     def alphabet(self, value):
#         return True if value in 'abcde' else False
# 
#     def validate_transitions(self, value, index):
#         if value == 'a' and index == 0:
#             self.states.update({f's{index}': value})
# 
#         if value == 'b' and index == 1:
#             self.states.update({f's{index}': value})
# 
#         if value == 'c':
#             self.states.update({f's{index}': value})
#             self.count_c += 1
# 
#         if value == 'd':
#             self.states.update({f's{index}': value})
# 
#         if value == 'e':
#             self.states.update({f's{index}': value})
#             return
# 
#     def final(self):
#         if len(self.states) != self.size:
#             return self.fail()
# 
#         if self.count_c % 2 == 0:
#             return self.fail()
#         return self.success()
# 
#     def success(self):
#         return {'status': 200, 'result': 'Autômato válido!'}
# 
#     def fail(self):
#         return {'status': 400, 'result': 'Autômato NÃO válido!'}

"""#### Tests"""

# Commented out IPython magic to ensure Python compatibility.
# %%file test_main.py
# 
# 
# import pytest
# from main import Automato
# 
# 
# @pytest.mark.parametrize('value,result', 
#     [('abcde', 200), 
#      ('abccde', 400), 
#      ('abcccccde', 200), 
#      ('edcccba', 400), 
#      ('abcccccccde', 200), 
#      ('aabbccdd', 400), 
#      ('abcccde', 200), 
#      ('asdfas', 400)]
# )
# def test_is_automato_valid(value, result):
#     assert Automato(value).run()['status'] == result

!python3 -m pytest test_main.py

