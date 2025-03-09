# nums = [1, 4, 6, 7, 4, 5,]
# total = 0
# for num in nums:
#     total = total + num
# print(f"total is {total}")
# avg = total / len(nums)
# print(f"average is {avg}")

numbers = []
num = 1
sum = 0
 
print("Enter a list of numbers, type 0 when finished.")
while num != 0:
    num = int(input("Enter number: "))
    numbers.append(num)
 
for number in numbers:
    sum = sum + number
print(f"The sum is: {sum}")
 
average = sum / (len(numbers) - 1)
print(f"The average is: {average}")
 
largest = 0
for number in numbers:
    if number > largest:
        largest = number
print(f"The largest number is: {largest}")
 