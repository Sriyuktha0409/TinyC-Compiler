from enum import Enum
from abc import ABCMeta, abstractmethod
DataType = Enum('DataType',['INT','DOUBLE'])
class AST(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass
    def typeCheckAST(self):
        pass
    def getDataType(self):
        pass
class NumberAst(AST):
    def __init__(self, number):
        self.value = number
    def getNumber(self):
        return self.value
    def print(self):
        print(f'Number : {self.value}', end = '')
    def getDataType(self):
        if (type(self.value) is int):
            return DataType.INT.name
        if (type(self.value) is float):
            return DataType.DOUBLE.name
class NameAst(AST):
    def __init__(self, symbolEntry):
        self.symbolEntry = symbolEntry
    def getSymbolEntry(self):
        return self.symbolEntry
    def print(self):
        print(f"NameAst : {self.symbolEntry.getSymbolName()}",end = "")
    def getDataType(self):
        return self.symbolEntry.getDataType()
class AssignAst(AST):
    def __init__(self,left,right,lineNo):
        self.left = left
        self.right = right
        self.lineNo = lineNo
    def getDataType(self):
        if(self.left.getDataType() == self.right.getDataType()):
            return self.left.getDataType()
    def typeCheckAST(self):
        if(self.left.getDataType() == self.right.getDataType()):
            return True
        else:
            return False
    def print(self):
        print("\t\tAssign Ast:\n\t\t\tLHS (",end = "")
        self.left.print()
        print(')\n\t\t\tRHS (',end = "")
        self.right.print()
        print(")")
class PrintAst(AST):
    def __init__(self,right):
        self.right= right
    def print(self):
        print("\t\tPrintAst: ")
        print("\t\t\t(", end = "")
        self.right.print()
        print(')')
