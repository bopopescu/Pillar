//
//  LoginStep1VC.swift
//  Pillar
//
//  Created by Kadeem Palacios on 4/28/18.
//  Copyright © 2018 Kadeem Palacios. All rights reserved.
//

import UIKit

class LoginStep1VC: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var firstNamefield: CustomTextField!
    @IBOutlet weak var emailField: CustomTextField!
    @IBOutlet weak var lastNameField: CustomTextField!
    override func viewDidLoad() {
        super.viewDidLoad()
        firstNamefield.delegate = self
        emailField.delegate = self
        lastNameField.delegate = self
        NotificationCenter.default.addObserver(self, selector: #selector(LoginStep1VC.keyboardWillShow), name: NSNotification.Name.UIKeyboardWillShow, object: nil)
        NotificationCenter.default.addObserver(self, selector: #selector(LoginStep1VC.keyboardWillHide), name: NSNotification.Name.UIKeyboardWillHide, object: nil)
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


    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
