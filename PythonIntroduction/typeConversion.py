num_int = 2
num_float = 3.2

#num_sum is implicitly assigned to float type to prevent data loss
# - python converts small to large data type to prevent data loss
num_sum = num_int + num_float
print(type(num_int), type(num_float), type(num_sum))

num_str = "4"
# Type error - unsupported types for +, string and integers dont add even though string is of higher type, explicit type conversion required
num_sum = num_int + int(num_str)
print(num_sum)
