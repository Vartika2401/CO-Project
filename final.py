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
          "hlt": ["01010", "f"]

          }
register_dict = {'R0': '000',
                 'R1': '001',
                 'R2': '010',
                 'R3': '011',
                 'R4': '100',
                 'R5': '101',
                 'R6': '110',
                 'FLAGS': '111'}


def a(list_instr):
    if list_instr[1] == 'FLAGS' or list_instr[2] == 'FLAGS' or list_instr[3] == 'FLAGS':
        print(f'ERROR, {list_instr[0]} cannot be used with FLAGS register')
        return
    output.write(opcode[list_instr[0]][0] + "00" + register_dict[list_instr[1]] + register_dict[list_instr[2]] + register_dict[
        list_instr[3]]+"\n")


def typeb(opcode, register_dict, list_instr):
    if list_instr[1] == 'FLAGS':
        output.write(f'ERROR, {list_instr[0]} cannot be used with FLAGS register')
        return

    if random[i][0] != "mov":
        for keys in opcode.keys():
            if str(list_instr[0]).lower() == str(keys).lower():
                op = opcode[keys][0]
    else:
        op = "10010"
    for reg in register_dict.keys():
        if str(list_instr[1]).lower() == str(reg).lower():
            r = register_dict[reg]
    b = str(bin(int(list_instr[2][1:])))[2:]
    if len(b)>8:
        output.write("error: Value exceeding the upper limit"+"\n")
    else:
        while len(b) != 8:
            b = '0' + b
        mc = op + r + b
        output.write(mc + "\n")


def typeC(opcode, register_dict, list_instr):
    if list_instr[1] == 'FLAGS':
        print(f'ERROR')
        return
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
        print(f'ERROR, {list_instr[0]} cannot be used with FLAGS register')
        return
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
        print(f'ERROR, {list_instr[0]} cannot be used with FLAGS register')
        return
    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]
    ans = op + "00000000000"
    output.write(ans + "\n")


random = []
file = open("tezt.txt", "r")
output = open("answer.txt", "a")
count = 0
var_count = 0
var = []
ans = 0
labels = {}
var_error=0
line_num = 0
error = False
for line in file:
    list_instr = []
    for i in line.split():
        list_instr.append(i)
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
                    ans = "error: variable using in-built names"
                    output.write(ans+"\n")
                    error = True
            else:
                output.write("error: var defined late")
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

# print(random)
if error==False:
    for i in range(count):
        if random[i][0] == "hlt" and i!=count-1:
            output.write("error: program closed before end"+"\n")
            break
        elif random[i][0] not in opcode.keys():
            print("error: wrong syntax!!")
        # elif random[i][1] not in register_dict.keys() and opcode[random[i][0]][1]!="e" and opcode[random[i][0]][1]!="f" and i!=count-1:
        #     print("error: unavilable reg called!!")
        elif opcode[random[i][0]][1] == "a":
            a(random[i])
        elif len(random[i])==3 and random[i][2][0:1] == "$":
            typeb(opcode, register_dict, random[i])
        elif opcode[random[i][0]][1] == "c":
            typeC(opcode, register_dict, random[i])
        elif opcode[random[i][0]][1] == "d":
            if random[i][2] in var:
                typed(opcode, register_dict, random[i])
            else:
                ans = "error: var not defined"
                output.write(ans)
                break
        elif opcode[random[i][0]][1] == "e":
            if random[i][1] in labels:
                typee(opcode,register_dict,random[i])
            else:
                output.write("Error: label not defined")
                break
        elif random[i][0]=="hlt" and i==count-1:
            output.write("0101000000000000")
    if random[-1][0]!="hlt" and i==count-1:
        output.write("Line:"+str(count+1)+" Program end command missing"+"\n")
    # output.close()
