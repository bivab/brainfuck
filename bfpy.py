import os
from pypy.rlib.streamio import open_file_as_stream

from bfparser import Parser
from bfcompiler import Compiler
from bfinterpreter import Interpreter
from bfdecompiler import Decompiler

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

def entry_point(args):
    if len(args) == 1:
        print "Missing input"
        return 1
    else:
        inp = args[1]
        if os.path.exists(inp):
            f = open_file_as_stream(args[1])
            code = f.readall()
            f.close()
        else:
            code = inp
        if len(args) >= 3 and args[2] == "-debug":
            debug = True
        else:
            debug = False

        run(code, debug)
        return 0
    
def target(driver, args):
    return entry_point, None