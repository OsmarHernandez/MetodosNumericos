#include <iostream>

MenuBase::MenuBase() {
    sText = "Texto por default.";
    sDivider = "-------------\n\n-------------";
}

MenuBase::~MenuBase() {}

inline void MenuBase::print() {
    cout << sDivider << endl 
    	 << sText << endl
    	 << "Tu selección: "; 
}
