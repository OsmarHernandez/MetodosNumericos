#include <iostream>
using namespace std;

class MenuBase {
    public: 
        MenuBase();
        virtual ~MenuBase();
        virtual BaseMenu* getNextMenu(int iSelection, bool *bSalir) = 0;
        virtual void print();
    protected:
        string sText;
        string sDivider;
};

class MenuRaiz : public MenuBase {
    MenuRaiz();
    ~MenuRaiz();
    BaseMenu* getNextMenu(int iSelection, bool *bSalir);
};

class MenuFunciones : public MenuBase {
    MenuFunciones();
    ~MenuFunciones();
    BaseMenu* getNextMenu(int iSelection, bool *bSalir);
    void print();
};

class MenuMatrices : public MenuBase {
    MenuMatrices();
    ~MenuMatrices();
    BaseMenu* getNextMenu(int iSelection, bool *bSalir);
    void print();
};

class MenuMetodos : public MenuBase {
    MenuMetodos();
    ~MenuMetodos();
    BaseMenu* getNextMenu(int iSelection *bSalir);
    void print();
}
