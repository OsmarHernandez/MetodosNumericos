//
//  Parser.swift
//  MetodosNumericos
//
//  Created by Osmar Hernández on 24/04/18.
//  Copyright © 2018 itesm. All rights reserved.
//

import Foundation

class Parser {
    enum Error: Swift.Error {
        case unexpectedEndOfInput
        case invalidToken(Token)
    }
    
    private let tokens: [Token]
    private var position = 0
    
    init(tokens: [Token]) {
        self.tokens = tokens
    }
    
    private func getNextToken() -> Token? {
        guard position < tokens.count else {
            return nil
        }
        let token = tokens[position]
        position += 1
        return token
    }
    
    private func getNumber() throws -> Int {
        guard let token = getNextToken() else {
            throw Error.unexpectedEndOfInput
        }
        
        switch token {
        case .number(let value):
            return value
        default:
            throw Error.invalidToken(token)
        }
    }
    
    private func baseToken(_ position: Int) -> Bool {
        let i = position < tokens.count ? position : 0
        let token = tokens[i]
        
        switch token {
        case .base:
            return true
        default:
            return false
        }
    }
    
    public func parse() throws -> Int {
        var value = try getNumber()
        
        while let token = getNextToken() {
            switch token {
            case .plus:
                let nextNumber = try parse()
                value += nextNumber
            case .multiply:
                let nextNumber = baseToken(position + 1) ? try parse() : try getNumber()
                value *= nextNumber
                case .base:
                let nextNumber = try getNumber()
                value = Int(pow(Double(value), Double(nextNumber)))
            case .number:
                throw Error.invalidToken(token)
            default:
                print("TODO: implement functionallity")
            }
        }
        
        return value
    }
}
