import unittest
from lexer import Lexer


class TestLexer(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_tokens(self):
        lexer = Lexer('test.txt')
        result = []
        for i in range(len(lexer.tokens)):
            result.append(lexer.get_next_token())

        self.assertEqual(result, [('Keyword', 'def'),
                                  ('Identifier', 'sqr'),
                                  ('Left parenthesis', '('),
                                  ('Identifier', 'x'),
                                  ('Right parenthesis', ')'),
                                  ('Keyword', 'return'),
                                  ('Identifier', 'x'),
                                  ('Operator', '*'),
                                  ('Identifier', 'x'),
                                  ('Keyword', 'end'),
                                  ('Left parenthesis', '('),
                                  ('Identifier', 'rand'),
                                  ('Left parenthesis', '('),
                                  ('Integer number', '4'),
                                  ('Right parenthesis', ')'),
                                  ('Operator', '+'),
                                  ('Integer number', '2'),
                                  ('Right parenthesis', ')'),
                                  ('Delimiter', '.'),
                                  ('Identifier', 'times'),
                                  ('Left parenthesis', '{'),
                                  ('Identifier', 'a'),
                                  ('Operator', '='),
                                  ('Identifier', 'rand'),
                                  ('Left parenthesis', '('),
                                  ('Integer number', '300'),
                                  ('Right parenthesis', ')'),
                                  ('Identifier', 'print'),
                                  ('Identifier', 'a'),
                                  ('Delimiter', ','),
                                  ('Literal', '"^2 = "'),
                                  ('Delimiter', ','),
                                  ('Identifier', 'sqr'),
                                  ('Left parenthesis', '('),
                                  ('Identifier', 'a'),
                                  ('Right parenthesis', ')'),
                                  ('Delimiter', ','),
                                  ('Literal', '"\\n"'),
                                  ('Right parenthesis', '}'),
                                  ('Identifier', 'print'),
                                  ('Literal', '"\\n"'),
                                  ('Keyword', 'def'),
                                  ('Identifier', 'boom'),
                                  ('Identifier', 'print'),
                                  ('Literal', '"Boom!\\n"'),
                                  ('Keyword', 'end')
                                  ])


if __name__ == '__main__':
    unittest.main()
