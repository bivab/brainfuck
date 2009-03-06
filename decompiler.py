import bytecodes
   
class Decompiler(object):
    def __init__(self, bytecode):
        self.bytecode = bytecode
        
    def decode(self, bytecode):
        return ord(bytecode)
        
    def read4(self, code, pc):
        highval = ord(code[pc+3])
        # if highval >= 128:
        #             highval -= 256
        return (ord(code[pc]) |
                (ord(code[pc+1]) << 8) |
                (ord(code[pc+2]) << 16) |
                (highval << 24))
    def decompile(self):
        i = 0
        while(i < len(self.bytecode)):
            if self.decode(self.bytecode[i]) == bytecodes.BF_INCR_DP:
                print "[%d] BF_INCR_DP" % i
            if self.decode(self.bytecode[i]) == bytecodes.BF_DCR_DP:
                print "[%d] BF_DCR_DP" % i
            if self.decode(self.bytecode[i]) == bytecodes.BF_INCR_D:
                print "[%d] BF_INCR_D" % i
            if self.decode(self.bytecode[i]) == bytecodes.BF_DCR_D:
                print "[%d] BF_DCR_D" % i
            if self.decode(self.bytecode[i]) == bytecodes.BF_ECHO:
                print "[%d] BF_ECHO" % i
            if self.decode(self.bytecode[i]) == bytecodes.BF_READ:
                print "[%d] BF_READ"  % i
            if self.decode(self.bytecode[i]) == bytecodes.BF_JUMP_IF_ZERO:
                target = self.read4(self.bytecode, i+1)
                print "[%d] BF_JUMP_IF_ZERO %d" % (i, target)
                i+=4
            if self.decode(self.bytecode[i]) == bytecodes.BF_JUMP_UNLESS_ZERO:
                target = self.read4(self.bytecode, i+1)
                print "[%d] BF_JUMP_UNLESS_ZERO %d" % (i, target)
                i+=4
                
            i+=1