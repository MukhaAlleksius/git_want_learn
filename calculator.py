class Calculator:

    last_res = 0

    def sum(self, n1, n2):
        self.last_res = n1 + n2
        return self.last_res

    def minus(self, n1, n2):
        self.last_res = n1 - n2
        return self.last_res
    
    def multiply(self, n1, n2):
        self.last_res = n1 * n2
        return self.last_res
    
    def division(self, n1, n2):
        self.last_res = n1 / n2
        return self.last_res
