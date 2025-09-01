# if statements do not need parentheses or braces

n = 1
if n > 2:
  n -= 1
  print(n)
elif n == 2:
  n *= 2
  print(n)
else:
  n += 2

# parentheses needed for multi-line conditions
# and -> &&
# or -> ||

n, m = 1, 2

if((n > 2 and
    n != m) or n == m):
  n += 1

# string usage
print(f"name: { n }")