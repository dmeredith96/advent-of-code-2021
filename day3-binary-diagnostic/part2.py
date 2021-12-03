def solveOxygen():
    file = open('input.txt')
    valid_oxygen_numbers = []
    current_line = file.readline()

    while(current_line != ''):
        valid_oxygen_numbers.append(current_line.strip())
        current_line = file.readline()
    length_of_number = len(valid_oxygen_numbers[0])
    i = 0
    while i < length_of_number:
        if len(valid_oxygen_numbers) == 1:
            break
        new_valid_numbers = []
        ones = 0
        zeros = 0
        for str_num in valid_oxygen_numbers:
            if str_num[i] == '0':
                zeros += 1
            elif str_num[i] == '1':
                ones += 1
        for str_num in valid_oxygen_numbers:
            if zeros > ones:
                if str_num[i] == '0':
                    new_valid_numbers.append(str_num)
            else:
                if str_num[i] == '1':
                    new_valid_numbers.append(str_num)
        valid_oxygen_numbers = new_valid_numbers
        i += 1
    return valid_oxygen_numbers

def solveCO2():
    file = open('input.txt')
    valid_co2_numbers = []
    current_line = file.readline()

    while(current_line != ''):
        valid_co2_numbers.append(current_line.strip())
        current_line = file.readline()
    length_of_number = len(valid_co2_numbers[0])
    i = 0
    while i < length_of_number:
        if len(valid_co2_numbers) == 1:
            break
        new_valid_numbers = []
        ones = 0
        zeros = 0
        for str_num in valid_co2_numbers:
            if str_num[i] == '0':
                zeros += 1
            elif str_num[i] == '1':
                ones += 1
        for str_num in valid_co2_numbers:
            if zeros > ones:
                if str_num[i] == '1':
                    new_valid_numbers.append(str_num)
            else:
                if str_num[i] == '0':
                    new_valid_numbers.append(str_num)
        valid_co2_numbers = new_valid_numbers
        i += 1
    return valid_co2_numbers

oxygen = solveOxygen()[0]
co2 = solveCO2()[0]

print(int(oxygen,2)*int(co2,2))
