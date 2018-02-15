//
//  main.cpp
//  MetodosNumericos
//
//  Created by Osmar Hernández on 14/02/18.
//  Copyright © 2018 itesm. All rights reserved.
//

#include <iostream>
using namespace std;

bool exit(bool run) {
    cout << "Salir\n";
    return !run;
}

int getInput() {
    int choice;
    cin >> choice;
    return choice;
}

void DisplayMenu() {
    cout << "Selecciona mediante el numero del índice\n";
    cout << "alguna de las siguientes opciones:\n";
    cout << "1. Regla del Trapecio\n";
    cout << "2. Simpson 1/3\n";
    cout << "3. Simpson 3/8\n";
    cout << "4. Salir\n";
    cout << "========================================\n";
}

int main(int argc, const char * argv[]) {
    bool run = true;
    int choice = 0;
    
    while (run) {
        DisplayMenu();
        choice = getInput();
        
        switch (choice) {
            case 1:
                cout << "Regla del Trapecio\n";
                break;
            case 2:
                cout << "Simpson 1/3\n";
                break;
            case 3:
                cout << "Simpson 3/8\n";
                break;
            case 4:
                run = exit(run);
                break;
                
            default:
                break;
        }
    }
    
    return EXIT_SUCCESS;
}
