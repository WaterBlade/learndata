# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:11:52 2018

@author: Administrator
"""

class Statement:
    def __init__(self):
        self.variable_dict = {}
        self.string = ''
        self.index = 0
        self.char = ''  # type: str
        
    def read(self, string):
        self.string = string
        self.index = 0
        self.move()
        
    def reachEnd(self):
        self.char = ''
        
    def move(self):
        if self.index < len(self.string):
            self.char = self.string[self.index]
            self.index += 1
        else:
            self.reachEnd()
        
    def findValue(self, var):
        return self.variable_dict[var]
    
    def processNode(self, var, value):
        self.variable_dict[var] = value
        
    def readId(self):
        id_ = ''
        
        while self.char.isspace():
            self.move()
        
        if self.char.isalpha():
            while self.char.isalnum():
                id_ += self.char
                self.move()
        else:
            raise RuntimeError('Unknown var type!')
            
        return id_
    
    def readNumber(self):
        number = ''
        
        while self.char.isdigit() or self.char == '.':
            number += self.char
            self.move()
            
        return float(number)
            
    
    def factor(self):
        minus = 1.0
        while self.char == '+' or self.char == '-':
            if self.char == '-':
                minus *= -1
            self.move()
                
        if self.char.isdigit() or self.char == '.':
            var = self.readNumber()
            
        elif self.char == '(':
            var = self.expression()
            if self.char == ')':
                self.move()
            else:
                raise RuntimeError('Right paren left out')
        else:
            id_ = self.readId()
            var = self.findValue(id_)
            
        return minus * var
    
    
    def term(self):
        f = self.factor()
        while True:
            if self.char == '*':
                f *= self.factor()
            elif self.char == '/':
                f /= self.factor()
            else:
                return f
            
    
    def expression(self):
        t = self.term()
        while True:
            if self.char == '+':
                t += self.term()
            elif self.char == '-':
                t -= self.term()
            else:
                return t
            
    
    def statement(self):
        id_ = self.readId()
        while self.char.isspace():
            self.move()
        
        self.move()
        
        while self.char.isspace():
            self.move()
            
        e = self.expression()
        
        self.processNode(id_, e)
        
    
    def status(self):
        print(self.variable_dict)
        
    def value(self, id_):
        print('%s = %f' % (id_, self.variable_dict[id_]))
            

def main():
    state = Statement()
    while True:
        print('Welcome:')
        print('[1]Enter Statement')
        print('[2]Check Status')
        print('[3]Print Variable')
        print('[q]Quit')
        c = input('choose: ')
        if c == '1':
            state.read(input('statement: '))
            state.statement()
        elif c == '2':
            state.status()
        elif c == '3':
            state.value(input('variable: '))
        elif c == 'q':
            break

            
                
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
            
    
            
        