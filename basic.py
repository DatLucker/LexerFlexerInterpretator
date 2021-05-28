from Lexer import lex
from Parser import CheckSyntax, Parser
from Stack_Machine import StackMachine
import sys
string = input('>>> ')
while string != 'exit':
    try:
        tokens = lex(string)
        print(tokens)
        pars = CheckSyntax(tokens)
        lng = pars.lng()
        print(lng)
        for char in lng.rpn:
            print(char[0],end = '\t')
        print()
        for i in range(len(lng.rpn)):
            print(i,end = '\t')
        print()
    except:
        print('Syntax error')
    try:
        machine = StackMachine(lng.rpn)
        machine.run()
        for var in machine.variables.items():
            print(var)
    except BaseException:
        pass
    string = input('>>> ')
sys.exit(0)

