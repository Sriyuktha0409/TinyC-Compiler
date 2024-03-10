from sly import Lexer
import argparse
apr=argparse.ArgumentParser()
apr.add_argument('-tokens',nargs=1)
args=apr.parse_args()
class Lexer1(Lexer):
    literals={',',';','(',')','{','}','[',']','='}
    tokens={INTEGER,INT,PRINT,ID,IF}
    ignore=' \t\n'
    INTEGER=r'[0-9]+'
    ID=r'[a-z A-Z]+'
    ID['print']=PRINT
    ID['int']=INT
    ID['if']=IF
f=open(args.tokens[0])
expr=f.read()
lexer=Lexer1()
if args.tokens is not None:
    with open(args.tokens[0]+'.tks','w') as i:
        for token in lexer.tokenize(expr):
            a=f'type={token.type}, value={token.value}'
            i.write(a + '\n')