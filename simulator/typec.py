from simulator.typee import PC


register_list = ['0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000']

def movreg(machine_ins):
    global PC
    global register_list
    reg1=machine_ins[7:12]
    reg2=machine_ins[12:]
    reg1_i=int(reg1,2)
    reg2_i=int(reg2,2)
    register_list[reg1_i]=register_list[reg2_i]
    PC+=1

def divide(machine_ins):
    global PC
    global register_list
    reg3=machine_ins[7:12]
    reg4=machine_ins[12:]
    reg1_i=int(reg3,2)
    reg2_i=int(reg4,2)
    q_val=bin(int(register_list[reg1_i],2)//int(register_list[reg2_i],2))[2:]
    r_val=bin(int(register_list[reg1_i],2)%int(register_list[reg2_i],2))[2:]
    while len(q_val)<16:
        q_val='0'+q_val

    while len(r_val)<16:
        r_val='0'+r_val

    register_list[0]=q_val
    register_list[1]=r_val
    PC+=1
    

def invert(machine_ins):
    global PC
    global register_list
    reg1=machine_ins[7:12]
    reg2=machine_ins[12:]
    reg1_i=int(reg1,2)
    reg2_i=int(reg2,2)
    reg1_val=register_list[reg1_i]
    reg1_val=int(reg1_val,2)
    reg1_val= ~reg1_val
    reg1_val=bin(reg1_val)[2:]
    while len(reg1_val)<16:
        reg1_val='0'+reg1_val

    register_list[reg2_i]=reg1_val

    PC+=1

def cmp(machine_ins):
    global PC
    global register_list
    reg1=machine_ins[7:12]
    reg2=machine_ins[12:]
    reg1_i=int(reg1,2)
    reg2_i=int(reg2,2)
    reg1_val=int(register_list[reg1_i],2)
    reg2_val=int(register_list[reg2_i],2)
    if reg1_val>reg2_val:
        temp_flag=register_list[6]
        temp_flag=list(temp_flag)
        temp_flag[14]='1'
        register_list[6]=''.join(temp_flag)
    elif reg1_val<reg2_val:
        temp_flag=register_list[6]
        temp_flag=list(temp_flag)
        temp_flag[13]='1'
        register_list[6]=''.join(temp_flag)
    else:
        temp_flag=register_list[6]
        temp_flag=list(temp_flag)
        temp_flag[15]='1'
        register_list[6]=''.join(temp_flag)

    PC+=1



