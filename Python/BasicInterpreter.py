import math

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, STRING, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, POW, EULER, EOF = (
    'INTEGER', 'STRING','PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'POW', 'EULER', 'EOF'
)

######### TOKEN ##################################################################
##################################################################################
class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

######### FUNCTIONS ##############################################################
##################################################################################
def const(a):
    def func(x):
        return a
    return func

def x(x):
    return x

def e(x):
    return math.e

def add(f, g):
    def func(x):
        return f(x) + g(x)
    return func

def subs(f, g):
    def func(x):
        return f(x) - g(x)
    return func

def mult(f, g):
    def func(x):
        return f(x) * g(x)
    return func

def div(f, g):
    def func(x):
        return f(x) / g(x)
    return func

def pow(f, g):
    def func(x):
        return math.pow(f(x), g(x))
    return func

#def e(x):
#    return math.e

######### LEXER ##################################################################
##################################################################################
class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, const(self.integer()))

            if self.current_char == 'x':
                self.advance()
                return Token(STRING, x)

            if self.current_char == 'e':
                self.advance()
                return Token(EULER, e)

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')
            
            if self.current_char == '^':
                self.advance()
                return Token(POW, '^')

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            self.error()

        return Token(EOF, None)

######### INTERPRETER ############################################################
##################################################################################
class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : INTEGER | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == STRING:
            self.eat(STRING)
            return token.value
        elif token.type == EULER:
            self.eat(EULER)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result

    def some(self):
        result = self.factor()

        while self.current_token.type in (POW):
            token = self.current_token
            if token.type == POW:
                self.eat(POW)
                result = pow(result, self.factor())

        return result

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        result = self.some()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = mult(result, self.some())
            elif token.type == DIV:
                self.eat(DIV)
                result = div(result, self.some())

        return result

    def expr(self):
        """Arithmetic expression parser / interpreter.

        calc> 7 + 3 * (10 / (12 / (3 + 1) - 1))
        22

        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER | LPAREN expr RPAREN
        """
        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = add(result, self.term())
            elif token.type == MINUS:
                self.eat(MINUS)
                result = subs(result, self.term())

        return result

def parse(s):
    lex = Lexer(s)
    interp = Interpreter(lex)
    res = interp.expr()
    return res

######################### INTEGRACION NUMERICA #########################
# Trapezoidal con aplicacion multiple
def trapezoidal(a, b, n, f):
    h = (b-a)/float(n)
    sum = f(a)
    for i in range(1, n):
        sum = sum + 2 * f(a + i * h)
    sum = sum + f(a+n*h)
    return h * sum / 2

def simpson(a, b, n, f):
    if(n < 2):
        return "Error: Intervalos insuficientes"
    def simp13(a,h,n,f):
        sum = f(a)
        for i in range(1, n-2, 2):
            sum += 4 * f(a+i*h) + 2 * f(a+(i+1)*h)
        sum += 4 * f(a+(n-1)*h) + f(a+n*h) 
        return h * sum / 3
    def simp38(a,h,f):
        return 3 * h * (f(a)+3*(f(a+h)+f(a+2*h)+f(a+3*h))) / 8
    h = (b-a)/float(n)
    if(n%2):
        return simp13(a,h,n-3,f) + simp38(b-h*3, h, f)
    else:
        return simp13(a, h, n, f)




######################### RAICES #########################

def samesign(a,b):
    return a * b > 0

# Biseccion
def bisect(func, low, high, iterations, threshold):
    assert not samesign(func(low), func(high))

    for i in range(iterations):
        midpoint = (low + high) / 2.0
        ea = ((low-high)/(low+high))*100
        if ea < threshold:
            return midpoint
        if samesign(func(low), func(midpoint)):
            low = midpoint
        else:
            high = midpoint
    return midpoint

# Secante
def secante(f, ai, a, n):
    for i in range(a, n+1):
        af = a - f(a)*((ai-a)/(f(ai)-f(a)))
        ai = a
        a = af
        if(ai == af):
            return af
    return af

# Newton Raphson
def newton_raphson(func, x0, iterations, threshval):
    # Derivada
    def der(f, x):
        h = 0.000000000001
        val1 = (f(x+h)-f(x))/h
        val2 = (f(x-h)-f(x))/-h
        return (val1+val2)/2

    for i in range(iterations):
        xi = x0 - (func(x0)/der(func, x0))
        if ((xi - x0)/(xi + x0))*100 < threshval:
            return xi
        x0 = xi
    return xi


######################## SISTEMAS DE ECUACIONES #########################

