#include "Menus.h"

MenuRaiz::MenuRaiz() {
    sText = "Menu Principal.\n"
          + "\t1) Ver mis funciones\n"
          + "\t2) Ver mis matrices\n"
          + "\t3) Usar método numérico\n"
          + "\t4) Salir\n\n"
          + "Selección: ";
}

MenuRaiz::~MenuRaiz() {}

BaseMenu* getNextMenu(int iSelection, bool *bSalir) {
    BaseMenu* 

    switch (iSelection) {
        case 1:
            return new MenuFunciones;
        case 2:
            return new MenuMatrices;
        case 3:
            return new MenuMetodos;
        case 4:
            return new Menu
    }
}


