/*
2022.11.9 Today, I Learned
ABOUT Navigation Conrtroller
*/


// there are typically 3 options to change ViewController

//First, I can change the "view" of ViewController, but it can cause memory overflow. (Not encouraged)
//Second, call another ViewController on current ViewController
//Third, Using NavigationController (push)




// I used navigation controller

    @IBAction func nextViewController(_ sender: UIButton) {
        guard let nextVC = self.storyboard?.instantiateViewController(withIdentifier: "BViewController") else {return}
        self.navigationController?.pushViewController(nextVC, animated: true)
    }
    
