import argparse
import sys
from Parser import *
from Lexer import *
from Ast import *
argparser = argparse.ArgumentParser()
par = tinycparser()
lex = tinyclexer()
argparser.usage = "tinyCC [options] file"
argparser.add_argument('-tokens',action='store_true',help="Show tokens in file.toks (or out.toks)")
argparser.add_argument('-parse',action='store_true',help="Show abstract syntax tree in file.ast (or out.ast)")
argparser.add_argument('-icode', action='store_true',help="Show 3 address code in file.icode (or out.icode)")
argparser.add_argument('-symtab',action='store_true',help="Show symbol table in file.sym (or out.sym)")
argparser.add_argument('-compile',action='store_true',help="Compile the program and generate spim code in file.spim (or out.spim)")
argparser.add_argument('file',help="TinyC Program")
args = argparser.parse_args()
f = open(args.file)
exp = f.read()
args.compile = True
if args.tokens:
    tokens_file_name = args.file +".toks"
    tokens_file = open(tokens_file_name,"w")
    for token in lex.tokenize(exp):
        tokens_file.write(f"type = {token.type} ,\t value = {token.value}\n")
if args.parse:
    parsers_file_name = args.file +".ast"
    parsers_file = open(parsers_file_name,"w")
    par.parse(lex.tokenize(exp))
    if par.program:
        par.prog.print()
    else:
        print("Program Not Accepted")
        args.ast = False
        args.compile = False
if args.icode:
    ast_file_name = args.file +".icode"
    par.parse(lex.tokenize(exp))
    originalstdout = sys.stdout
    with open(ast_file_name,'w') as sys.stdout:
        par.prog.print()
        sys.stdout = originalstdout
if args.compile:
    target_code_file_name = args.file +".spim"
    target_code_file = open(target_code_file_name,"w")
    sys.stdout = target_code_file
    originalstdout=sys.stdout
    program = par.prog
    if program:
        main_function = program.getMainFunction()
        if main_function:
            generator(par)
        else:
            print("Error: Main function not found.")
    else:
        print("Error: No program to compile.")
        sys.stdout = originalstdout
        target_code_file.close()