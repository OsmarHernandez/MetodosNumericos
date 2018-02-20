#include "Evaluables.h"

int main(void){
    Funcion func;
    func.init();
    func.print();
    cout <<	"Tu funcion evaluada en 10 es: "
    	 << func.eval(10) << endl;

    return 0;
}
