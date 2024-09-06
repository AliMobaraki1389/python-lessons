times= (int(input()))
loop = 1
number_one = 0
number_two = 1
print (number_one , number_two , sep= " " , end=" ")
number_one = number_two
while loop != times//2 :
    number_one  = number_one + number_two
    number_two = number_one + number_two
    loop += 1
    print (number_one , number_two , sep= " " , end=" ")
if times %2 != 0 :
    print (number_one + number_two)


