test_case = int(input())

for i in range(test_case):
    times, input_str = input().split()
    repeated_str = ''
    for j in input_str:
        repeated_str += j*int(times)
    print(repeated_str)

