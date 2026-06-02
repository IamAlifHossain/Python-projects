#Python credit card validator program
# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#                (If result is a two-digit number,
#                 add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

odd_sum = 0
even_sum = 0
total = 0
# step 1
card_num = input("Enter you credit card number = ")
card_num = card_num.replace("-", "")
card_num = card_num.replace(" ", "")
card_num = card_num[::-1]
# print(card_num)

# step 2
for x in card_num[::2]:
    odd_sum += int(x)

# step 3
for x in card_num[1::2]:
    x = int(x)*2
    if x>=10:
        even_sum +=(1+x%10)
    else:
        even_sum+=x

# step 4
total = odd_sum + even_sum

# step 5
if total%10==0:
    print("Valid")
else:
    print("Invalid")
