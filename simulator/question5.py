

import math
addressable_types = {"BIT ADDRESSABLE MEMORY":1/8,
                     "NIBBLE ADDRESSABLE MEMORY":1/2,
                     "BYTE ADDRESSABLE MEMORY":1,
                     "WORD ADDRESSABLE MEMORY":1}
units = {"B":0,"KB":10,"MB":20,"GB":30,"TB":40, "WORD": 0, "KWORD": 10, "MWORD": 20, "GWORD":30, "TWORD":40}

def isaq(mem_space, addressable_types, mem_add_type, unit, mem_space_value):
    instr_len = int(input("Enter length of instruction in bits: "))
    reg_len = int(input("Enter length of register in bits: "))
    if len(unit)>=2:
        ans = units[unit.upper()]  
    else:
        ans=0

    #print(ans)
    address_len= int(math.log(mem_space_value*(2**ans)/addressable_types[mem_add_type],2))
    #address_len = ((int(math.log(mem_space_value,2)))+ans)/addressable_types[mem_add_type]
    opcode = instr_len - reg_len - address_len
    filler_bits = instr_len - 2*reg_len - opcode
    maxnum_instr = 2**opcode
    maxnum_reg = 2**reg_len
    if int(address_len)>int(instr_len):
        print("Error: Instruction length is too small")
    else:
        print('Minimum bits to represent an address: ',int(address_len))
        print('Number of bits needed by opcode: ',int(opcode))
        print('Number of filler bits: ',int(filler_bits))
        print('Number of maximum instructions: ',int(maxnum_instr))
        print('Maximum number of registers: ',maxnum_reg)
    return address_len


def type1(addressable_types, mem_space_value, old_add_len, unit, units):
    cpu=int(input('Input the number of bits of the CPU: '))
    i=0
    for keys in addressable_types.keys():
        i+=1
        print(i,":",keys)
    new_mem_add_type=input('Input change in how you would like to address memory: ')
    new_mem_add_type=new_mem_add_type.upper()
    if len(unit)>=2:
        ans = units[unit.upper()]  
    else:
        ans=0
    if 'Word' in unit:
        mem_space_value=mem_space_value*(cpu/8)
    #addressable_types["WORD ADDRESSABLE MEMORY"]=1/8
    if new_mem_add_type=='WORD ADDRESSABLE MEMORY':
        deno=(cpu/8)
    else:
        deno=addressable_types[new_mem_add_type]
    if len(unit)>=2:
        ans = units[unit.upper()]  
    else:
        ans=0
    new_address_len= int(math.log(mem_space_value*(2**ans)/deno,2))
    #new_address_len = ((int(math.log(mem_space_value,2)))+ans)/deno
    #print(new_address_len, old_add_len, deno, ans, mem_space_value)
    print('Number of address pins: ',int(new_address_len-old_add_len))



def type2(addressable_types, mem_space_value,unit, units):
    cpu=int(input("Input the number of bits of CPU: "))
    add_pin=int(input("Input address pins: "))
    mem_type=input("Input the type of memory: ")

    if mem_type.upper()=='BIT ADDRESSABLE MEMORY':
        mem_val=add_pin-3
    elif mem_type.upper()=='NIBBLE ADDRESSABLE MEMORY':
        mem_val=add_pin-1
    elif mem_type.upper()=='BYTE ADDRESSABLE MEMORY':
        mem_val=add_pin
    else:
        mem_val=add_pin+3

    if mem_val<10:
        print('Size of main memory: ',2**mem_val, ' B')
    elif mem_val>=10 and mem_val<20:
        print('Size of main memory: ',2**(mem_val-10), 'KB')
    elif mem_val>=20 and mem_val<30:
        print('Size of main memory: ',2**(mem_val-20), 'MB')
    elif mem_val>=30 and mem_val<40:
        print('Size of main memory: ',2**(mem_val-30), 'GB')
    else:
        print('Size of main memory: ',2**(mem_val-40), 'TB')
    


#main
mem_space = str(input("Enter space in memory: "))
unit=''
val=''
for ch in mem_space:
    if ch.isalpha()==True:
        
        unit=unit+ch
    elif ch in '0123456789':
        val=val+ch

val=int(val)
#print(unit)
if unit=="b":

    mem_space_value = int(int(mem_space[:-1])/8)
elif 'Word' in unit:
    mem_space_value=val
else:
    mem_space_value = int(mem_space[:-2])
i=0
for keys in addressable_types.keys():
    i+=1
    print(i,":",keys)
mem_add_type = str(input("Enter how you would like to address memory: "))
# mem_add_type = "BYTE ADDRESSABLE MEMORY"

mem_add_type=mem_add_type.upper()
#address_len=isaq(mem_space, addressable_types, mem_add_type, unit,nmem_space_value)
address_len=isaq(mem_space, addressable_types, mem_add_type, unit,mem_space_value)



type1(addressable_types, mem_space_value, address_len, unit, units)
type2(addressable_types, mem_space_value,unit, units)
