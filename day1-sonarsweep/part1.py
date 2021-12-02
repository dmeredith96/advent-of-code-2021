def solve():
    last_depth = 0;
    number_of_increases = 0;
    input_file = open("input.txt")
    current=input_file.readline()
    while(len(current) > 0):
        current = int(current)
        if current > last_depth:
            number_of_increases += 1
        last_depth = current
        current=input_file.readline()
    return number_of_increases-1;

print(solve())