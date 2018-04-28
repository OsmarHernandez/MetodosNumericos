//
//  main.swift
//  MetodosNumericos
//
//  Created by Osmar Hernández on 24/04/18.
//  Copyright © 2018 itesm. All rights reserved.
//

import Foundation

func evaluate(input: String) {
    print("Evaluating: \(input)")
    let lexer = Lexer.init(input: input)

    do {
        let tokens = try lexer.lex()
        print("Lexer output: \(tokens)")

        let parser = Parser(tokens: tokens)
        let result = try parser.parse()
        print("Parser output: \(result)")
    } catch Lexer.Error.invalidCharacter(let character) {
        print("Input contained an invalid character: \(character)")
    } catch Parser.Error.unexpectedEndOfInput {
        print("Unexpected end of input during parsing")
    } catch Parser.Error.invalidToken(let token) {
        print("Invalid token during parsing: \(token)")
    } catch {
        print("An error ocurred: \(error)")
    }
}

evaluate(input: "10*3 + 4*3")
print()
evaluate(input: "3^2 * 2")
print()
evaluate(input: "90 + 3^2")
print()
evaluate(input: "90 + 3 * 4 * 3^2")
print()
evaluate(input: "90 + 343 * 2 + 190")

//var presedenceFlag = false
//
//presedenceFlag = true
//
//let string = presedenceFlag ? "true" : "false"
//print(string)

