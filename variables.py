# variables are dynamically typed

n = 0
print("n = ", n)

# types are determined at runtime

n = "string"
print("n = ", n)

# multiple assignments

n, m = 0, "string"

n, m, z = 0.125, "string", True

# increment

n = n + 1 # -> it's ok
n += 1 # -> it's ok
# not ok in python -> n++

# there is null in python as None
# None -> absence of value
n = None

