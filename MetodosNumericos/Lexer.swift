//
//  Lexer.swift
//  MetodosNumericos
//
//  Created by Osmar Hernández on 24/04/18.
//  Copyright © 2018 itesm. All rights reserved.
//

import Foundation

class Lexer {
    enum Error: Swift.Error {
        case invalidCharacter(Character)
    }
    
    private let input: String
    private var position: String.Index
    
    init(input: String) {
        self.input = input
        self.position = self.input.startIndex
    }
    
    private func peekNextCharacter() -> Character? {
        guard position < input.endIndex else {
            return nil
        }
        return input[position]
    }
    
    private func advancePosition() {
        position = input.index(after: position)
    }
    
    private func getNumber() -> Int {
        var value = 0
        
        while let nextCharacter = peekNextCharacter() {
            switch nextCharacter {
            case "0"..."9":
                let digitValue = Int(String(nextCharacter))!
                value = 10 * value + digitValue
                advancePosition()
            default:
                return value
            }
        }
        return value
    }
    
    public func lex() throws -> [Token] {
        var tokens: [Token] = []
        
        while let nextCharacter = peekNextCharacter() {
            switch nextCharacter {
            case "0"..."9":
                let value = getNumber()
                tokens.append(.number(value))
            case "+":
                tokens.append(.plus)
                advancePosition()
            case "-":
                tokens.append(.minus)
                advancePosition()
            case "*":
                tokens.append(.multiply)
                advancePosition()
            case "^":
                tokens.append(.base)
                advancePosition()
            case " ":
                advancePosition()
            default:
                throw Error.invalidCharacter(nextCharacter)
            }
        }
        
        return tokens
    }
}
