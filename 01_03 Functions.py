#Functions

#How to define a function
def func():
	print "This is a function definition"
	
#Function Calling 
func()
print func()
print func		# returns the address where functino func() is located

#Passing arguments in a function
def func2(arga, argb):
	print arga,'*', argb
	
# Function call
func2(10,13)

#Function that returns a value
def func3(y):
	return y*y

print func3(4)

# Passing variable no. of arguments
def func4(*args):
	tot = 0
	for i in args:
		tot = tot + i
	return tot

	
print func4(1,2,3,4,12)

# Function with defalut value of an arguments

def func5(num, ras = 1):
	pow = 1
	for i in range(ras):
		pow = pow * num
	return pow
	
print func5(3)		# here, default value of ras = 1 is used
print func5(3,2)	# here, 2 is used as the raise to power
print func5(ras = 2, num = 4)