# AppiumEnhanceLibrary for robotframework

## Introduction

___

  Bring back the missing keywords from [Selenium2Library](https://github.com/robotframework/Selenium2Library)  to [AppiumLibrary](https://github.com/jollychang/robotframework-appiumlibrary).

  It depends on [AppiumLibrary](https://github.com/jollychang/robotframework-appiumlibrary) and use [active library instance](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#extending-existing-test-libraries) to enhance robotframework-appiumlibrary.

## Installation

---

 Robotframework-appiumlibrary should be installed first. And just put this library in your project. And link a reference for it.

    *** Settings ***
    Libraries    AppiumEnhanceLibrary.py


## Keywords

---

| Keyword            | Arguments  |         |              |            |
| ------------------ | -----------| --------|--------------|------------|
| Execute Javascript | code       |
| Wait Until Element Is Visible   | locator | timeout=None | error=None |
| Wait Until Element Is Not Visible | locator | timeout=None  | error=None |
| Element Should Be Visible | locator | message='' |    |
| Element Should Not Be Bisible | locator | message='' |
| Wait Until Element Contains | locator | text | timeout=None | error=None |
| Wait Until Element Does Not Contain | locator | text | timeout=None | error=None |
| Page Should Contain | text |
| Page Should Not Contain | text |
| Wait For Condition | condition | timeout=None | error=None |
| Get Horizontal Position | locator |
| Get Vertical Position | locator |
| Get Value | locator |
| Get Text | locator |
| Mouse Down At | locator | xoffset | yoffset |
| Mouse Up At | locator | xoffset | yoffset |
| Drag And Drop By Offset | locator | xoffset | yoffset |
| Get Matching Xpath Count | xpath |
| Select Frame | locator |
| Unselect Frame | locator |

## Contributing

---

Fork the project, make a change, and send a pull request!


*Written by: Scen.Kang*
