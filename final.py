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
register_dict = {'R0':'000' ,
                 'R1':'001' ,
                 'R2':'010' ,
                 'R3':'011' ,
                 'R4':'100' ,
                 'R5':'101' ,
                 'R6':'110' ,
                 'FLAGS':'111'}

def a(list_instr):
    print(opcode[list_instr[0]][0] + "00" + register_dict[list_instr[1]] + register_dict[list_instr[2]] + register_dict[list_instr[3]])


def typeb(opcode, register_dict, list_instr):
    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]

    for reg in register_dict.keys():
        if str(list_instr[1]).lower() == str(reg).lower():
            r = register_dict[reg]
    b = str(bin(int(list_instr[2][1:])))[2:]
    while len(b) != 8:
        b = '0' + b
    mc = op + r + b
    print(mc)

file = open("tezt.txt","r")
for line in file:
    list_instr = []
    for i in line.split():
        list_instr.append(i)
    if opcode[list_instr[0]][1]=="a":
        a(list_instr)
    elif list_instr[0]=="mov" and list_instr[2][:1]=="$":
        typeb(opcode,register_dict,list_instr)
    elif opcode[list_instr[0]][1]=="b":

        typeb(opcode,register_dict,list_instr)

