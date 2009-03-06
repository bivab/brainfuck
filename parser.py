class Parser(object):
    def __init__(self, code):
        self.code = code
        self.ast  = []
        self.nest = 0
        
    def parseLoop(self):
        self.nest -= 1
        t = []
        c = self.ast.pop()
        while(c != '['):
            t.insert(0, c)
            c = self.ast.pop()
        self.ast.append(t)
        
    def parse(self):
        pos = 0
        while(pos < len(self.code)):
            inst = self.code[pos]
            if inst == '>':
                self.ast.append('>')
            elif inst == '<':
                self.ast.append('<')
            elif inst == '+':
                self.ast.append('+')
            elif inst == '-':
                self.ast.append('-')
            elif inst == '.':
                self.ast.append('.')
            elif inst == ',':
                self.ast.append(',')
            elif inst == '[':
                self.nest +=1
                self.ast.append('[')
            elif inst == ']':
                self.parseLoop()
            pos += 1
            
        assert self.nest == 0, self.nest