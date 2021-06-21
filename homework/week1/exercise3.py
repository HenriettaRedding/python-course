#3a
float_var = 8.98
int_var = 4
str_var = "Jam"
#3b

print(f"yUM! {str_var.swapcase()}!")
#inverts the cases in a string
print (f"All you need is: {int_var.bit_length()}!")
#shows the number of bits necessary to represent the integer in binary
#print(dir(float_var))
print(f"Apparently the answer is: {float_var.hex()}!")
#shows a float as a hexdecimal string