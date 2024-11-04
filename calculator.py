class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b+1):
            result = 0
             #= self.add(result, a)
            if a > 0 or a == 0:
                result = result +a
            else:
                result = result + a
        return result - a

    def divide(self, a, b):
        result = 0
        if b == 0 : return "error"
        while a > b:
            a = self.subtract(a, b)
            result += 1
        return result +1
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))