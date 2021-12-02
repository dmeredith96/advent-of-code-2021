def solve():
    number_of_increases = 0;
    input_file = open("input.txt")
    a1 = int(input_file.readline())
    a2 = int(input_file.readline())
    a3 = int(input_file.readline())
    current_sum=a1+a2+a3
    last_sum=0
    while(True): 
        last_sum=int(current_sum)
        a1=int(a2)
        a2=int(a3)
        a3=input_file.readline()
        if(len(a3) == 0):
            break;
        current_sum=a1+a2+int(a3)
        if(current_sum>last_sum):
            number_of_increases +=1
       
    return number_of_increases;

print(solve())