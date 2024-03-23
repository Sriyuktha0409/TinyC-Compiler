from sly import Lexer
class LexicalAnalyzer(Lexer):
    literals = {'(',')','{','}',';',',','='}
    tokens = {NUMBER,ID,INT,PRINT}
    ignore = ' \t'
    NUMBER = r'[0-9]+'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['int'] = INT
    ID['print'] = PRINT
    def NUMBER(self, t):
        t.value = int(t.value)
        return t
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    def error(self, t):
        print(f"Illegal character {t.value[0]} on line{self.lineno} {self.index}")
        self.index += 1