import sys
opcode = {"add": ["10000", "a"],
          "sub": ["10001", "a"],
          "movi": ["10010", "b"],
          "mov": ["10011", "c"],
          "ld": ["10100", "d"],
          "st": ["10101", "d"],
          "mul": ["10110", "a"],
          "div": ["10111", "c"],
          "rs": ["11000", "b"],
          "ls": ["11001", "b"],
          "xor": ["11010", "a"],
          "or": ["11011", "a"],
          "and": ["11100", "a"],
          "not": ["11101", "c"],
          "cmp": ["11110", "c"],
          "jmp": ["11111", "e"],
          "jlt": ["01100", "e"],
          "jgt": ["01101", "e"],
          "je": ["01111", "e"],
          "hlt": ["01010", "f"],
          "addf": ["00000", "a"],
          "subf": ["00001", "a"],
          "movf": ["00010", "b"]
          }
register_dict = {'R0': '000',
                 'R1': '001',
                 'R2': '010',
                 'R3': '011',
                 'R4': '100',
                 'R5': '101',
                 'R6': '110',
                 'FLAGS': '111'}

def typea(list_instr):
    if len(list_instr)!=4:
        output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: missing arguments"+"\n")
        return 1
    if list_instr[1] not in register_dict or list_instr[2] not in register_dict or list_instr[3] not in register_dict:
        output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: wrong arguments given"+"\n")
        return 1
    if list_instr[1] == 'FLAGS' or list_instr[2] == 'FLAGS' or list_instr[3] == 'FLAGS':
        output.write(f'Line {str(all_line.index(list_instr)+1)} ERROR: {list_instr[0]} can\'t be used with FLAGS register')
        return 1
    output.write(opcode[list_instr[0]][0] + "00" + register_dict[list_instr[1]] + register_dict[list_instr[2]] + register_dict[
        list_instr[3]]+"\n")


def typeb(opcode, register_dict, list_instr):
    if list_instr[1] == 'FLAGS':
        output.write(f'Line {str(all_line.index(list_instr)+1)} ERROR: {list_instr[0]} can\'t be used with FLAGS register')
        return 1
    if float(list_instr[2][1:])<0:
        output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: negative numbers are not allowed")
        return 1

    if random[i][0] == "movf":
        op = "00010"
        float_num = float(list_instr[2][1:])
        int_val = int(float_num)
        deci_val = float_num - int_val
        # print(deci_val)
        deci_len = len(str(deci_val)) - 2
        # print(deci_len)
        deci_val = int(deci_val * (10**deci_len))
        # print(deci_val)
        b_int_val = bin(int_val)[2:]
        b_deci_val = bin(deci_val)[2:]

        if len(b_int_val)>3 or len(b_deci_val)>5:      # max floating is with mantissa 11111 and exp 111 i.e. 1.11111(in binary) * 2**7 = 252
            output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: number cannot be represented in 8 bits(3 bit exponential and 5 bit mantissa)")
            return 1

        if len(b_int_val)<3:
            b_int_val = (3-len(b_int_val)) * "0" + b_int_val

        if len(b_deci_val)<5:
            b_deci_val = b_deci_val + (5-len(b_deci_val)) * "0"

        b = b_int_val + b_deci_val
        
    else:
        if type(eval(list_instr[2][1:])) != int:
            output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: floating numbers not allowed")
            return 1

        if random[i][0] == "mov":
            op = "10010"
        else:
            for keys in opcode.keys():
                if str(list_instr[0]).lower() == str(keys).lower():
                    op = opcode[keys][0]

        b = str(bin(int(list_instr[2][1:])))[2:]
        if len(b)>8:
            output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: Value exceeding the upper limit"+"\n")
            return 1
        else:
            while len(b) != 8:
                b = '0' + b

    for reg in register_dict.keys():
        if str(list_instr[1]).lower() == str(reg).lower():
            r = register_dict[reg]
    
    
    mc = op + r + b
    output.write(mc + "\n")


def typeC(opcode, register_dict, list_instr):
    if (list_instr[1] == 'FLAGS' or list_instr[2]=='FLAGS') and list_instr[0]!='mov' or (list_instr[0]=='mov' and list_instr[1]=='FLAGS'):
        output.write(f'Line {str(all_line.index(list_instr)+1)} ERROR: {list_instr[0]} can\'t be used with FLAGS register\n')
        return 1
    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]

    for reg in register_dict.keys():
        if str(list_instr[1]).lower() == str(reg).lower():
            r1 = register_dict[reg]

    for reg in register_dict.keys():
        if str(list_instr[2]).lower() == str(reg).lower():
            r2 = register_dict[reg]

    mc = op + '00000' + r1 + r2
    output.write(mc + "\n")


