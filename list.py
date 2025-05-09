student_name=['abdullah','ahmad','khan']
#display all itms in list
print('student name list:',student_name)
#display a spacific itm, in list
print('3rd name :',student_name[2])
# add new itm in the list
student_name.append('azhar')
#display updated list
print('updated name list:',student_name)
first_name='abdullah'
last_name='khan'
#joining above string togather
full_name =first_name+" "+last_name
print(full_name)
#an other method to joing string 
print(first_name,last_name)
#repeat string
print(first_name * 3)
lough='ha'
print(lough * 3)
# finding lenghth of string means how many letter or charactor in it
print(len(first_name)) # count space ,letters, symbols
#indexing means get a latter by its number in the word (start at 0 from left, start at-1 from right) 
print(first_name[0]) # 1st letter
print(first_name[-1]) # last letter 
# slicing means cutt out a piece of strig 
print(first_name[0:3]) # 0 included and 3 not include [0 to 2 ]
print(first_name[3:]) # 3 to end 
print(last_name[-1:-2]) # does not giving result it mean we will slicing by positive number only 