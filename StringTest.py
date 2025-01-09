str_1 = "Gara"
str_2 = "Gara Hernandez"
str_3 = "My name is Gara Hernandez"
str_4 = "Gara"
str_5 = 'Campo'

print(len(str_1))
print(str_1[0])
print(str_3[1])
#SubString
print(str_1[1:4])

list_obj = str_3.split(" ")
print(list_obj[1])

#Verify string
print("**************")
print(str_1 == str_2)
print(str_1 == str_4)
print(str_1 in str_2)#True
print(str_1 not in str_2)#false