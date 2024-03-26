def main():
    origin, amount = input().split()
    output = input()

    in_atoms = {}
    out_atoms = {}

    num_string = ""
    current = ""
    
    for i in range(len(origin)):
        if origin[i].isalpha():
            if current != "": 
                in_atoms[current] = (int(num_string) if num_string != "" else 1) * int(amount)
                
            num_string = ""
            current = origin[i]
            
            if current not in in_atoms:
                in_atoms[current] = 1
        else:
            num_string += origin[i]
            if i == len(origin) - 1:
                in_atoms[current] = int(num_string) * int(amount)

    if num_string == "" and current != "": in_atoms[current] += int(amount)

    num_string = ""
    current = ""
    
    for i in range(len(output)):
        if output[i].isalpha():
            if current != "": 
                out_atoms[current] = (int(num_string) if num_string != "" else 1)
                
            num_string = ""
            current = output[i]
            
            if current not in out_atoms:
                out_atoms[current] = 1
        else:
            num_string += output[i]
            if i == len(output) - 1:
                out_atoms[current] = int(num_string)
                    
    for key in out_atoms:
        if key not in in_atoms:
            print(0)
            return
    
    multiplier = 1
    
    temp = out_atoms.copy()
    
    while True:
        for i in out_atoms:
            temp[i] = out_atoms[i] * multiplier
        for key in out_atoms:
            if temp[key] > in_atoms[key]:
                print(multiplier - 1)
                return
        multiplier += 1

main()