//
//  divisorViewModel.swift
//  MMVM_EXAMPLE
//
//  Created by 김은상 on 7/14/24.
//

import UIKit

final class DivisorViewModel {
    //MARK: - Model
    private var divisor: Divisor?
    //MARK: - Setter
    func setDivisor(with num: Int) {
        let num = num
        let countOfDivisor = self.getDivisorCountOfNum(with: num)
        let divisors = self.getDivisorsOfNum(with: num)
        
        self.divisor = Divisor(number: num, divisors: divisors, countOfDivisor: countOfDivisor)
    }
    //MARK: - Getter
    func getDivisorModel() -> Divisor? {
        return self.divisor
    }
    
    private func getDivisorsOfNum(with num: Int) -> [Int] {
        var divisors: [Int] = []
        for i in 1...num {
            if num%i == 0 {
                divisors.append(i)
            }
        }
        return divisors
    }
    
    private func getDivisorCountOfNum(with num: Int) -> Int {
        var countOfDivisor: Int = 0
        for i in 1...num {
            if num%i == 0 {
                countOfDivisor += 1
            }
        }
        return countOfDivisor
    }
}
