# file=  open("my_file.txt") = with open("my_file.txt") as file
with  open("../../Desktop/my_file.txt") as file:
    content= file.read()
    print(content)
# with open("new_file.txt", mode="w") as file:
#     file.write("\nnew Text")