"""
COMPILADORES
WESLEY DE OLIVEIRA MENDES - 828.507


1. Definir o autômato (formal, incluindo a tabela de transição).
    M = ( estados, alfabeto, transições, inicial, final )

    M = ( Q, Σ, δ, s, F )

    Q: { s0, s1, s2, s3, s4, s5, s6 }

    Σ: { a, b, c, d, e }

    δ: 
    |   δ   |   a   |   b   |   c   |   d   |   e   |
    | :---: | :---: | :---: | :---: | :---: | :---: |
    |  s0   |  s1   |   -   |   -   |   -   |   -   |
    |  s1   |   -   |  s2   |   -   |   -   |   -   |
    |  s2   |   -   |   -   |  s3   |   -   |   -   |
    |  s3   |   -   |   -   |  s4   |  s5   |   -   |
    |  s4   |   -   |   -   |  s3   |   -   |   -   |
    |  s5   |   -   |   -   |   -   |   -   |  s6   |
    |  s6   |   -   |   -   |   -   |   -   |   -   |

    s: { s0 }

    F: { s6 }

2. Escrever o programa que irá ler as palavras e validá-las por meio deste autômato.
"""
import pytest


class Automato:

    def __init__(self, values):
        self.values = values
        self.size = self.validate_entry()
        self.states = {}
        self.count_c = 0

    def validate_entry(self):
        size = len(self.values)
        if size >= 5:
            return size
        return self.fail()

    def run(self):
        for k, v in enumerate(self.values):

            if not self.alphabet(v):
                break

            self.validate_transitions(v, k)
        return self.final()

    def alphabet(self, value):
        return True if value in 'abcde' else False

    def validate_transitions(self, value, index):
        if value == 'a' and index == 0:
            self.states.update({f's{index}': value})

        if value == 'b' and index == 1:
            self.states.update({f's{index}': value})

        if value == 'c':
            self.states.update({f's{index}': value})
            self.count_c += 1

        if value == 'd':
            self.states.update({f's{index}': value})

        if value == 'e':
            self.states.update({f's{index}': value})
            return

    def final(self):
        if len(self.states) != self.size:
            return self.fail()

        if self.count_c % 2 == 0:
            return self.fail()
        return self.success()

    def success(self):
        return {'status': 200, 'result': 'Autômato válido!'}

    def fail(self):
        return {'status': 400, 'result': 'Autômato NÃO válido!'}


@pytest.mark.parametrize('value,result', 
    [('abcde', 200), 
     ('abccde', 400), 
     ('abcccccde', 200), 
     ('edcccba', 400), 
     ('abcccccccde', 200), 
     ('aabbccdd', 400), 
     ('abcccde', 200), 
     ('asdfas', 400)]
)
def test_is_automato_valid(value, result):
    assert Automato(value).run()['status'] == result
