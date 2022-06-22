# from multiprocessing.sharedctypes import Value


# def Addition(reg1,reg2,reg3):
#     reg3 = reg2+reg1
# def Subtraction(reg1,reg2,reg3):
#     reg3 = reg1-reg2
# def MoveImmediate(reg1,value):
#     reg1 = value
# def MoveRegister(reg1,reg2):
#     reg2 = reg1
# def Load(reg1,mem):

# def Store()
#opcodes 
opcode = {"add":"10000",
        "sub":"10001",
        "movi":"10010",
        "mov":"10011",
        "ld":"10100",
        "st":"10101",
        "mul":"10110",
        "div":"10111",
        "rs":"11000",
        "ls":"11001",
        "xor":"11010",
        "or":"11011",
        "and":"11100",
        "not":"11101",
        "cmp":"11110",
        "jmp":"11111",
        "jlt":"01100",
        "jgt":"01101",
        "je":"01111",
        "hlt":"01010"

        }
# opcode = {"10000":Addition,
#         "10001":Subtraction,
#         "10010":MoveImmediate,
#         "10011":MoveRegister,
#         "10100":Load,
#         "10101":Store,
#         "10110":Multiply,
#         "10111":Divide,
#         "11000":RightShift,
#         "11001":LeftShift,
#         "11010":ExclusiveOR,
#         "11011":Or,
#         "11100":And,
#         "11101":Invert,
#         "11101":Compare,
#         "11111":uncond_jump,
#         "01100":ljump,
#         "01101":gjump,
#         "01111":ejump,
#         "01010":Halt
#         }

