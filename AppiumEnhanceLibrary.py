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

    def wait_until_element_is_visible(self, locator, timeout=None, error=None):
        """Wait until element specified with `locator` is visible.

        Fails if `timeout` expires before the element is visible. See
        `introduction` for more information about `timeout` and its
        default value.

        `error` can be used to override the default error message.

        See also `Wait Until Page Contains`, `Wait Until Page Contains
        Element`, `Wait For Condition`.
        """
        def check_visibility():
            visible = self._is_visible(locator)
            if visible:
                return
            elif visible is None:
                return error or "Element locator '%s' did not match any " \
                                "elements after %s" % \
                                (locator, self.apu._format_timeout(timeout))
            else:
                return error or "Element '%s' was not visible in %s" % \
                                (locator, self.apu._format_timeout(timeout))
        self.apu._wait_until_no_error(timeout, check_visibility)

    def wait_until_element_is_not_visible(self, locator, timeout=None,
                                          error=None):
        """Wait until element specified with `locator` is not visible.

        Fails if `timeout` expires before the element is not visible. See
        `introduction` for more information about `timeout` and its
        default value.

        `error` can be used to override the default error message.

        See also `Wait Until Page Contains`, `Wait Until Page Contains
        Element`, `Wait For Condition`.
        """
        def check_hidden():
            visible = self._is_visible(locator)
            if not visible:
                return
            elif visible is None:
                return error or "Element locator '%s' did not match any " \
                                "elements after %s" % \
                                (locator, self.apu._format_timeout(timeout))
            else:
                return error or "Element '%s' was still visible in %s" % \
                                (locator, self.apu._format_timeout(timeout))
        self.apu._wait_until_no_error(timeout, check_hidden)

    # Private

    def _is_visible(self, locator):
        element = self.apu._element_find(locator, True, False)
        if element is not None:
            return element.is_displayed()
        return None
