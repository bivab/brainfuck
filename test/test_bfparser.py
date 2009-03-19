#import sys
# sys.path.append('..')
# print sys.path
from Brainfuck.bfparser import Parser, AstNode
import py
def test_ast_node():
    a = AstNode('<')
    b = AstNode('>')
    c = AstNode('-')
    d = AstNode('<')
    d.children.append(AstNode('-'))
    assert a.value == '<'
    assert b.value == '>'
    assert a != b
    assert a != d
    a.children.append(c)
    a.children == [c]
    assert a == d
    
def test_parse_simple_symbols():
    for x in ['<', '>', '+', '-', '.', ',']:
        p = Parser(x)
        p.parse()
        print p.ast
        assert p.ast.children[0].value == x
        
def test_parse_unclosed_loop():
    p = Parser('[')
    py.test.raises(AssertionError, 'p.parse()')
    p = Parser('[[')
    py.test.raises(AssertionError, 'p.parse()')
    
def test_parse_unopened_loop():
    p = Parser(']')
    py.test.raises(AssertionError, 'p.parse()')
    p = Parser(']]')
    py.test.raises(AssertionError, 'p.parse()')
    
def test_parse_empty_loop():
    p = Parser('[]')
    p.parse()
    ast = p.ast
    assert len(ast.children) == 1
    loop = ast.children[0]
    assert loop.value is None

def test_non_empty_loop():
    p = Parser('[-]')
    p.parse()
    ast = p.ast
    loop = ast.children[0]
    assert loop.value is None
    assert len(loop.children) == 1
    assert loop.children[0] == AstNode('-')
    
def test_nested_loops():
    ast = parse(',[<[-]>].')
    assert len(ast.children) == 3
    
def parse(string):
    p = Parser(string)
    p.parse()
    return p.ast