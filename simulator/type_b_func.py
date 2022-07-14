register_list = ['0000000000000000','0000000000001000','0000000000000011','0000000000000000','0000000000000000','0000000000000000','0000000000000000']


def movi(machine_ins):
    global PC
    global register_list
    reg = int(machine_ins[5:8],2)
    imm = machine_ins[8:]
    register_list[reg] = "00000000"+imm

    register_list[6] = '0000000000000000'
    PC+=1


def rs(machine_ins):
    global PC
    global register_list
    reg = int(machine_ins[5:8],2)
    imm = int(machine_ins[8:],2)
    if (imm > 16):
        register_list[reg] = "0000000000000000"
    else:
        register_list[reg] = register_list[reg][imm:]
        register_list[reg] = register_list[reg] + imm*"0"
    
    register_list[6] = '0000000000000000'
    PC+=1
        

def ls(machine_ins):
    global PC
    global register_list
    reg = int(machine_ins[5:8],2)
    imm = int(machine_ins[8:],2)
    if (imm > 16):
        register_list[reg]="0000000000000000"
    else:
        register_list[reg] = register_list[reg][0:(16-imm)]
        register_list[reg] = imm*"0" + register_list[reg]
    
    register_list[6] = '0000000000000000'
    PC+=1
        

#movi("1000000001010011")
#print("movi: ",register_list)
#ls("1000000100000011")
#print("ls: ",register_list)
#rs("1000000100000011")
#print("rs: ",register_list)