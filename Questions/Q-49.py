#Find the Sum of Even Numbers in a List
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum(n for n in nums if n % 2 == 0)
print("Sum of even numbers:", even_sum)
