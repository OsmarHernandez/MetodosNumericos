import math

def const(a):
	def func(x):
		return a
	return func

def x(x):
	return x

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

def e(x):
	return math.e

def pow(f, g):
	def func(x):
		return math.pow(f(x), g(x))
	return func

def ln(f):
	def func(x):
		return math.log(f(x))
	return func

def log(f, g):
	def func(x):
		return math.log(g(x)) / math.log(f(x))
	return func

def sin(f):
	def func(x):
		math.sin(f(x))
	return func

def cos(f):
	def func(x):
		math.cos(f(x))
	return func

def tan(f):
	def func(x):
		math.tan(f(x))
	return func

def pi(x):
	return math.pi