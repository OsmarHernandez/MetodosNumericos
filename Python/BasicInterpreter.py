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

def sum(f, g):
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
                result = sum(result, self.term())
            elif token.type == MINUS:
                self.eat(MINUS)
                result = subs(result, self.term())

        return result


######################### RAICES #########################

def samesign(a,b):
    return a * b > 0

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

def der(f, x):
    h = 0.000000000001
    val1 = (f(x+h)-f(x))/h
    val2 = (f(x-h)-f(x))/-h
    return (val1+val2)/2

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
        # print bisect(result, int(aval), int(bval), int(iterval), float(thresval))
        print der(result, 0)
        print result(1)


if __name__ == '__main__':
    main()
