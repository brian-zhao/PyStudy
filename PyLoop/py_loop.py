# for... else

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for i in my_list:
    if i == 10:
        break
    print(i)
else:
    raise ValueError("In else statement")


# Without for ... loop
# flag_found = False
# for i in my_list:
#     if i == 10:
#         flag_found = True
#         break
#     print(i)
#
# if not flag_found:
#     raise ValueError("In else statement.")
