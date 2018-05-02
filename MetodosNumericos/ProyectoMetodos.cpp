#include "Evaluables.h"

int main(void){
    int metodo, n;
    double a, b;
    Funcion func;
    func.init();
    func.print();
    cout << "a: ";
    cin >> a;
    cout << "b: ";
    cin >> b;
    cout << "n: ";
    cin >> n;
    cout <<	"Selecciona un metodo: " << endl
         << "\t1) Trapecio" << endl
         << "\t2) Simpson" << endl;
    cin >> metodo;
    switch(metodo){
        case 1:
            cout << func.trapecio(a, b, n);
            break;
        case 2:
            cout << func.simpson(a, b, n);
            break;
    }
    cout << endl;

    return 0;
}
