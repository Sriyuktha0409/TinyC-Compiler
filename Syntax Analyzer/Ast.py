from enum import Enum
from abc import *
from SymbolTable import SymbolTable
from SymbolTable import SymbolTableEntry
DataType = Enum('DataType',['INT','DOUBLE'])
class AST(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass
    @abstractmethod
    def typeCheckAST(self):
        pass
    @abstractmethod
    def getDataType(self):
        Pass
class NumberAst(AST):
    def __init__(self, number):
        self.value=number
    def print(self,output):
        if output is not None:
            output.write(f"Num:{self.value}")
    def getDataType(self):
        return type(self.value)
    def typeCheckAST(self):
        Pass
class NameAst(AST):
    def __init__(self, symbolEntry):
        self.symbolEntry = symbolEntry
    def print(self,output):
        self.output=output
        if output is not None:
            output.write(f"Name:{self.symbolEntry}")
    def getDataType(self):
        return SymbolTable.getSymbolEntry(self.symbolEntry).getDataType()
    def typeCheckAST(self):
        pass
class AssignAst(AST):
    def __init__(self,left,right,lineNo):
        self.left = left
        self.right = right
        self.lineNo = lineNo
    def getDataType(self):
        pass
    def typeCheckAST(self):
        if(self.left.getDataType()== self.right.getDataType()):
            return True
        else:
            return False
    def print(self,output):
        output.write("\t\tAssign:\n")
        output.write("\t\t\tLHS: (")
        self.left.print(output)
        output.write(")\n")
        output.write("\t\t\tRHS: (")
        self.right.print(output)
        output.write(")\n")
class PrintAst(AST):
    def __init__(self,symbolEntry):
        self.symbolEntry= symbolEntry
    def print(self,output):
        output.write("\t\tPrint: \n")
        output.write(f"\t\t\t")
        self.symbolEntry.print(output)
        output.write("\n")
    def getDataType(self):
        pass
    def typeCheckAST(self):
        pass