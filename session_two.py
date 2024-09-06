'''iteration = 0
while iteration < 5 :
    # if iteration == 3 :
    #     break
    if iteration == 3 :
        continue
    print ('ali')
    iteration += 1'''

# for j in range(0,5,1): #[0,1,2,3,4], range(0,5,1)==range(5)
#     print('ali') 

# for d in range (10 , 2) :
#     print (d , end = " ")

# print ([ d for d in range (0 ,10 , 2)])


# for h in range (5) :
#     for g in range (3) :
#         print ((h , g ) , end = "&")

#home work 
# *
# **
# ***
# ****
# *****



# stars = "*"
# iteration= input()
# iteration = int(iteration)
# stars_number=1
# while stars_number < iteration :
#     print (stars)
#     stars = stars + "*"
#     stars_number = stars_number + 1
    
# print (stars)



'''stars = "*"
iteration= input()
iteration = int(iteration)
stars_number=1

for a in range (iteration) :
    print (stars)
    stars = stars + "*"
    stars_number = stars_number + 1
print (stars)'''


iteration=int(input())
for i in range(1,iteration+1):
    for j in range(i):
        print('*', end='')
    print('\n')



