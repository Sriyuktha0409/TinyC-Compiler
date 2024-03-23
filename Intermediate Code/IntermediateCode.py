from SymbolTable import *
class Operand:
    pass
class Variable(Operand):
    def __init__(self,symbol_entry):
        self.symbol_entry = symbol_entry
    def getDatatype(self):
        return self.symbol_entry.getDataType()
    def print(self):
        return self.symbol_entry.getSymbolName()
class Constant(Operand):
    def __init__(self,value):
        self.value = value
    def print(self):
        return self.value
    def getDatatype(self):
        return type(self.value)
class Quadruple:
    def __init__(self,opd1,opd2,result,opcode):
        self.opd1 = opd1
        self.opd2 = opd2
        self.result = result
        self.opcode = opcode
    def getopd1(self):
        return self.opd1
    def getopd2(self):
        return self.opd2
    def getresult(self):
        return self.result
    def getopcode(self):
        return self.opcode
    def getDatatype(self):
        return self.result.getDatatype()
    def print(self):
        if self.opd2 is not None:
            print(f"\t\t{self.result.print()} = {self.opd1.print()} {self.opcode} {self.opd2.print()}")
        else:
            print(f"\t\t{self.result.print()} = {self.opd1.print()}")
class NewTemp:
    inc = 0
    def __init__(self,datatype):
        NewTemp.inc = NewTemp.inc + 1
        self.temp = f"t{self.inc}"
        self.datatype = datatype
        self.obj = SymbolTableEntry(self.temp,self.datatype)
    def print(self):
        return self.temp
    def getDatatype(self):
        return self.datatype
    def getEntry(self):
        return self.obj