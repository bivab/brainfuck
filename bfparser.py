class AstNode(object):
    def __init__(self, value = None):
        self.value = value
        self.children = []
    
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
        
    def parse(self):
        self.pos = 0
        self._parse(self.ast)
        assert self.nest == 0, self.nest
    def _parse(self, node):
        nesting = self.nest
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
                self.nest += 1
                self._parse(n)
                node.children.append(n)
            elif inst == ']':
                # self.pos += 1
                self.nest -= 1
                nesting -= 1
                break
            self.pos += 1
            
        assert self.nest == nesting, (self.nest, nesting)