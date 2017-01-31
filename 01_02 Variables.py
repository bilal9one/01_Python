# Variables, string concatination, global/local 

# How to declare a variable
var = 0
print var

# How to decalare a string variable
strr = 'abc'
print strr

# How to check the type of variable created

print type(var)
print type(strr)

# converting between variables
# str is a built in python function that converts any type to "string" type`
print str(var) # This would have type string


# Concatinate two strings
# + is used to concatinate strings, they should be having string type.
print "Bilal" + "Maqsood" + str(var)

def myfunc():
	#global var
	var = 'new var'		# this var and the var defined above as 0, are different as this var = 'new var' is a local variable of function myfunc(). If you uncomment the #global line, 
						# it will make var a global variable. 
	print var

myfunc()	# This will print var i.e. local to myfunc()
print var	# This will print var  = 0
# to delete an existing variable 
del var
print var	# This print statement will show an error.