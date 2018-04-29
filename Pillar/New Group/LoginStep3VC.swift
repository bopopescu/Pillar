//
//  LoginStep3VC.swift
//  Pillar
//
//  Created by Kadeem Palacios on 4/28/18.
//  Copyright © 2018 Kadeem Palacios. All rights reserved.
//

import UIKit

class LoginStep3VC: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var creditCardField: CustomTextField!
    override func viewDidLoad() {
        super.viewDidLoad()
        creditCardField.delegate = self
        NotificationCenter.default.addObserver(self, selector: #selector(LoginStep3VC.keyboardWillShow), name: NSNotification.Name.UIKeyboardWillShow, object: nil)
        NotificationCenter.default.addObserver(self, selector: #selector(LoginStep3VC.keyboardWillHide), name: NSNotification.Name.UIKeyboardWillHide, object: nil)
        // Do any additional setup after loading the view.
    }



@objc func keyboardWillShow(notification: NSNotification) {
    if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {
        if self.view.frame.origin.y == 0{
            self.view.frame.origin.y -= keyboardSize.height
        }
    }
}

@objc func keyboardWillHide(notification: NSNotification) {
    if let keyboardSize = (notification.userInfo?[UIKeyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {
        if self.view.frame.origin.y != 0{
            self.view.frame.origin.y += keyboardSize.height
        }
    }
}
    @IBAction func screenTapped(_ sender: Any) {
        self.resignFirstResponder()
        print("tapped")
    }

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
