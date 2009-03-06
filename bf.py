from parser import Parser
from compiler import Compiler
from decompiler import Decompiler
from interpreter import Interpreter
        
def run(code):
    p = Parser(code)
    p.parse()
    c = Compiler(p.ast)
    b = c.compile()
    d = Decompiler(b)
    d.decompile()
    i = Interpreter(b)
    i.run()
    print 
    
if __name__ == '__main__':
    
    run("[-]")
    run("[[-]<]")
    run("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.")