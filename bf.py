from bfparser import Parser
from bfcompiler import Compiler
from bfdecompiler import Decompiler
from bfinterpreter import Interpreter

import sys
import os
        
def run(code, debug=False):
    p = Parser(code)
    p.parse()
    c = Compiler(p.ast)
    b = c.compile()

    if debug:
        print p.ast
        print b
        d = Decompiler(b)
        d.decompile()

    i = Interpreter(b)
    i.run()
    print 

def main():
    if len(sys.argv) == 1:
        print "Missing input"
    else:
        inp = sys.argv[1]
        if os.path.exists(inp):
            f = open(inp, 'r')
            code = f.read()
            f.close()
        else:
            code = inp
        if len(sys.argv) >= 3 and sys.argv[2] == "-debug":
            debug = True
        else:
            debug = False

        run(code, debug)
            
if __name__ == '__main__':
    main()
