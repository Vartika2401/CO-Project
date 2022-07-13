def movi(register_list,instruction):
    reg = instruction[5:8]
    imm = instruction[8:]
    for i in range(7):
        if reg==register_dict["R"+str(i)]:
            register_list[i]="00000000"+str(imm)
def rs(register_list,instruction):
    reg = instruction[5:8]
    imm = instruction[8:]
    for i in range(7):
        if reg == register_dict["R" + str(i)]:
            print(int(imm,2))
            if int(imm,2)>16:
                register_list[i]="0000000000000000"
            else:
                register_list[i]=register_list[i][0:16-int(imm,2)]
                while len(register_list[i])<16:
                    register_list[i]="0"+register_list[i]
                print(register_list[i])
def ls(register_list,instruction):
    reg = instruction[5:8]
    imm = instruction[8:]
    for i in range(7):
        if reg == register_dict["R" + str(i)]:
            print(int(imm, 2))
            if int(imm, 2) > 16:
                register_list[i] = "0000000000000000"
            else:
                register_list[i] = register_list[i][int(imm, 2):]
                while len(register_list[i]) < 16:
                    register_list[i] = register_list[i]+"0"
                print(register_list[i])
