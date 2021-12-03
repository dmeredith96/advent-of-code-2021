def solve():
    counter_dict = {}
    current_file = open('input.txt')
    current_line = current_file.readline()
    gamma_rate = ""
    epsilon_rate = ""
    while(len(current_line) > 0):
        char_index = 0        
        for character in current_line:
            if char_index not in counter_dict:
                counter_dict[char_index] = {}
            if "zero" not in counter_dict[char_index]:
                counter_dict[char_index]["zero"] = 0
            if "one" not in counter_dict[char_index]:
                counter_dict[char_index]["one"] = 0

            if (character == "0"):
                current_count = counter_dict[char_index]["zero"]             
                counter_dict[char_index]["zero"] = (current_count+1)
            else:

                current_count = counter_dict[char_index]["one"]
                counter_dict[char_index]["one"] = (current_count+1)
            char_index += 1
        current_line=current_file.readline()

    print(counter_dict)
    for key,val in counter_dict.items():
        print(val)
        if val["zero"] > val["one"]:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'

    gamma_rate = gamma_rate[:-1]
    epsilon_rate = epsilon_rate[:-1]
    gamma_rate = int((gamma_rate), 2)
    epsilon_rate = int((epsilon_rate), 2)

    return gamma_rate*epsilon_rate

print(solve())