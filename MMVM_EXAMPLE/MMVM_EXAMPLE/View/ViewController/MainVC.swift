//
//  ViewController.swift
//  MMVM_EXAMPLE
//
//  Created by 김은상 on 7/14/24.
//

import UIKit

protocol MainViewDelegate: AnyObject {
    func getDivisorButtonDidTapped(num: Int)
}

final class MainVC: UIViewController {
    //MARK: - Properties
    private let mainView = MainView()
    
    var divisorViewModel: DivisorViewModel!

    //MARK: - LifeCycle
    override func loadView() {
        mainView.mainViewDelegate = self
        self.view = mainView
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        self.divisorViewModel = DivisorViewModel()
        self.view.backgroundColor = .white
    }
}
//MARK: - Extensions
extension MainVC: MainViewDelegate {
    func getDivisorButtonDidTapped(num: Int) {
        self.divisorViewModel.setDivisor(with: num)
        
        //mainView가 소유한 divisorViewModel에 현재 divisorViewModel을 전달
        self.mainView.divisorViewModel = self.divisorViewModel
    }
}
