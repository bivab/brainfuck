import bytecodes

import os
class Interpreter(object):
    def __init__(self, bytecode):
        #super(Interpreter, self).__init__()
        self.bytecode = bytecode

    def decode(self, bytecode):
        return ord(bytecode)

    def read4(self, code, pc):
        highval = ord(code[pc+3])
        if highval >= 128:
            highval -= 256
        return (ord(code[pc]) |
                (ord(code[pc+1]) << 8) |
                (ord(code[pc+2]) << 16) |
                (highval << 24))

    def run(self):
        pc = 0
        memory = [0 for x in xrange(300)]
        dp = 0
        while(pc < len(self.bytecode)):
            inst = self.decode(self.bytecode[pc])
            pc += 1
            if inst == bytecodes.BF_INCR_DP:
                dp += 1
            elif inst == bytecodes.BF_DCR_DP:
                dp -= 1
            elif inst == bytecodes.BF_INCR_D:

                memory[dp] += 1
            elif inst == bytecodes.BF_DCR_D:

                memory[dp] -= 1
            elif inst == bytecodes.BF_ECHO:

                if memory[dp] < 256:
                    print chr(memory[dp])
                else:
                    print memory[dp]
            elif inst == bytecodes.BF_READ:
                inp = read()
                memory[dp] = ord(inp)
            elif inst == bytecodes.BF_JUMP_IF_ZERO:

                if memory[dp] == 0:
                    arg = self.read4(self.bytecode, 4)
                    pc = arg
                else:
                    # skip argument
                    pc += 4
            elif inst == bytecodes.BF_JUMP_UNLESS_ZERO:

                if memory[dp] != 0:
                    arg = self.read4(self.bytecode, pc)
                    pc = arg
                else:
                    pc += 4
        #print memory
def read():
    result = None
    while True:
        s = os.read(0, 1)
        if result is None:
            result = s
        if s == "\n":
            break
        if s == '':
            if len(result) > 1:
                break
            raise SystemExit
    return result[0]
