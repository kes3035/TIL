//
//  ViewController.swift
//  MVC_EXAMPLE
//
//  Created by 김은상 on 7/7/24.
//

import UIKit

protocol MainViewDelegate: AnyObject {
    func getDivisorsWithNum(_ num: Int)
}

final class MainVC: UIViewController {
    //MARK: - Properties
    private let mainView = MainView()

    private var divisor: Divisor? {
        didSet {
            guard let divisor = self.divisor else { return }
            mainView.configureMainViewUIWithData(divisor: divisor)
        }
    }
    //MARK: - LifeCycle
    override func loadView() {
        mainView.mainViewDelegate = self
        self.view = mainView
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        self.view.backgroundColor = .white
    }
}
//MARK: - Extensions
extension MainVC: MainViewDelegate {
    func getDivisorsWithNum(_ num: Int) {
        var divisors: [Int] = []
        for i in 1...num {
            if num%i == 0 {
                divisors.append(i)
            }
        }
        let count = divisors.count
        
        self.divisor = Divisor(number: num, divisors: divisors, countOfDivisor: count)
    }
}
