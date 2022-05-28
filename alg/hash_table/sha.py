import hashlib

print("The available algorithms are : ", end="")
print(hashlib.algorithms_guaranteed)

# Python 3 code to demonstrate
# SHA hash algorithms.

# initializing string
init_str = "ImpossibleIsNothing"

# encoding GeeksforGeeks using encode()
# then sending to SHA256()
result = hashlib.sha256(init_str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

print("\r")

# initializing string
init_str = "ImpossibleIsNothing"

# encoding GeeksforGeeks using encode()
# then sending to SHA384()
result = hashlib.sha384(init_str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())

print("\r")

# initializing string
init_str = "ImpossibleIsNothing"

# encoding GeeksforGeeks using encode()
# then sending to SHA224()
result = hashlib.sha224(init_str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())

print("\r")

# initializing string
init_str = "ImpossibleIsNothing"

# encoding GeeksforGeeks using encode()
# then sending to SHA512()
result = hashlib.sha512(init_str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())

print("\r")

# initializing string
init_str = "ImpossibleIsNothing"

# encoding GeeksforGeeks using encode()
# then sending to SHA1()
result = hashlib.sha1(init_str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
