def verify_code(value):
    return ((int(value[0])**2 + int(value[1])**2 + int(value[2])**2 + int(value[3])**2 + int(value[4])**2)%10)


value = input().replace(" ",'')
ver_code = verify_code(value)
print(str(ver_code))
