def solve():
    input_file=open('input.txt')
    horizontal_position = 0
    depth = 0
    current_line = input_file.readline()
    while(len(current_line) > 0):        
        action = current_line.split(' ')[0]
        num = int(current_line.split(' ')[1])
        if(action == 'forward'):
            horizontal_position += num
        elif(action == 'down'):
            depth += num
        elif(action == 'up'):
            depth -= num
        current_line=input_file.readline()
    return horizontal_position*depth

print(solve())