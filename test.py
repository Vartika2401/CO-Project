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



register_dict = {'R0':'000' ,
                 'R1':'001' , 
                 'R2':'010' , 
                 'R3':'011' , 
                 'R4':'100' , 
                 'R5':'101' , 
                 'R6':'110' , 
                 'FLAGS':'111'}


instruction='mov R2 $100'

list_ins=instruction.split()
    
def typeb(opcode,register_dict,instruction):
    list_instr=instruction.split()
    for keys in opcode.keys():
        if str(list_instr[0]).lower()==str(keys).lower():
            op=opcode[keys][0]
            if list_instr[0]=='mov':
                #print(str(list_instr[2])[:1])
                if str(list_instr[2])[:1]=='$':
                    op=opcode['movi'][0]
                else:
                    op=opcode['mov'][0]

    for reg in register_dict.keys():
        if str(list_instr[1]).lower()==str(reg).lower():
            r=register_dict[reg]
    b=str(bin(int(list_instr[2][1:])))[2:]
    while len(b)!=8:
        b='0'+b
    #print(op)
    #print(r)
    #print(b)
    mc=op+r+b
    print(mc)


typeb(opcode,register_dict,instruction)
