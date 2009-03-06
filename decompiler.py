import bytecodes
   
class Decompiler(object):
    def __init__(self, bytecode):
        self.bytecode = bytecode
        
    def decode(self, bytecode):
        return ord(bytecode)
        
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
                target = self.decode(self.bytecode[i+1])
                print "[%d] BF_JUMP_IF_ZERO %d" % (i, target)
                i+=1
            if self.decode(self.bytecode[i]) == bytecodes.BF_JUMP_UNLESS_ZERO:
                target = self.decode(self.bytecode[i+1])
                print "[%d] BF_JUMP_UNLESS_ZERO %d" % (i, target)
                i+=1
                
            i+=1