#include <iostream>
#include <fstream>
#include <vector>;
#include "../includes/Evaluables.h"
using namespace std;

/*
	La clase FParser provee la funcionalidad necesaria para serializar objetos
	de la clase Funcion y crear objetos Funcion a partir de strings serializados,
	asi como leer y escribir estos strings en archivos para poder guardar objectos
	Funcion en memoria persistente.
*/
class FParser {
	public:
		// Constructor y destructor
		FParser(){}
		~FParser(){}

		// 
		Funcion* parse(string in);
		void parseAll(ifstream &file, vector<Funcion*> mem);
		string serialize(Funcion* fun);
	private:
		Expresion* hold[5];
};