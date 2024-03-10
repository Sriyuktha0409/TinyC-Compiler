class Program:
    def __init__(self):
        self.functions = {}
    def addFunctionDetails(self,name, function):
        self.functions[name] = function
    def print(self,val):
        val.write("Program :\n")
        for name in self.functions:
            self.functions[name].print(val)
    def getMainFunction(self):
        for funname, function in self.functions.items():
            if(funname == 'main'):
                return function