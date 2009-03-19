import bytecodes
class Compiler(object):
    def __init__(self, ast):
        self.ast = ast
        self.pc = 0
        
    def emit(self, acc, bytecode, arg=None):
        acc.append(chr(bytecode))
        if arg is not None:
            if isinstance(arg, list):
                acc += arg
            else:
                print "Error got somenthing that is not a list"
            #   acc.append(chr(arg))
            
    def encode4(self, value):
        return [chr(value & 0xFF),
                chr((value >> 8) & 0xFF),
                chr((value >> 16) & 0xFF),
                chr((value >> 24) & 0xFF)]
                
    def compile_Loop(self, bytecode, ast, pos):
        self.pc += 5
        start = self.pc
        res = self._compile(ast)
        end = start + len(res) + 5
        self.emit(bytecode, bytecodes.BF_JUMP_IF_ZERO, self.encode4(end))
        bytecode += res
        self.emit(bytecode, bytecodes.BF_JUMP_UNLESS_ZERO, self.encode4(start))
        
    def compile(self):
        return self._compile(self.ast)
        
    def _compile(self, ast):
        pos = 0
        bytecode = []
        while(pos < len(ast.children)):
            inst = ast.children[pos]
            if inst.value == '>':
                self.emit(bytecode, bytecodes.BF_INCR_DP)
            elif inst.value == '<':
                self.emit(bytecode, bytecodes.BF_DCR_DP)
            elif inst.value == '+':
                self.emit(bytecode, bytecodes.BF_INCR_D)
            elif inst.value == '-':
                self.emit(bytecode, bytecodes.BF_DCR_D)
            elif inst.value == '.':
                self.emit(bytecode, bytecodes.BF_ECHO)
            elif inst.value == ',':
                self.emit(bytecode, bytecodes.BF_READ)
            elif inst.value is None and len(inst.children) > 0:
                self.compile_Loop(bytecode, inst, pos)
            pos += 1
            self.pc += 1
        return bytecode