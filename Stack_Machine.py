from LinkedList import LinkedList

class StackMachine:
    def __init__(self, input):
        self.stck = []
        self.input = input
        self.index = -1
        self.variables = {}
        self.advance()

    def advance(self):
        if self.index < len(self.input):
            self.index += 1
            if self.index == len(self.input):
                self.current_elem = ('', None)
            else:
                self.current_elem = self.input[self.index]

    def is_defined(self,a):
        try:
            if a in self.variables.keys():
                if self.variables[a] == 'Undefined':
                    raise BaseException
        except:
            print(f'Variable {a} is not defined')
            raise BaseException

    def bin_log_op(self, Z, X, operand):
        if operand == '>':
            return X > Z
        if operand == '<':
            return X < Z
        if operand == '>=':
            return X >= Z
        if operand == '<=':
            return X <= Z
        if operand == '==':
            return X == Z
        if operand == '!=':
            return X != Z
        if operand == '&&':
            return X & Z
        if operand == '||':
            return X | Z

    def bin_op(self, Z, X, operand):
        self.is_defined(X)
        if operand == '+':
            return X + Z
        if operand == '-':
            return X - Z
        if operand == '*':
            return X * Z
        if operand == '/':
            return X / Z

    def assign_op(self, Z, X):
        try:
            self.is_defined(Z)
            self.variables[X] = Z
        except:
            raise BaseException

    def jmp(self, pos):
        if pos == len(self.input):
            self.index = pos
            return
        self.index = pos
        self.current_elem = self.input[self.index]

    def jmpf(self,pos,f):
        if not f:
            self.jmp(pos)
        else:
            self.advance()

    def run(self):
        try:
            while self.index < len(self.input):
                if self.current_elem[1] == 'INT':
                    self.stck.append(int(self.current_elem[0]))
                    self.advance()
                elif self.current_elem[1] == 'VAR':
                    if self.current_elem[0] not in self.variables:
                        self.variables[self.current_elem[0]] = 'Undefined'
                    self.stck.append(self.current_elem[0])
                    self.advance()
                elif self.current_elem[1] == 'LOGICAL_OP':
                    Z = self.stck.pop()
                    X = self.stck.pop()
                    if Z in self.variables.keys():
                        self.is_defined(Z)
                        Z = self.variables[Z]
                    if X in self.variables.keys():
                        self.is_defined(X)
                        X = self.variables[X]
                    self.stck.append(self.bin_log_op(Z, X, self.current_elem[0]))
                    self.advance()
                elif self.current_elem[1] == 'PLUS' or self.current_elem[1] == 'MINUS' or self.current_elem[1] == 'MUL' or self.current_elem[1] == 'DIV':
                    Z = self.stck.pop()
                    X = self.stck.pop()
                    if Z in self.variables.keys():
                        self.is_defined(Z)
                        Z = self.variables[Z]
                    if X in self.variables.keys():
                        self.is_defined(X)
                        X = self.variables[X]
                    self.stck.append(self.bin_op(Z, X, self.current_elem[0]))
                    self.advance()
                elif self.current_elem[1] == 'ASSIGN':
                    Z = self.stck.pop()
                    if Z in self.variables.keys():
                        self.is_defined(Z)
                        Z = self.variables[Z]
                    self.assign_op(Z, self.stck.pop())
                    self.advance()
                elif self.current_elem[0] == '!':
                    self.jmp(self.stck.pop())
                elif self.current_elem[0] == '!F':
                    pos = self.stck.pop()
                    f = self.stck.pop()
                    self.jmpf(pos, f)
                elif self.current_elem[1] in ('LINKED_LIST_KW','function_name'):
                    args = []
                    i = self.current_elem[2] # число параметров функции
                    while(i != 0):
                        args.insert(0, self.stck.pop())
                        i -= 1
                    if len(args) == 1:
                        args = args[0]
                    if self.current_elem[1] == 'LINKED_LIST_KW':
                        self.stck.append(LinkedList(args))
                        self.advance()
                    elif self.current_elem[0] == 'push':
                        self.variables[self.stck.pop()].push(args)
                        self.advance()
                    elif self.current_elem[0] == 'contains':
                        self.stck.append(self.variables[self.stck.pop()].contains(args))
                        self.advance()
                    elif self.current_elem[0] == 'get':
                        X = self.stck.pop()
                        lst = self.variables[X]
                        c = lst.get(args)
                        self.stck.append(c)
                        self.advance()
                    elif self.current_elem[0] == 'remove':
                        self.variables[self.stck.pop()].remove(args)
                        self.advance()
        except BaseException:
            raise BaseException
