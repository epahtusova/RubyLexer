from tokens import *


class Lexer:
    def __init__(self, file_name):
        self.position = 0
        self.tokens = generate_tokens(file_name)

    def get_next_token(self):
        # get the next token from list of tokens
        if self.position < len(self.tokens):
            tmp = self.position
            self.position += 1
            return self.tokens[tmp]


def read_file(file):
    f_in = open(file, encoding='utf8')
    src_code = f_in.read()
    return src_code


def generate_tokens(file):
    src_code = read_file(file)
    pos = 0
    tokens = []

    while pos < len(src_code):
        while pos < len(src_code) and src_code[pos].isspace():
            # Skip spaces
            pos += 1

        if pos < len(src_code) and src_code[pos] == '#':
            # Skip comments
            while src_code[pos] != '\n':
                pos += 1

        if pos < len(src_code) - 10 and src_code[pos] == '=':
            # Skip embedded documentation
            if src_code[pos + 1] == 'b' and src_code[pos + 2] == 'e' and src_code[pos + 3] == 'g' and \
                    src_code[pos + 4] == 'i' and src_code[pos + 5] == 'n':
                while not (src_code[pos - 1] in ['\n', ' '] and src_code[pos] == '=' and src_code[pos + 1] == 'e'
                           and src_code[pos + 2] == 'n' and src_code[pos + 3] == 'd'):
                    pos += 1
                pos += 4

        current_token = ""

        if pos < len(src_code) and (src_code[pos].isalpha() or src_code[pos] in ['$', '@', '_']):
            # Identifier or keyword
            current_token += src_code[pos]
            pos += 1

            while pos < len(src_code) and (src_code[pos].isalnum() or src_code[pos] == '_'):
                current_token += src_code[pos]
                pos += 1
                if pos >= len(src_code):
                    break

            if pos < len(src_code) and src_code[pos] == '?':
                current_token += '?'
                pos += 1

            if current_token in keywords:
                tokens.append(("Keyword", current_token))
            else:
                tokens.append(("Identifier", current_token))

        elif pos < len(src_code) and src_code[pos] in [
            ',', ':', ';', '+', '-', '*', '/', '%', '!', '&', '|',
            '~', '^', '<', '=', '>', '.', ',', '\\'
        ]:
            # Delimiter or operator
            # Take the longest fitting option
            while pos < len(src_code) and (any(op.startswith(current_token + src_code[pos]) for op in operators) or
                                           any(dl.startswith(current_token + src_code[pos]) for dl in delimiters)):
                current_token += src_code[pos]
                pos += 1

            if current_token in operators:
                tokens.append(('Operator', current_token))

            elif current_token in delimiters:
                tokens.append(('Delimiter', current_token))
            else:
                tokens.append(('Other operator', current_token))

        elif pos < len(src_code) and src_code[pos] == '?':
            # Literal like ?b should return ASCII code of character after ?
            pos += 1
            current_token = '?' + src_code[pos]
            pos += 1
            tokens.append(('ASCII code', current_token))

        elif pos < len(src_code) and src_code[pos] == '0':
            current_token += '0'
            pos += 1
            if (src_code[pos] not in ['x', 'b', '.']) and (not src_code[pos].isdigit()):
                # zero
                tokens.append(('Integer number', current_token))
            # It's a non-decimal literal:
            elif src_code[pos] == 'x':
                # hex
                current_token += 'x'
                pos += 1
                while pos < len(src_code) and (
                        src_code[pos].isdigit() or src_code[pos] in ['a', 'b', 'c', 'd', 'e', 'f', 'A',
                                                                     'B', 'C', 'D', 'E', 'F']):
                    current_token += src_code[pos]
                    pos += 1
                tokens.append(('Hex number', current_token))

            elif src_code[pos] == 'b':
                # bin
                current_token += 'b'
                pos += 1
                while pos < len(src_code) and src_code[pos] in ['0', '1']:
                    current_token += src_code[pos]
                    pos += 1
                tokens.append(('Bin number', current_token))

            elif src_code[pos] != '.':
                # oct
                while pos < len(src_code) and src_code[pos] in ['0', '1', '2', '3', '4', '5', '6', '7']:
                    current_token += src_code[pos]
                    pos += 1
                tokens.append(('Oct number', current_token))

            elif src_code[pos] == '.':  # TODO 0.(a) problem
                # float starting with 0
                # if src_code[pos+1].isdigit(): and tab everything
                current_token += '.'
                pos += 1
                while pos < len(src_code) and (src_code[pos].isdigit() or src_code[pos] == '_'):
                    # Underscores within decimal digits are ignored
                    current_token += src_code[pos]
                    pos += 1
                tokens.append(('Float number', current_token))

        elif pos < len(src_code) and src_code[pos].isdigit() and src_code[pos] != '0':
            # int or float
            current_token += src_code[pos]
            pos += 1
            flag = True
            while pos < len(src_code) and flag:
                if src_code[pos] == '_':
                    current_token += '_'
                    pos += 1
                if src_code[pos].isdigit() or src_code[pos] in ['e', 'E']:
                    current_token += src_code[pos]
                    pos += 1
                elif src_code[pos] == '.' and src_code[pos + 1].isdigit():
                    current_token += src_code[pos]
                    pos += 1
                elif src_code[pos] in ['+', '-'] and current_token[-1] in ['E', 'e']:
                    current_token += src_code[pos]
                    pos += 1
                else:
                    flag = False
            if current_token.__contains__('.'):
                tokens.append(('Float number', current_token))
            else:
                tokens.append(('Integer number', current_token))

        elif pos < len(src_code) and src_code[pos] == '"':
            # string literal between ''
            current_token += src_code[pos]
            pos += 1
            while src_code[pos] != '"':
                current_token += src_code[pos]
                pos += 1
            current_token += src_code[pos]
            pos += 1
            tokens.append(('Literal', current_token))

        elif pos < len(src_code) and src_code[pos] == "'":
            # string literal between ""
            current_token += src_code[pos]
            pos += 1
            while src_code[pos] != "'":
                current_token += src_code[pos]
                pos += 1
            current_token += src_code[pos]
            pos += 1
            tokens.append(('Literal', current_token))

        elif pos < len(src_code) and src_code[pos] in left_par:
            # Left parenthesis
            current_token += src_code[pos]
            tokens.append(('Left parenthesis', current_token))
            pos += 1

        elif pos < len(src_code) and src_code[pos] in right_par:
            # Right parenthesis
            current_token += src_code[pos]
            tokens.append(('Right parenthesis', current_token))
            pos += 1

        elif pos < len(src_code) and src_code[pos] in ['\n', '\r', '\t', '\f', '\b', '\a']:
            # Skip unicode special characters
            pos += 1

        else:
            if pos < len(src_code):
                current_token = src_code[pos]
                pos += 1
                tokens.append(('Unrecognized token', current_token))

    return tokens
