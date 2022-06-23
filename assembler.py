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
opcode = {"add":["10000","a"],
        "sub":["10001","a"],
        "movi":["10010","b"],
        "mov":["10011","c"],
        "ld":["10100","d"],
        "st":["10101","d"],
        "mul":["10110","a"],
        "div":["10111","c"],
        "rs":["11000","b"],
        "ls":["11001","b"],
        "xor":["11010","a"],
        "or":["11011","a"],
        "and":["11100","a"],
        "not":["11101","c"],
        "cmp":["11110","c"],
        "jmp":["11111","e"],
        "jlt":["01100","e"],
        "jgt":["01101","e"],
        "je":["01111","e"],
        "hlt":["01010","f"]

        }
register_dict = {'reg0':'000' ,
                 'reg1':'001' , 
                 'reg2':'010' , 
                 'reg3':'011' , 
                 'reg4':'100' , 
                 'reg5':'101' , 
                 'reg6':'110' , 
                 'FLAGS':'111'}
# def a():


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

