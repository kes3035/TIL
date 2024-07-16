//
//  MainView.swift
//  MMVM_EXAMPLE
//
//  Created by 김은상 on 7/15/24.
//

import UIKit

final class MainView: UIView {
    //MARK: - Properties
    private lazy var titleLabel: UILabel = {
        let label = UILabel()
        label.translatesAutoresizingMaskIntoConstraints = false
        label.text = "정수 구하기"
        label.font = UIFont.boldSystemFont(ofSize: 30)
        label.textColor = UIColor.black
        label.textAlignment = .center
        return label
    }()
    
    private lazy var numTextField: UITextField = {
        let textField = UITextField()
        textField.placeholder = "숫자를 입력하세요"
        textField.backgroundColor = .white
        textField.layer.borderColor = UIColor.black.cgColor
        textField.layer.borderWidth = 1
        textField.keyboardType = .numberPad
        textField.returnKeyType = .done
        textField.delegate = self
        textField.translatesAutoresizingMaskIntoConstraints = false
        return textField
    }()
    
    private lazy var getDivisorButton: UIButton = {
       let button = UIButton()
        button.translatesAutoresizingMaskIntoConstraints = false
        button.setTitle("확인", for: .normal)
        button.backgroundColor = .systemBlue
        button.layer.cornerRadius = 8
        button.clipsToBounds = true
        button.setTitleColor(UIColor.white, for: .normal)
        button.addTarget(self, action: #selector(getDivisorButtonTapped), for: .touchUpInside)
        return button
    }()
    
    private lazy var countOfDivisorsLabel: UILabel = {
        let label = UILabel()
        label.text = "약수의 갯수가 표시됩니다."
        label.translatesAutoresizingMaskIntoConstraints = false
        label.textAlignment = .left
        label.textColor = .black
        label.numberOfLines = 0
        label.font = UIFont.systemFont(ofSize: 16)
        return label
    }()
    
    private lazy var divisorsLabel: UILabel = {
        let label = UILabel()
        label.text = "약수들이 표시됩니다."
        label.translatesAutoresizingMaskIntoConstraints = false
        label.textAlignment = .left
        label.textColor = .black
        label.font = UIFont.systemFont(ofSize: 16)
        return label
    }()
    
    weak var mainViewDelegate: MainViewDelegate?
    
    // ⭐️⭐️⭐️뷰가 뷰모델을 소유⭐️⭐️⭐️
    var divisorViewModel: DivisorViewModel! {
        didSet {
            self.configureMainViewUIWithData()
        }
    }
    
    //MARK: - LifeCycle
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.divisorViewModel = DivisorViewModel()
        self.configureMainViewUI()
    }
    
    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }
    //MARK: - Helpers
    private func configureMainViewUIWithData() {
        guard let divisor = self.divisorViewModel.getDivisorModel() else { return }
        let divisors = divisor.divisors.map{String($0)}
        var textDivisors: String = ""
        for str in divisors {
            let text = str + ", "
            textDivisors += text
        }
        DispatchQueue.main.async {
            self.countOfDivisorsLabel.text = "약수의 갯수는 : \(divisor.countOfDivisor)개"
            self.divisorsLabel.text = textDivisors
        }
    }
    //MARK: - Actions
    @objc func getDivisorButtonTapped() {
        //유저가 직접 버튼을 터치했을 때(액션) 뷰가 컨트롤러에 업데이트
        guard let str = self.numTextField.text,
              let num = Int(str) else { return }
        self.mainViewDelegate?.getDivisorButtonDidTapped(num: num)
    }
}

extension MainView: UITextFieldDelegate {
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, 
                                             replacementString string: String) -> Bool {
        // 숫자만 && 글자수 제한
        guard Int(string) != nil || string == "" else { return false }
        guard textField.text!.count < 4 else { return false }
        
        return true
    }
}
extension MainView {
    private func configureMainViewUI() {
        self.backgroundColor = .white

        [titleLabel, numTextField, getDivisorButton,
         divisorsLabel, countOfDivisorsLabel].forEach { self.addSubview($0) }
        
        NSLayoutConstraint.activate([
            self.titleLabel.centerXAnchor.constraint(equalTo: self.centerXAnchor),
            self.titleLabel.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 50),
            self.titleLabel.widthAnchor.constraint(equalToConstant: 200),
            self.titleLabel.heightAnchor.constraint(equalToConstant: 50)
        ])
        
        NSLayoutConstraint.activate([
            self.countOfDivisorsLabel.centerXAnchor.constraint(equalTo: self.centerXAnchor),
            self.countOfDivisorsLabel.topAnchor.constraint(equalTo: titleLabel.bottomAnchor, constant: 30),
            self.countOfDivisorsLabel.widthAnchor.constraint(equalToConstant: 250),
            self.countOfDivisorsLabel.heightAnchor.constraint(equalToConstant: 30)
        
        ])
        
        NSLayoutConstraint.activate([
            self.divisorsLabel.centerXAnchor.constraint(equalTo: self.centerXAnchor),
            self.divisorsLabel.topAnchor.constraint(equalTo: countOfDivisorsLabel.bottomAnchor, constant: 30),
            self.divisorsLabel.widthAnchor.constraint(equalToConstant: 250),
            self.divisorsLabel.heightAnchor.constraint(equalToConstant: 120)
        
        ])
        
        NSLayoutConstraint.activate([
            self.numTextField.centerXAnchor.constraint(equalTo: self.centerXAnchor),
            self.numTextField.centerYAnchor.constraint(equalTo: self.centerYAnchor),
            self.numTextField.widthAnchor.constraint(equalToConstant: 250),
            self.numTextField.heightAnchor.constraint(equalToConstant: 50)
        ])
        
        NSLayoutConstraint.activate([
            self.getDivisorButton.centerXAnchor.constraint(equalTo: numTextField.centerXAnchor),
            self.getDivisorButton.topAnchor.constraint(equalTo: numTextField.bottomAnchor, constant: 10),
            self.getDivisorButton.widthAnchor.constraint(equalToConstant: 100),
            self.getDivisorButton.heightAnchor.constraint(equalToConstant: 30)
        ])
    }
}
