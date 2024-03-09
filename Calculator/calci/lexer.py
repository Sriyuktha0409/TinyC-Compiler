from sly import Lexer
class Calclexer(Lexer):
	literals = {"+","-","*","/","(",")"}
	tokens = {INTEGER,NEWLINE,ID}
	ignore = '\t'
	NEWLINE=r'\n'
	INTEGER = r'[0-9]+'
	def INTEGER(self,t):
		t.value = int(t.value)
		return t
	ID=r'[a-z]+'