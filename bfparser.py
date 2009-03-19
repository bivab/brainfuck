class AstNode(object):
    def __init__(self, value = None):
        self.value = value
        self.children = []

    def __repr__(self):
        s = ''
        if len(self.children) > 0:
            s = repr(self.children)
        if self.value is not None:
            s = self.value + s
        return s
    
    def __eq__(self, other):
        return (self.__class__ is other.__class__ and 
                self.__dict__ == other.__dict__)
        
    def __ne__(self, other):
        return not self == other
    
class Parser(object):
    def __init__(self, code):
        self.code = code
        self.ast  = AstNode()
        self.nest = 0
        
    def parseLoop(self):
        self.nest -= 1
        t = []
        c = self.ast.children.pop()
        while(c.value != '['):
            t.insert(0, c)
            c = self.ast.children.pop()
        self.ast.children = t
        
    def parse(self):
        self.pos = 0
        self._parse(self.ast)
    def _parse(self, node):
        while(self.pos < len(self.code)):
            inst = self.code[self.pos]
            if inst == '>':
                node.children.append(AstNode('>'))
            elif inst == '<':
                node.children.append(AstNode('<'))
            elif inst == '+':
                node.children.append(AstNode('+'))
            elif inst == '-':
                node.children.append(AstNode('-'))
            elif inst == '.':
                node.children.append(AstNode('.'))
            elif inst == ',':
                node.children.append(AstNode(','))
            elif inst == '[':
                self.pos += 1
                n = AstNode()
                self._parse(n)
                node.children.append(n)
            elif inst == ']':
                self.pos += 1
                return
            self.pos += 1
            
        assert self.nest == 0, self.nest