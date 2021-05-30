import math

class NormalOpration:
	"""add, sub, mul, div"""
	
	def __init__(self, variable_01, variable_02):
		self.variable_01 = variable_01
		self.variable_02 = variable_02
		
	def add(self):
		return(self.variable_01 + self.variable_02)
		
	def sub(self):
		return(self.variable_01 - self.variable_02)
		
	def mul(self):
		return(self.variable_01 * self.variable_02)
		
	def div(self):
		return(self.variable_01 / self.variable_02)
		
		
		
class Power:
	"""Two di power"""
	
	def __init__(self, variable_01, variable_02):
		self.variable_01 = variable_01
		self.variable_02 = variable_02
	
	def pow(self):
		return(self.variable_01 ** self.variable_02)



class Root:
    """ Root the value """

    def __init__(self, variable_01):
        self.variable_01 = variable_01
        
    def root(self):
        return(math.sqrt(variable_01))



class Modulus:
    """ modulus the value """

    def __init__(self, variable_01, variable_02):
        self.variable_01 = variable_01
        self.variable_02 = variable_02

    def mod(self):
        return(self.variable_01 % self.variable_02)



class UserManual:
    """ user manual """


    def manual(self):
        print("\n\n                         USER MANUAL                           ")
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print(" FOR ADDITION ==================== addition value1 value2 ")
        print(" FOR SUBTRACTION ================= subtraction value1 value2 ")
        print(" FOR MULTIPLICATION ============== multiplication value1 value2 ")
        print(" FOR DIVISION ==================== division value1 value2 ")
        print(" FOR EXPONENTIATION ============== power value1 value2 ")
        print(" FOR SQUARE ROOT ================= root value ")
        print(" FOR MODULAS ===================== modulus value1 value2 ")
        print(" FOR USER MANUAL ===================== manu ")
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

object_UM = UserManual()
object_UM.manual()

""" FOR LOGIC """
value_01 = 1
while (value_01 == 1):
    arr = list(num for num in input("\nEnter Arithmetic  operation(rewuire argument, separate by SPACE)\nOtherwish to Get out type exit\n>>>    ").strip().split())
    variable_03 = arr[0]
    variable_03 = variable_03.lower()

    if variable_03 == "exit":
        value_01 = value_01 + 1
    else:

        if variable_03 == "addition":
            variable_01 = int(arr[1])
            variable_02 = int(arr[2])
            object_02 = NormalOpration(variable_01, variable_02)
            print(">>>    calculate value = ", object_02.add(), "\n")

        elif variable_03 == "subtraction":
            variable_01 = int(arr[1])
            variable_02 = int(arr[2])
            object_02 = NormalOpration(variable_01, variable_02)
            print(">>>    calculate value = ", object_02.sub(), "\n")

        elif variable_03 == "multiplication":
            variable_01 = int(arr[1])
            variable_02 = int(arr[2])
            object_02 = NormalOpration(variable_01, variable_02)
            print(">>>    calculate value = ", object_02.mul(), "\n")

        elif variable_03 == "division":
            variable_01 = int(arr[1])
            variable_02 = int(arr[2])
            object_02 = NormalOpration(variable_01, variable_02)
            print(">>>    calculate value = ", object_02.div(), "\n")

        elif variable_03 == "power":
            variable_01 = int(arr[1])
            variable_02 = int(arr[2])
            object_02 = Power(variable_01, variable_02)
            print(">>>    calculate value = ", object_02.pow(), "\n")

        elif variable_03 == "root":
            variable_01 = int(arr[1])

            object_02 = Root(variable_01)
            print(">>>    calculate value = ", object_02.root(), "\n")

        elif variable_03 == "modulus":
            variable_01 = int(arr[1])
            variable_02 = int(arr[2])
            object_02 = Modulus(variable_01, variable_02)
            print(">>>    calculate value = ", object_02.mod(), "\n")

        elif variable_03 == "manu":
            object_UM = UserManual()
            object_UM.manual()

