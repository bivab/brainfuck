import bytecodes

import sys
class Interpreter(object):
    def __init__(self, bytecode):
        super(Interpreter, self).__init__()
        self.bytecode = bytecode
    
    def decode(self, bytecode):
        return ord(bytecode)
        
    def run(self):
        pc = 0
        memory = {0:0}
        dp = 0
        while(pc < len(self.bytecode)):
            inst = self.decode(self.bytecode[pc])
            pc += 1
            if inst == bytecodes.BF_INCR_DP:
                dp += 1
            elif inst == bytecodes.BF_DCR_DP:
                dp -= 1
            elif inst == bytecodes.BF_INCR_D:
                if dp not in memory:
                    memory[dp] = 0
                memory[dp] += 1
            elif inst == bytecodes.BF_DCR_D:
                if dp not in memory:
                    memory[dp] = 0
                memory[dp] -= 1
            elif inst == bytecodes.BF_ECHO:
                if dp not in memory:
                    memory[dp] = 0
                print chr(memory[dp])
            elif inst == bytecodes.BF_READ:
                # TODO: read
                inp = sys.stdin.read(1)
                memory[dp] = ord(inp)
            elif inst == bytecodes.BF_JUMP_IF_ZERO:
                if dp not in memory:
                    memory[dp] = 0
                if memory[dp] == 0:
                    arg = self.decode(self.bytecode[pc])
                    pc = arg
                else:
                    # skip argument
                    pc += 1
            elif inst == bytecodes.BF_JUMP_UNLESS_ZERO:
                if dp not in memory:
                    memory[dp] = 0
                if memory[dp] != 0:
                    arg = self.decode(self.bytecode[pc])
                    pc = arg
                else:
                    pc += 1
        print memory