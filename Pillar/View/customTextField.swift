//
//  customTextField.swift
//  Pillar
//
//  Created by Kadeem Palacios on 4/28/18.
//  Copyright © 2018 Kadeem Palacios. All rights reserved.
//

import UIKit

class CustomTextField: UITextField {

    private var padding = UIEdgeInsets(top: 0, left: 0, bottom: 0, right: 0)

    override func awakeFromNib() {
        let placeholder = NSAttributedString(string: self.placeholder!, attributes: [NSAttributedStringKey.foregroundColor: #colorLiteral(red: 1, green: 1, blue: 1, alpha: 1)])
        self.layer.borderColor = UIColor(red: 41/255, green: 195/255, blue: 211/255, alpha: 0).cgColor
//            UIColor(displayP3Red: 41/255, green: 195/255, blue: 211/255, alpha: 0) as! CGColor
        self.layer.backgroundColor = UIColor(red: 0, green: 0, blue: 0, alpha: 0).cgColor
        self.attributedPlaceholder = placeholder
        super.awakeFromNib()
    }

    override func textRect(forBounds bounds: CGRect) -> CGRect {
        return UIEdgeInsetsInsetRect(bounds, padding)
    }

    override func editingRect(forBounds bounds: CGRect) -> CGRect {
        return UIEdgeInsetsInsetRect(bounds, padding)
    }

    override func placeholderRect(forBounds bounds: CGRect) -> CGRect {
        return UIEdgeInsetsInsetRect(bounds, padding)
    }

}