def print_mat(mat):
    for i in range(len(mat)):
        print mat[i]
    print "--"

def montante(mat):
    last_pivot = 1
    for k in range(len(mat)):
        #Transforma el arreglo para el pivote
        for i in range(len(mat)):
            if(i != k):
                for j in range(k+1, len(mat[0])):
                    mat[i][j] = (mat[k][k]*mat[i][j]-(mat[k][j]*mat[i][k]))/last_pivot
        # Llenar columna del pivote con 0s
        for i in range(len(mat)):
            if(i != k):
                mat[i][k] = 0
        # Cambiar pivote anterior por actual
        for p in range(k):
            mat[p][p] = mat[k][k]
        # Actualizar pivote anterior
        last_pivot = mat[k][k]
    # Guarda los valores resultantes en un arreglo
    results = []
    last_column = len(mat[0])-1
    for x in range(len(mat)):
        results.append(float(mat[x][last_column])/float(mat[x][x]))
    return results


####################### INTERPOLACION ###########################

def lagrange(ax, ay):
    n = len(ax)
    suma = const(0)
    for i in range(n):
        term = const(ay[i])
        for j in range(n):
            if i != j:
                xi = const(ax[i])
                xj = const(ax[j])
                term = mult(term, div(subs(x, xj), subs(xi,xj)))
        suma = suma(suma, term)
    return suma 


# def newton(ax,ay):
#     fdd = []
#     for i in range(n)


######################## AJUSTE DE CURVAS #########################
arreglo_x = [.75, 2, 3, 4, 6, 8, 8.5]
arreglo_y = [1.2, 1.95, 2, 2.4, 2.4, 2.7, 2.6]

# Regresion Lineal
def regresionLineal(x, y):
    x_squared = map(lambda x: x ** 2, x)
    x_times_y = [a*b for a,b in zip(x, y)]
    
    first_row = [len(x), sum(x), sum(y)]
    second_row = [sum(x), sum(x_squared), sum(x_times_y)]
    
    matrix = [first_row, second_row]
    
    return montante(matrix)

# Regresion Potencial
def regresionPotencial(x, y):
    ln_x_arr = map(lambda x: math.log(x), x)
    ln_y_arr = map(lambda y: math.log(y), y)
    ln_x_squared = map(lambda x: x ** 2, ln_x_arr)
    lnx_times_lny = [a*b for a,b in zip(ln_x_arr, ln_y_arr)]
    
    first_row = [len(x), sum(ln_x_arr), sum(ln_y_arr)]
    second_row = [sum(ln_x_arr), sum(ln_x_squared), sum(lnx_times_lny)]
    
    matrix = [first_row, second_row]
    
    return montante(matrix)

# Regresion Exponencial
def regresionExponencial(x, y):
    x_squared = map(lambda x: x ** 2, x)
    ln_y_arr = map(lambda y: math.log(y), y)
    lny_times_x = [a*b for a,b in zip(ln_y_arr, x)]
    
    first_row = [len(x), sum(x), sum(ln_y_arr)]
    second_row = [sum(x), sum(x_squared), sum(lny_times_x)]
    
    matrix = [first_row, second_row]
    
    return montante(matrix)

# Regresion Parabola
def regresionParabola(x, y, n):
    x_arr = []
    y_arr = []
    x_times_y = [a*b for a,b in zip(x, y)]
    
    for i in range(1, n+2):
        i_arr = map(lambda x: x ** i, x)
        x_arr.append(i_arr)

    for j in range(1, n):
        j_arr = [a*b for a,b in zip(y, x_arr[j-1])]
        y_arr.append(j_arr)
    
    matrix = [[len(x), sum(x_arr[0]), sum(x_arr[1]), sum(y)]]
    for k in range(1, n):
        matrix.append([sum(x_arr[k-1]), sum(x_arr[k]), sum(x_arr[k+1]), sum(y_arr[k-1])])
    
    return montante(matrix)

############################### MAIN #############################
def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = raw_input('f(x): ')
            # aval = raw_input('a = ')
            # bval = raw_input('b = ')
            # iterval = raw_input('iterations: ')
            # thresval = raw_input('threshold: ')
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print der(result, 0)
        print result(1)

        print "** Regresion **"
        print regresionLineal(arreglo_x, arreglo_y)
        print regresionPotencial(arreglo_x, arreglo_y)
        print regresionExponencial(arreglo_x, arreglo_y)
        print regresionParabola(arreglo_x, arreglo_y, 3)

if __name__ == '__main__':
    main()
