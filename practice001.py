# Loop through numbers from 1 to 5
numbers = range(1, 6)
for number in numbers:
    print(number)

# Find the largest number in a list
nums = [1, 4, 7, 9, 2, 4, 111, 45, 87, 11, 34, 90]
max = nums[0]
for num in nums:
    if (num > max):
        max = num
print(max)

# print odd and even numbers from a list, and count them
even = []
odd = []
even_count = 0
odd_count = 0
for i in nums:
    if (i % 2 == 0):
        even.append(i)
        even_count += 1
    else:
        odd.append(i)
        odd_count += 1

print(even, odd)
print(f"even: {even_count}, odd: {odd_count}")


# # get sum of all odd numbers from 1 to 100
total = 0
for i in range(1, 101, 2):
    total = total + i

print(total)

# Sum of all even numbers
total = 0
for i in range(2, 101, 2):
    total += i
print(total)
