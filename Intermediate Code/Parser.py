from sly import Parser
from Lexer import tinyclexer
from SymbolTable import *
from IntermediateCode import *
from Program import *
from Function import *
from enum import Enum
from Ast import *
DataType = Enum('DataType',['INT','DOUBLE'])
class tinycparser(Parser):
    tokens = tinyclexer.tokens
    literals = tinyclexer.literals
    precedence = (('left',"+","-"),('left',"*","/","%"))
    lst = []
    localsymboltable = SymbolTable()
    prog = Program()
    @_(' return_type ID "(" ")" "{" statements "}" ')
    def program(self,value):
        fun = Function(int,value.ID)
        fun.setIntermediateCodeList(value.statements)
        self.prog.addFunctionDetails(value.ID,fun)
        #self.localsymboltable.printSymbolTable()
    def print(self):
        return fun
    @_(' INT ')
    def return_type(self,value):
        pass
    @_(' statement ";" statements ')
    def statements(self,value):
        return value[2]
    @_(' statement ";" ')
    def statements(self,value):
        return value[0]
    @_('dec_st')
    def statement(self,value):
        pass
    @_('ass_st')
    def statement(self,value):
        self.lst.append(value[0])
        return self.lst
    @_('print_st')
    def statement(self,value):
        pass
    @_(' INT ',' DOUBLE ')
    def type(self,value):
        pass
    @_(' type list_var')
    def dec_st(self,value):
        for i in value.list_var:
            obj = SymbolTableEntry(i,int)
            self.localsymboltable.addSymbol(obj)
    @_(' ID "," list_var ')
    def list_var(self,value):
        return [value.ID] + value.list_var
    @_(' ID ')
    def list_var(self,value):
        return [value.ID]
    @_(' expr "+" expr ')
    def expr(self,value):
        if (value[0].getDatatype() == int and value[2].getDatatype() == int):
            t = NewTemp(int)
            obj = Quadruple(value.expr0,value.expr1,t,'+')
        elif (value[0].getDatatype() == double and value[2].getDatatype() == int):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'+')
        elif (value[0].getDatatype() == int and value[2].getDatatype() == double):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'+')
        elif (value[0].getDatatype() == double and
            value[2].getDatatype() == double):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'+')
            self.localsymboltable.addSymbol(t.getEntry())
            self.lst.append(obj)
            return t
    @_(' expr "-" expr ')
    def expr(self,value):
        if (value[0].getDatatype() == int and value[2].getDatatype() == int):
            t = NewTemp(int)
            obj = Quadruple(value.expr0,value.expr1,t,'-')
        elif (value[0].getDatatype() == double and
            value[2].getDatatype() == int):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'-')
        elif (value[0].getDatatype() == int and value[2].getDatatype()== double):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'-')
        elif (value[0].getDatatype() == double and value[2].getDatatype() == double):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'-')
            self.localsymboltable.addSymbol(t.getEntry())
            self.lst.append(obj)
            return t
    @_(' expr "*" expr ')
    def expr(self,value):
        if (value[0].getDatatype() == int and value[2].getDatatype() ==int):
            t = NewTemp(int)
            obj = Quadruple(value.expr0,value.expr1,t,'*')
        elif (value[0].getDatatype() == double and
            value[2].getDatatype() == int):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'*')
        elif (value[0].getDatatype() == int and value[2].getDatatype()== double):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'*')
        elif (value[0].getDatatype() == double and
            value[2].getDatatype() == double):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'*')
            self.localsymboltable.addSymbol(t.getEntry())
            self.lst.append(obj)
            return t
    @_(' expr "/" expr ')
    def expr(self,value):
        if (value[0].getDatatype() == int and value[2].getDatatype() ==int):
            t = NewTemp(int)
            obj = Quadruple(value.expr0,value.expr1,t,'/')
        elif (value[0].getDatatype() == double and
            value[2].getDatatype() == int):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'/')
        elif (value[0].getDatatype() == int and value[2].getDatatype()== double):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'/')
        elif (value[0].getDatatype() == double and
            value[2].getDatatype() == double):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'/')
            self.localsymboltable.addSymbol(t.getEntry())
            self.lst.append(obj)
            return t
    @_(' expr "%" expr ')
    def expr(self,value):
        if (value[0].getDatatype() == int and value[2].getDatatype() ==int):
            t = NewTemp(int)
            obj = Quadruple(value.expr0,value.expr1,t,'%')
        elif (value[0].getDatatype() == double and
            value[2].getDatatype() == int):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'%')
        elif (value[0].getDatatype() == int and value[2].getDatatype()== double):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'%')
        elif (value[0].getDatatype() == double and
            value[2].getDatatype() == double):
            t = NewTemp(double)
            obj = Quadruple(value.expr0,value.expr1,t,'%')
            self.localsymboltable.addSymbol(t.getEntry())
            self.lst.append(obj)
            return t
    @_(' expr "<" expr ')
    def expr(self,value):
        pass
    @_(' expr ">" expr ')
    def expr(self,value):
        pass
    @_(' expr GREATERTHANEQUALS expr ')
    def expr(self,value):
        pass
    @_(' expr LESSTHANEQUALS expr ')
    def expr(self,value):
        pass
    @_(' expr EQUALS expr ')
    def expr(self,value):
        pass
    @_(' expr NOTEQUALS expr ')
    def expr(self,value):
        pass
    @_(' expr LOGAND expr ')
    def expr(self,value):
        pass
    @_(' expr LOGOR expr ')
    def expr(self,value):
        pass
    @_(' "+" expr')
    def expr(self,value):
        pass
    @_(' "-" expr ')
    def expr(self,value):
        pass
    @_(' "(" type ")" expr ')
    def expr(self,value):
        pass
    @_(' "!" expr ')
    def expr(self,value):
        pass
    @_(' "(" expr ")"')
    def expr(self,value):
        pass
    @_('ID')
    def expr(self,value):
        obj = Variable(self.localsymboltable.getSymbolInTable(value.ID))
        return obj
    @_('INTCONST','DOUBLECONST')
    def expr(self,value):
        obj = Constant(value[0])
        return obj
    @_(' ID "=" expr')
    def ass_st(self,value):
        e = Variable(self.localsymboltable.getSymbolInTable(value.ID))
        obj = Quadruple(value.expr,None,e,'=')
        return obj
    @_(' PRINT ID ')
    def print_st(self,value):
        pass