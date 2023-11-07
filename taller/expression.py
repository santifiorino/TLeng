class Expression():
    def evaluate(self):
        raise NotImplementedError

class Sum(Expression):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def evaluate(self):
        return self.op1.evaluate() + self.op2.evaluate()

class Sub(Expression):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        
    def evaluate(self):
        return self.op1.evaluate() - self.op2.evaluate()

class Prod(Expression):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        
    def evaluate(self):
        return self.op1.evaluate() * self.op2.evaluate()

class Div(Expression):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        
    def evaluate(self):
        return self.op1.evaluate() / self.op2.evaluate()

class Par(Expression):
    def __init__(self, op1):
        self.op1 = op1
        
    def evaluate(self):
        return self.op1.evaluate()

class Neg(Expression):
    def __init__(self, op1):
        self.op1 = op1
        
    def evaluate(self):
        return -self.op1.evaluate()

class Id(Expression):
    def __init__(self, op1):
        self.op1 = op1
        
    def evaluate(self):
        return float(self.op1)

class Term(Expression):
    def __init__(self, op1):
        self.op1 = op1
        
    def evaluate(self):
        return self.op1.evaluate()

class Factor(Expression):
    def __init__(self, op1):
        self.op1 = op1
        
    def evaluate(self):
        return self.op1.evaluate()