from Brainfuck.bfparser import Parser
from Brainfuck.bfcompiler import Compiler
from Brainfuck import bytecodes
def test_bytecodes():
    ast = parse('>')
    c = Compiler(ast)
    b = c.compile()
    assert b == [chr(bytecodes.BF_INCR_DP)]

def test_bytecodes2():
    ast = parse('<')
    c = Compiler(ast)
    b = c.compile()
    assert b == [chr(bytecodes.BF_DCR_DP)]

def test_bytecodes3():    
    ast = parse('+')
    c = Compiler(ast)
    b = c.compile()
    assert b == [chr(bytecodes.BF_INCR_D)]

def test_bytecodes4():
    ast = parse('-')
    c = Compiler(ast)
    b = c.compile()
    assert b == [chr(bytecodes.BF_DCR_D)]
    
def test_bytecodes5():
    ast = parse('.')
    c = Compiler(ast)
    b = c.compile()
    assert b == [chr(bytecodes.BF_ECHO)]
    
def test_bytecodes6():
    ast = parse(',')
    c = Compiler(ast)
    b = c.compile()
    assert b == [chr(bytecodes.BF_READ)]

def test_compile_loop():
    ast = parse('[-]')
    c = Compiler(ast)
    b = c.compile()
    exp = [chr(bytecodes.BF_JUMP_IF_ZERO)] + c.encode4(11) + [chr(bytecodes.BF_DCR_D)] + [chr(bytecodes.BF_JUMP_UNLESS_ZERO)] + c.encode4(5)
    assert b == exp

def test_nested_loop():
    ast = parse(',[<[-]>].')
    c = Compiler(ast)
    b = c.compile()
    exp = [chr(bytecodes.BF_READ), chr(bytecodes.BF_JUMP_IF_ZERO)] + c.encode4(24) + [chr(bytecodes.BF_DCR_DP), chr(bytecodes.BF_JUMP_IF_ZERO)] +  c.encode4(18) + [chr(bytecodes.BF_DCR_D), chr(bytecodes.BF_JUMP_UNLESS_ZERO)] + c.encode4(12) + [chr(bytecodes.BF_INCR_DP), chr(bytecodes.BF_JUMP_UNLESS_ZERO)] + c.encode4(6) + [chr(bytecodes.BF_ECHO)]
    print b
    print exp
    assert len(b) == len(exp)
    assert b == exp

def parse(string):
    p = Parser(string)
    p.parse()
    return p.ast