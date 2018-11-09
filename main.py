from lexer import Lexer

f_out = open('out.txt', 'w')
lexer = Lexer('in.txt')
for i in range(len(lexer.tokens)):
    f_out.write(str(lexer.get_next_token())+'\n')
