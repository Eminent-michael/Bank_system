import random
import time
import pandas as pd


while True:
    guess = random.randint(100000, 999999)
    ap = []

    file = pd.read_fwf("account_list.txt", header=None)
    all_list = list(file.loc[:, 0])
    if guess in all_list:
        print("Account number already existed.")
        time.sleep(2)
    else:
        ap.append(guess)
        df = pd.DataFrame(ap)
        df.to_csv("account_list.txt", mode="a", header=None, index=None)
        print("Jesus!!!")
        break
print(guess)
print(file)

pin = input("Enter the 4 digit for your pin: ")
while len(pin) > 4 or len(pin) < 4:
    pin = input("Enter the 4 digit for your pin: ")
print(pin)





# file_path = "account_list.txt"
# with open("account_list.txt", "r") as file:
#     for lines in file:
#         time.sleep(2)
#         if str(n) not in lines:
#             # print("Account has being added to the list.")
#             # print(n)
#             with open("account_list.txt", "a") as acct:
#                 acct = acct.write(str(n) + "\n")
#     lines.truncate()
#         else:
#             print("Account number already existed.")
#             break
#
#
# # file = file.write(str(n) + "\n")
