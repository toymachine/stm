import _stm

_stm.test()

import opcode

from stm import persistent, world


class Member(persistent):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def sum(self):
        return self.a + self.b


m = Member(10, 20)

def sum(a, b):
    c = a + b

def run(code_object):
    code = code_object.co_code
    n = len(code)
    i = 0
    e = 0
    while i < n:
        i_offset = i
        i_opcode = ord(code[i])
        i = i + 1
        if i_opcode >= opcode.HAVE_ARGUMENT:
            i_argument = ord(code[i]) + (ord(code[i+1]) << 8) + e
            i = i +2
            if i_opcode == opcode.EXTENDED_ARG:
                e = iarg << 16
            else:
                e = 0
            if i_opcode in opcode.hasconst:
                i_arg_value = repr(code_object.co_consts[i_argument])
                i_arg_type = 'CONSTANT'
            elif i_opcode in opcode.hasname:
                i_arg_value = code_object.co_names[i_argument]
                i_arg_type = 'GLOBAL VARIABLE'
            elif i_opcode in opcode.hasjrel:
                i_arg_value = repr(i + i_argument)
                i_arg_type = 'RELATIVE JUMP'
            elif i_opcode in opcode.haslocal:
                i_arg_value = code_object.co_varnames[i_argument]
                i_arg_type = 'LOCAL VARIABLE'
            elif i_opcode in opcode.hascompare:
                i_arg_value = opcode.cmp_op[i_argument]
                i_arg_type = 'COMPARE OPERATOR'
            elif i_opcode in opcode.hasfree:
                i_arg_value = variables[i_argument]
                i_arg_type = 'FREE VARIABLE'
            else:
                i_arg_value = i_argument
                i_arg_type = 'OTHER'
        else:
            i_argument = None
            i_arg_value = None
            i_arg_type = None

        print (i_offset, i_opcode, opcode.opname[i_opcode], i_argument, i_arg_type, i_arg_value)


#run(sum.func_code)


