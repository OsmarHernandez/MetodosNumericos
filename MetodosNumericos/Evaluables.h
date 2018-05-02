#include <iostream>
#include <vector>
#include <cmath>
#include <sstream>
#include <iomanip>
using namespace std;

class Expresion;
class Funcion;
class Producto;
class Cociente;
class Variable;
class Polinomio;
class Constante;
class Exponencial;
class RaizCuadrada;
class Seno;
class Coseno;
class Tangente;

class Expresion{
    public:
        Expresion() {}
        virtual ~Expresion() {}
        virtual double eval(double x) = 0;
        virtual string toString(Expresion* input = NULL, int index = 0) = 0;
        virtual void init(Funcion* func) = 0;
    protected:
        Expresion* select();
};

class Polinomio : public Expresion{
    private:
        vector<Expresion*> terminos;
    public:
        Polinomio() {}
        ~Polinomio() {
            int size = terminos.size();
            for(int i = 0; i < size; i++)
                delete terminos[i];
        }
        double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

class Funcion{
    private:
        Polinomio* expr;
        double simpson13(double a, double b, int n);
        double simpson38(double a, double b);
    public:
        Funcion() { expr = NULL; }
        ~Funcion() { delete expr; }
        double eval(double x);
        void print(Expresion* input = NULL, int index = 0);
        void init();
        double trapecio(double a, double b, int n);
        double simpson(double a, double b, int n);
};

class Producto : public Expresion{
    private:
        vector<Expresion*> factores;
    public:
        Producto() {}
        ~Producto() {
        	int size = factores.size();
        	for (int i = 0; i < size; i++)
        		delete factores[i];
        }
        double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

class Cociente : public Expresion{
    private:
        Expresion* dividendo;
        Expresion* divisor;
    public:
        Cociente() {
            dividendo = NULL;
            divisor = NULL;
        }
        ~Cociente() {
            delete dividendo;
            delete divisor;
        }
        double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

class Variable : public Expresion{
    public:
        Variable() {}
        ~Variable() {}
        double eval(double x) { return x; }
        string toString(Expresion* input = NULL, int index = 0) { return "x"; }
        void init(Funcion* func) {};
};

class Constante : public Expresion{
    private:
        double value;
    public:
        Constante() {}
        ~Constante() {}
        double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

class Exponencial : public Expresion{
    private:
        Expresion* base;
        Expresion* power;
    public:
        Exponencial() {
            base = NULL;
            power = NULL;
        }
        ~Exponencial() {
            delete base;
            delete power;
        }
        double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

class RaizCuadrada : public Expresion{
    private:
        Expresion* param;
    public:
        RaizCuadrada() { param = NULL; }
        ~RaizCuadrada() { delete param; }
        double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

class Seno : public Expresion{
    private:
        Expresion* param;
    public:
        Seno() { param = NULL; }
        ~Seno() { delete param; }
        double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

class Coseno : public Expresion{
    private:
        Expresion* param;
    public:
        Coseno() { param = NULL; }
        ~Coseno() { delete param; } 
        double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

class Tangente : public Expresion{
    private:
        Expresion* param;
    public:
        Tangente() { param = NULL; }
        ~Tangente() { delete param; }
        double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

class LogNatural : public Expresion{
	private:
		Expresion* param;
	public:
		LogNatural() { param = NULL; }
		~LogNatural() { delete param; }
		double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

class Logaritmo : public Expresion{
	private:
		Expresion* base;
		Expresion* param;
	public:
		Logaritmo() { 
			base = NULL;
			param = NULL; 
		}
		~Logaritmo() { 
			delete base;
			delete param; 
		}
		double eval(double x);
        string toString(Expresion* input = NULL, int index = 0);
        void init(Funcion* func);
};

Expresion* Expresion::select(){  
    int sel;
    cout << "\t1)  Polinomio" << endl
         << "\t2)  Producto" << endl
         << "\t3)  Cociente" << endl
         << "\t4)  Exponencial" << endl
         << "\t5)  Raíz Cuadrada" << endl
         << "\t6)  Logaritmo Natural" << endl
         << "\t7)  Logaritmo (otra base)" << endl
         << "\t8)  Seno" << endl
         << "\t9)  Coseno" << endl
         << "\t10) Tangente" << endl
         << "\t11) Constante" << endl
         << "\t12) Variable (x)" << endl << endl
         << "Tu selección: ";
    cin >> sel;
    switch(sel){
        case 1:
            return new Polinomio;
        case 2:
            return new Producto;
        case 3:
            return new Cociente;
        case 4:
            return new Exponencial;
        case 5:
            return new RaizCuadrada;
        case 6:
            return new LogNatural;
        case 7:
            return new Logaritmo;
        case 8:
            return new Seno;
        case 9:
            return new Coseno;
        case 10:
            return new Tangente;
        case 11:
            return new Constante;
        case 12:
            return new Variable;
    }
}

double Funcion::eval(double x) { return expr->eval(x); }
void Funcion::print(Expresion* input, int index) { 
    cout << "-------------------------------------" << endl;
    if (input != NULL)
        cout << "Editando la expresión indicada con '___':";
    else
        cout << "Tu función es la siguiente:";
    cout << "\n\tf(x) = " << expr->toString(input, index) << endl; 
}
void Funcion::init() {
    expr = new Polinomio;
    cout << "Empecemos a definir su función." << endl;
    expr->init(this);
}

double Producto::eval(double x){
    double result = 1.0;
    int size = factores.size();
    for (int i = 0; i < size; i++)
    	result *= factores[i]->eval(x);
    return result;
}
string Producto::toString(Expresion* input, int index) {
    string output = "";
    string emptySeparator = "(";
    string separator = ")*(";
    string* sep = &emptySeparator;
    int size = factores.size();
    for (int i = 0; i < size; i++){
        output += *sep;
        if(factores[i] != NULL)
            output += factores[i]->toString(input, index);
        else if (input == this && index == i)
            output += "___";
        sep = &separator;
    }
    output += ")";
    if(index == -1 && input == this)
        output += "*(___)";
    return output;
}
void Producto::init(Funcion* func){
    int i = 2;
    int cont = true;
    factores.push_back(NULL);
    factores.push_back(NULL);
    func->print(this, 0);
    factores[0] = select();
    factores[0]->init(func);
    func->print(this, 1);
    factores[1] = select();
    factores[1]->init(func);
    do{
        func->print(this, -1);
        cout << "¿Desea agregar otro factor al producto?" << endl
             << "\t0) No" << endl
             << "\t1) Si" << endl << endl
             << "Tu selección: ";
        cin >> cont;
        if(cont){
            factores.push_back(NULL);
            func->print(this, i);
            factores[i] = select();
            factores[i]->init(func);
        }
        i++;
    } while (cont);
}


double Cociente::eval(double x) {
    return dividendo->eval(x) / divisor->eval(x);
}
string Cociente::toString(Expresion* input, int index){
    string output = "(";
    if(dividendo != NULL)
        output += dividendo->toString(input, index);
    else if (input == this && index == 0)
        output += "___";
    output += ")/(";
    if(divisor != NULL)
        output += divisor->toString(input, index);
    else if (input == this && index == 1)
        output += "___";
    output += ")";
    return output;
}
void Cociente::init(Funcion* func){
    func->print(this, 0);
    dividendo = select();
    dividendo->init(func);

    func->print(this, 1);
    divisor = select();
    divisor->init(func);
}


double Polinomio::eval(double x) {
    double result = 0;
    int size = terminos.size();
    for(int i = 0; i < size; i++)
        result += terminos[i]->eval(x);
    return result;
}
string Polinomio::toString(Expresion* input, int index){
    string output = "";
    string emptySeparator = "";
    string separator = " + ";
    string* sep = &emptySeparator;
    int size = terminos.size();
    for(int i = 0; i < size; i++){
        output += *sep;
        if (terminos[i] != NULL)
            output += terminos[i]->toString(input, index);
        else if (input == this)
            output += "___";
        sep = &separator;
    }
    if(index == -1 && input == this)
        output += " + (___)";
    return output;
}
void Polinomio::init(Funcion* func) {
    int i = 0;
    int cont = true;
    do{
        terminos.push_back(NULL);
        func->print(this, i);
        terminos[i] = select();
        terminos[i]->init(func);

        func->print(this, -1);
        cout << "¿Desea agregar otro término al polinomio?" << endl
             << "\t0) No" << endl
             << "\t1) Si" << endl << endl
             << "Tu selección: ";
        cin >> cont;
        i++;
    } while (cont);
}


double Constante::eval(double x){
    return value;
}
string Constante::toString(Expresion* input, int index){
    if(input == this)
        return "___";
    ostringstream stream;
    stream << fixed << setprecision(2) << value;
    return stream.str();
}
void Constante::init(Funcion* func){
    func->print(this);
    cout << "Ingrese el valor de su constante: ";
    cin >> value;
}


double Exponencial::eval(double x){
    return pow(base->eval(x), power->eval(x)); 
}
string Exponencial::toString(Expresion* input, int index){
    string output = "(";
    if (base != NULL)
        output += base->toString(input, index);
    else if (input == this && index == 0) 
        output += "___";

    output += ")^(";
    if (power != NULL) 
        output += power->toString(input, index);
    else if (input == this && index == 1)
        output += "___";
    output += ")";
    return output;
}
void Exponencial::init(Funcion* func){
    func->print(this, 0);
    base = select();
    base->init(func);

    func->print(this, 1);
    power = select();
    power->init(func);
}


double RaizCuadrada::eval(double x){
    return sqrt(param->eval(x));
}
string RaizCuadrada::toString(Expresion* input, int index){
    string output = "sqrt(";
    if (param != NULL)
        output += param->toString(input, index);
    else if (input == this)
        output += "___";
    output += ")";
    return output;
}
void RaizCuadrada::init(Funcion* func) {
    func->print(this);
    param = select();
    param->init(func);
}


double Seno::eval(double x){
    return sin(param->eval(x));
}
string Seno::toString(Expresion* input, int index){
    string output = "sin(";
    if (param != NULL)
        output += param->toString(input, index);
    else if (input == this)
        output += "___";
    output += ")";
    return output;
}
void Seno::init(Funcion* func) {
    func->print(this);
    param = select();
    param->init(func);
}


double Coseno::eval(double x){
    return cos(param->eval(x));
}
string Coseno::toString(Expresion* input, int index){
    string output = "cos(";
    if (param != NULL)
        output += param->toString(input, index);
    else if (input == this)
        output += "___";
    output += ")";
    return output;
}
void Coseno::init(Funcion* func){
    func->print(this);
    param = select();
    param->init(func);
}

double Tangente::eval(double x){
    return tan(param->eval(x));
}
string Tangente::toString(Expresion* input, int index){
    string output = "tan(";
    if (param != NULL)
        output += param->toString(input, index);
    else if(input == this)
        output += "___";
    output += ")";
    return output;
}
void Tangente::init(Funcion* func){
    func->print(this);
    param = select();
    param->init(func);
}


double LogNatural::eval(double x){
	return log(param->eval(x));
}
string LogNatural::toString(Expresion* input, int index){
	string output = "ln(";
	if (param != NULL)
		output += param->toString(input, index);
	else if (input == this)
		output+= "___";
	output += ")";
	return output;
}
void LogNatural::init(Funcion* func){
	func->print(this);
	param = select();
	param->init(func);
}

double Logaritmo::eval(double x){
	return log(param->eval(x)) / log(base->eval(x));
}
string Logaritmo::toString(Expresion* input, int index){
	string output = "log((";
	if(base != NULL)
		output += base->toString(input, index);
	else if (input == this && index == 0)
		output += "___";
	output += "),(";
	if (param != NULL)
		output += param->toString(input, index);
	else if (input == this && index == 1)
		output+= "___";
	output += "))";
	return output;
}
void Logaritmo::init(Funcion* func){
	func->print(this, 0);
	base = select();
	base->init(func);

	func->print(this, 1);
	param = select();
	param->init(func);
}

double Funcion::trapecio(double a, double b, int n){
    double h = (b - a) / n;
    double sol = 0;
    sol += eval(a);
    for(int i = 1; i < n; i++)
        sol += 2 * eval( a + i * h );
    sol += eval(n);
    sol *= h / 2;
    return sol;
}

double Funcion::simpson13(double a, double b, int n){
    double h = (b - a) / n;
    double sol = 0;
    sol += eval(a);
    for(int i = 1; i < n; i++)
        sol += (i%2 ? 4 : 2) * eval( a + i * h );
    sol += eval(n);
    sol *= h / 3;
    return sol;
}

double Funcion::simpson38(double a, double b){
    double h = (b - a) / 3;
    double sol = 0;
    sol += eval(a) + eval(b);
    sol += 3 * (eval(a + h) + eval(b - h));
    sol *= (b - a) / 8;
    return sol;
}

double Funcion::simpson(double a, double b, int n){
    double sol;
    double h = (b - a) / n ;
    // Por el momento hace puro S-1/3 o un S-3/8 y el resto S-1/3
    if(n % 2)
        sol = simpson13(a, b - 3 * h, n-3) + simpson38(b - 3 * h, b);
    else
        sol = simpson13(a, b, n);
    return sol;
}
