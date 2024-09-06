name ="ali" #create varriable
print (type(name)) #show the type (SRT , INt , bool , floet)
name_upper = name.upper() #make every letter to captal
print (name_upper) # print new name
print (name.islower()) # if all of the letter in this varriable be small = true

esm = "alli2%" #creat new varriable
print (esm.replace("l" , "s" , 1)) # replace first letter (l) with (s) / third number for show wich letter
print (esm.isalpha()) # is the varriable have letter
print (esm.isnumeric())# is the varriable have number
print (esm.isalnum())# is the varriable have letter or number

#ruls for choosing letter for varriable =
#dont start with number
#diffrent upper & lower is importante
#NO space
#NO special charechter

vasayel = "ali's book"
vasayel2 = 'ali\'s book'

#when we use ' for our string and in the string we have ' too we use \ to connect the words

print (vasayel2)
print ("ali \n book") # go to next line
print ("ali \t book") # write 8 space
print (vasayel + " " + vasayel2) # write space middle of the words


print (vasayel , vasayel2 , sep = " & " , end = " ")
print ("ali")

# sep : is for the letter insted of (,) when you want to print more than two word
# end : is for the next print that where it's will write ... python use "\n" in defult

A = input() #every input is STR
A = int () #you have to change the type first then put the new input type in new or your last varriable
print (type(A)) # print typy of varriable (A)


#python run the cod line by line


# homework 
print ("HOMEWORK")

student = "ALI"
print (student.upper())
print (student.lower())
print (student.islower())
print (student.isupper())
print (student.isalpha())
print (student.isnumeric())
print (student.isalnum())

print (student.replace("L" , "S" , 1))

first = "Ali"
second = "ahmad"
third = "reza"

Match_Report = ("Hello\nwinner of the match is " + (first) + " and second person is " + (second) + " and third person is " + (third) + " thank you\tMR mobaraki")
print (Match_Report)

print ("first = " + first , end = " ")
print ("second = " + second , end = " ")
print ("third = " + third)


thing = input()
if thing.isalpha() == True :
    print ("letter")
elif thing.isnumeric() == True :
    print ("number")
    thing = int()
else :
    print ("ERROR")