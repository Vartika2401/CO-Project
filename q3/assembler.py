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


def typea_err(list_instr):
    if len(list_instr)!=4:
        output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: missing arguments"+"\n")
        return 1
    if list_instr[1] not in register_dict or list_instr[2] not in register_dict or list_instr[3] not in register_dict:
        output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: wrong arguments given"+"\n")
        return 1
    if list_instr[1] == 'FLAGS' or list_instr[2] == 'FLAGS' or list_instr[3] == 'FLAGS':
        output.write(f'Line {str(all_line.index(list_instr)+1)} ERROR: {list_instr[0]} can\'t be used with FLAGS register')
        return 1
    return 0

def typeb_err(list_instr):
    if list_instr[1] == 'FLAGS':
        output.write(f'Line {str(all_line.index(list_instr)+1)} ERROR: {list_instr[0]} can\'t be used with FLAGS register')
        return 1
    if float(list_instr[2][1:])<0:
        output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: negative numbers are not allowed")
        return 1

    if random[i][0] == "movf":
        num = list_instr[2][1:]
        num_l = num.split(".")
        int_binary = bin(int(num_l[0]))[2:]
        n_deci_val = len(num_l[1])

        exp = 0
        if (len(int_binary) > 1):
            exp = len(int_binary) - 1
        #print("exp : ",exp)

        now_num = int(float(num)*(2**n_deci_val))
        #print("now_num : ",now_num)
        float_binary = bin(now_num)[2:]
        #print("float_binary : ",float_binary)

        exp_b = bin(exp)[2:]
        if (len(exp_b)<3):
            exp_b = (3-len(exp_b))*'0' + exp_b
        elif (len(exp_b)>3):
            output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: number cannot be represented in 8 bits(3 bit exponential and 5 bit mantissa)")
            return 1
        #print(exp_b)

        mantissa = float_binary[len(float_binary)-exp-n_deci_val:]
        if (len(mantissa)<5):
            mantissa = mantissa + (5-len(mantissa))*'0'
        elif (len(mantissa)>5):
            output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: number cannot be represented in 8 bits(3 bit exponential and 5 bit mantissa)")
            return 1
        #print(mantissa)
    else:
        if type(eval(list_instr[2][1:])) != int:
            output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: floating numbers not allowed")
            return 1

        b = str(bin(int(list_instr[2][1:])))[2:]
        if len(b)>8:
            output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: Value exceeding the upper limit"+"\n")
            return 1
    return 0

def typeC_err(list_instr):
    if (list_instr[0] == 'FLAGS' or list_instr[2]=='FLAGS') and list_instr[0]!='mov' or (list_instr[0]=='mov' and list_instr[2]=='FLAGS'):
        output.write(f'Line {str(all_line.index(list_instr)+1)} ERROR: {list_instr[0]} can\'t be used with FLAGS register\n')
        return 1
    return 0

def typed_err(list_instr):
    if list_instr[1] == 'FLAGS' or list_instr[2] == 'FLAGS':
        output.write(f'Line {str(all_line.index(list_instr)+1)} ERROR: {list_instr[0]} can\'t be used with FLAGS register')
        return 1
    return 0

def typee_err(list_instr):
    if list_instr[1] == 'FLAGS':
        output.write(f'Line {str(all_line.index(list_instr)+1)} ERROR: {list_instr[0]} can\'t be used with FLAGS register')
        return 1
    return 0


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
        num = list_instr[2][1:]
        num_l = num.split(".")
        int_binary = bin(int(num_l[0]))[2:]
        n_deci_val = len(num_l[1])

        exp = 0
        if (len(int_binary) > 1):
            exp = len(int_binary) - 1
        #print("exp : ",exp)

        now_num = int(float(num)*(2**n_deci_val))
        #print("now_num : ",now_num)
        float_binary = bin(now_num)[2:]
        #print("float_binary : ",float_binary)

        exp_b = bin(exp)[2:]
        if (len(exp_b)<3):
            exp_b = (3-len(exp_b))*'0' + exp_b
        elif (len(exp_b)>3):
            output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: number cannot be represented in 8 bits(3 bit exponential and 5 bit mantissa)")
            return 1
        #print(exp_b)

        mantissa = float_binary[len(float_binary)-exp-n_deci_val:]
        if (len(mantissa)<5):
            mantissa = mantissa + (5-len(mantissa))*'0'
        elif (len(mantissa)>5):
            output.write("Line"+str(all_line.index(list_instr)+1)+": ERROR: number cannot be represented in 8 bits(3 bit exponential and 5 bit mantissa)")
            return 1
        #print(mantissa)

        float_arithmatic = exp_b + mantissa
        #print(float_arithmatic)
        b = float_arithmatic
        
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
    if (list_instr[0] == 'FLAGS' or list_instr[2]=='FLAGS') and list_instr[0]!='mov' or (list_instr[0]=='mov' and list_instr[2]=='FLAGS'):
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

    if r2=="111":
    	mc = op + '00000' + r2 + r1
    else:
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
# file = sys.stdin
# output = sys.stdout
file = open("tezt.txt", "r")
output = open("answer_a.txt", "w")
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
                error = True
                break
            elif random[i][0] not in opcode.keys():
                output.write("Line"+str(all_line.index(random[i])+1)+": ERROR: wrong syntax!!")
                error = True
                break
            # elif random[i][1] not in register_dict.keys() and opcode[random[i][0]][1]!="e" and opcode[random[i][0]][1]!="f" and i!=count-1:
            #     print("error: unavilable reg called!!")
            elif opcode[random[i][0]][1] == "a":
                ans = typea_err(random[i])
                if ans == 1:
                    error = True
                    break
            elif len(random[i])==3 and random[i][2][0:1] == "$":
                ans = typeb_err(random[i])
                if ans == 1:
                    error = True
                    break
            elif opcode[random[i][0]][1] == "c":
                ans = typeC_err(random[i])
                if ans == 1:
                    error = True
                    break
            elif opcode[random[i][0]][1] == "d":
                if random[i][2] in var:
                    ans = typed_err(random[i])
                    if ans == 1:
                        error = True
                        break
                else:
                    ans = "Line"+str(all_line.index(random[i])+1)+": ERROR: variable not defined"
                    output.write(ans)
                    error = True
                    break
            elif opcode[random[i][0]][1] == "e":
                if random[i][1] in labels:
                    ans = typee_err(random[i])
                    if ans == 1:
                        error = True
                        break
                else:
                    output.write("Line"+str(all_line.index(random[i])+1)+": ERROR: label not defined")
                    error = True
                    break
    if random[-1][0]!="hlt" and i==count-1:
        output.write("Line"+str(all_line.index(random[i])+1)+" ERROR: Program end command missing"+"\n")
        error = True
    # output.close()

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
