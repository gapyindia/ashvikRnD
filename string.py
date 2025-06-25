str1="ashvik"
str2="_"
str3="raj"
str4="_"
str5="aaron"
print(str1,str2,str3,str4,str5)
str6=1/2
str7=1/2
str8=(str6+str7)
print(str8)
str9=34
str0=56
str10=(str9*str0)
print(str10)
str11=(str1,str2,str3,str4,str4,str5,str6,str7,str8,str9,str0,str10)
print(str11)
str12=(str1,str2,str3,str4,str5)
print(str12)
fred ="other_name_of_string"
print(fred)
fred1 = '''How do dinosaurs pay their bills?
With tyrannosaurus checks!'''
print(fred1)
myscore = 1000
message = 'I scored %s points'
print(message % myscore)
single_quote_str = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
double_quote_str = "He said, \"Aren't can't shouldn't wouldn't.\""
print(single_quote_str)
print(double_quote_str)
joke_text = '%s: a device for finding furniture in the dark'
bodypart1 = 'Knee'
bodypart2 = 'Shin'
print(joke_text % bodypart1)
print(joke_text % bodypart2)
spaces = ' ' * 25
print('%s to' % spaces)
print('%s the_headmaster'% spaces)
print('%s gururkul_center_school__ghoshi_jehanabad' % spaces)
print()
print()
print('Dear_ Sir')
print()
print('most_humbly_and_rsepectfully_i_beg_to_state_that_i_am_suffering_from')
print('fever_.')
print('i,therefore,request_you_to_allow_to_take_a_one_day_levea')
print()
print('Regards,turthful')
print('asvik_raj_aaron,8,22,b')
a=int(input('enter_number_a:'))
b=int(input('enter_number_b:'))
print('the_sum_of_a_and_b_is:',(a+b-a-b))
a=input('enter_number_a:')
b=input('enter_number_b:')
print('theaddofaandbis:',(a+b))

username = input("Enter username:")
print("Username is: " + username)
print("Username is(lower): " + username.lower())
print("Username is(upper): " + username.upper())
print("Username is(len): " + str(len(username)))
print("Username is(lower):"+username.lower())

name="ashvik"
nameshort=name[0:6]
print(nameshort)

a="ashvik is good boy \nthen garvit"
print(a)

name=input("enter_your_name:")
print(f"good_morning,{name}")

letter='''dear<|name|>,
you are selected !
<|date|>'''
print(letter.replace("<|name|>","ashvik").replace("<|date|>","12/9/2024"))