def typed(opcode, register_dict, list_instr):
    if list_instr[1] == 'FLAGS' or list_instr[2] == 'FLAGS':
        output.write(f'Line {str(all_line.index(list_instr)+1)} ERROR: {list_instr[0]} can\'t be used with FLAGS register')
        return 1
    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]

    for reg in register_dict.keys():
        if str(list_instr[1]).lower() == str(reg).lower():
            r = register_dict[reg]
    mem_add = str(bin(var.index(list_instr[2]) + count))[2:]
    # print(mem_add)
    while len(mem_add) != 8:
        mem_add = "0" + mem_add
    ans = op + r + mem_add
    output.write(ans + "\n")


def typee(opcode, register_dict, list_instr):
    if list_instr[1] == 'FLAGS':
        output.write(f'Line {str(all_line.index(list_instr)+1)} ERROR: {list_instr[0]} can\'t be used with FLAGS register')
        return 1
    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]
    for keys in labels.keys():
        if str(list_instr[1]) == str(keys).lower():
            mem = (labels[keys])
    mem = str(bin(mem))[2:]
    # print(bin(mem))
    while len(mem)<8:
        mem = "0"+mem

    ans = op + "000"+mem
    output.write(ans + "\n")

random = []
#file = sys.stdin
#output = sys.stdout
file = open("tezt.txt", "r")
output = open("answer.txt", "w")
count = 0
var_count = 0
var = []
ans = 0
labels = {}
all_line = []
t_l=0
var_error=0
line_num = 0
error = False
for line in file:
    list_instr = []
    for i in line.split():
        list_instr.append(i)
    all_line.append(list_instr)
    # print(list_instr)
    if list_instr != []:
        line_num+=1
        # if var_count+2-line_num==1:
        if list_instr[0] == 'var':
            if line_num-var_error==1:
                if list_instr[1] not in opcode.keys() and list_instr[1] not in register_dict.keys():
                    var.append(list_instr[1])
                    var_count += 1
                    var_error = line_num
                else:
                    ans = "Line"+str(all_line.index(list_instr)+1)+": ERROR: variable using in-built names"
                    output.write(ans+"\n")
                    error = True
            else:
                output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: variable defined late")
                error = True
                break
        # # elif var_count+2-line_num>=1:
        # #     output.write("error:var not declared on top"+"\n")
        #     error = True
        #     break
        elif list_instr[0][-1]!=":":
            count += 1
            random.append(list_instr)
        if list_instr[0][-1:] == ":":
            labels[list_instr[0][0:-1]] = count - 1
            random.append(list_instr[1:])
            count+=1
# print(all_line)
if error==False:
    for i in range(count):
        if error == False:
            if random[i][0] == "hlt" and i!=count-1:
                output.write("Line"+str(all_line.index(random[i])+1)+": ERROR: program closed before end"+"\n")
                break
            elif random[i][0] not in opcode.keys():
                output.write("Line"+str(all_line.index(random[i])+1)+": ERROR: wrong syntax!!")
                break
            # elif random[i][1] not in register_dict.keys() and opcode[random[i][0]][1]!="e" and opcode[random[i][0]][1]!="f" and i!=count-1:
            #     print("error: unavilable reg called!!")
            elif opcode[random[i][0]][1] == "a":
                ans = typea(random[i])
                if ans == 1:
                    break
            elif len(random[i])==3 and random[i][2][0:1] == "$":
                ans = typeb(opcode, register_dict, random[i])
                if ans ==1:
                    break
            elif opcode[random[i][0]][1] == "c":
                ans = typeC(opcode, register_dict, random[i])
                if ans == 1:
                    break
            elif opcode[random[i][0]][1] == "d":
                if random[i][2] in var:
                    ans = typed(opcode, register_dict, random[i])
                    if ans == 1:
                        break
                else:
                    ans = "Line"+str(all_line.index(random[i])+1)+": ERROR: variable not defined"
                    output.write(ans)
                    break
            elif opcode[random[i][0]][1] == "e":
                if random[i][1] in labels:
                    ans = typee(opcode,register_dict,random[i])
                    if ans ==1:
                        break
                else:
                    output.write("Line"+str(all_line.index(random[i])+1)+": ERROR: label not defined")
                    break
            elif random[i][0]=="hlt" and i==count-1:
                output.write("0101000000000000")
    if random[-1][0]!="hlt" and i==count-1:
        output.write("Line"+str(all_line.index(random[i])+1)+" ERROR: Program end command missing"+"\n")
    # output.close()
