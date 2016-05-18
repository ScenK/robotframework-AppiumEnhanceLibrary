# -*- coding: utf-8 -*-
"""AppiumEnhanceLibrary is the enhancement of robotframework-appiumlibrary.

It will bring back these missing keywords from robotframework selenium2library.

Detail imformation could be found on github.com:
    https://github.com/ScenK/robotframework-AppiumEnhanceLibrary
"""
from robot.libraries.BuiltIn import BuiltIn


class AppiumEnhanceLibrary(object):
    """AppiumEnhanceLibrary for supporting actions that not included in RF.

    Support more keywords for AppiumLibrary.

    Detail imformation about AppiumLibrary could be found on github.com:
        https://github.com/jollychang/robotframework-appiumlibrary
    """

    def __init__(self):
        """Init function.

        Load and store configs in to variables.
        """
        super(AppiumEnhanceLibrary, self).__init__()
        self.apu = BuiltIn().get_library_instance('AppiumLibrary')

    def execute_javascript(self, code):
        """Execute the given JavaScript code.

        `code` may contain multiple lines of code and may be divided into
        multiple cells in the test data. In that case, the parts are
        catenated together without adding spaces.

        The JavaScript executes in the context of the currently selected
        frame or window as the body of an anonymous function. Use _window_ to
        refer to the window of your application and _document_ to refer to the
        document object of the current frame or window, e.g.
        _document.getElementById('foo')_.

        This keyword returns None unless there is a return statement in the
        JavaScript. Return values are converted to the appropriate type in
        Python, including WebElements.

        Examples:
        | Execute JavaScript | window.my_js('arg1', 'arg2') |               |
        | ${sum}=            | Execute JavaScript           | return 1 + 1; |
        | Should Be Equal    | ${sum}                       | ${2}          |
        """
        driver = self.apu._current_application()
        return driver.execute_script(code)
