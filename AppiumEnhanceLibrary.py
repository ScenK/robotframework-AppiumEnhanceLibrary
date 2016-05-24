# -*- coding: utf-8 -*-
"""AppiumEnhanceLibrary is the enhancement of robotframework-appiumlibrary.

It will bring back these missing keywords from robotframework selenium2library.

Detail imformation could be found on github.com:
    https://github.com/ScenK/robotframework-AppiumEnhanceLibrary
"""
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
from AppiumLibrary.locators.elementfinder import ElementFinder


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

        Examples:libraries/AppiumEnhanceLibrary.py
uLiu
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

    def element_should_be_visible(self, locator, message=''):
        """Verify that the element identified by `locator` is visible.

        Herein, visible means that the element is logically visible,
        not optically visible in the current browser viewport. For example,
        an element that carries display:none is not logically visible,
        so using this keyword on that element would fail.

        `message` can be used to override the default error message.

        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.
        """
        visible = self._is_visible(locator)
        if not visible:
            if not message:
                message = "The element '%s' should be visible, but it " \
                          "is not." % locator
            raise AssertionError(message)

    def element_should_not_be_visible(self, locator, message=''):
        """Verify that the element identified by `locator` is NOT visible.

        This is the opposite of `Element Should Be Visible`.

        `message` can be used to override the default error message.

        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.
        """
        visible = self._is_visible(locator)
        if visible:
            if not message:
                message = "The element '%s' should not be visible, " \
                          "but it is." % locator
            raise AssertionError(message)

    def wait_until_element_contains(self, locator, text, timeout=None,
                                    error=None):
        """Wait until given element contains `text`.

        Fails if `timeout` expires before the text appears on given element.
        See `introduction` for more information about `timeout` and its
        default value.

        `error` can be used to override the default error message.

        See also `Wait Until Page Contains`, `Wait Until Page Contains Element`
        , `Wait For Condition`, `Wait Until Element Is Visible`.
        """
        element = self.apu._element_find(locator, True, True)

        def check_text():
            actual = element.text
            if text in actual:
                return
            else:
                return error or "Text '%s' did not appear in %s to element " \
                                "'%s'. Its text was '%s'." \
                                % (text, self.apu._format_timeout(timeout),
                                   locator, actual)

        self.apu._wait_until_no_error(timeout, check_text)

    def wait_until_element_does_not_contain(self, locator, text,
                                            timeout=None, error=None):
        """Wait until given element does not contain `text`.

        Fails if `timeout` expires before the text disappears from given
        element. See `introduction` for more information about `timeout` and
        its default value.

        `error` can be used to override the default error message.

        See also `Wait Until Page Contains`, `Wait Until Page Contains Element`
        , `Wait For Condition`, `Wait Until Element Is Visible`.
        """
        element = self.apu._element_find(locator, True, True)

        def check_text():
            actual = element.text
            if text not in actual:
                return
            else:
                return error or "Text '%s' did not disappear in %s from " \
                                "element '%s'." % (text,
                                                   self.apu._format_timeout(
                                                       timeout), locator)

        self.apu._wait_until_no_error(timeout, check_text)

    def page_should_contain(self, text, loglevel):
        """Verify that current page contains `text`.

        If this keyword fails, it automatically logs the page source
        using the log level specified with the optional `loglevel` argument.
        Giving `NONE` as level disables logging.
        """
        self.apu.page_should_contain_text(self, text, loglevel=loglevel)

    def page_should_not_contain(self, text, loglevel):
        """Verify that current page not contains `text`.

        If this keyword fails, it automatically logs the page source
        using the log level specified with the optional `loglevel` argument.
        Giving `NONE` as level disables logging.
        """
        self.apu.page_should_not_contain_text(self, text, loglevel=loglevel)

    def wait_for_condition(self, condition, timeout=None, error=None):
        """Wait until the given `condition` is true or `timeout` expires.

        The `condition` can be arbitrary JavaScript expression but must contain
         a return statement (with the value to be returned) at the end.
        See `Execute JavaScript` for information about accessing the
        actual contents of the window through JavaScript.

        `error` can be used to override the default error message.

        See `introduction` for more information about `timeout` and its
        default value.

        See also `Wait Until Page Contains`, `Wait Until Page Contains
        Element`, `Wait Until Element Is Visible` and BuiltIn keyword
        `Wait Until Keyword Succeeds`.
        """
        if not error:
            error = "Condition '%s' did not become true in <TIMEOUT>" % \
                    condition
        self.apu._wait_until(timeout, error,
                             lambda: self.apu._current_application().
                             execute_script(condition) == True)

    def get_horizontal_position(self, locator):
        """Return horizontal position of element identified by `locator`.

        The position is returned in pixels off the left side of the page,
        as an integer. Fails if a matching element is not found.

        See also `Get Vertical Position`.
        """
        x = self.apu.get_element_location(locator)['x']
        return x

    def get_vertical_position(self, locator):
        """Return vertical position of element identified by `locator`.

        The position is returned in pixels off the left side of the page,
        as an integer. Fails if a matching element is not found.

        See also `Get Horizontal Position`.
        """
        y = self.apu.get_element_location(locator)['y']
        return y

    def get_value(self, locator):
        """Return the value attribute of element identified by `locator`.

        See `introduction` for details about locating elements.
        """
        return self.apu.get_element_attribute(locator, 'value')

    def get_text(self, locator):
        """Return the text value of element identified by `locator`.

        See `introduction` for details about locating elements.
        """
        return self._get_text(locator)

    def mouse_down_at(self, locator, xoffset, yoffset):
        """Support `mouse down at` for AppiumLibrary.

        Offsets are relative to the top-left corner of the element.

        Args:
         - locator: robot framework locator.
         - xoffset: X offset to start.
         - yoffset: Y offset to start.

        Examples:
        | Mouse Down At | id=canvas | 120 | 250 |
        """
        element = self.apu._element_find(locator, True, True)

        if element is None:
            raise AssertionError("ERROR: Element %s not found." % locator)

        ActionChains(self.apu._current_application()).\
            move_to_element_with_offset(element, xoffset, yoffset).\
            click_and_hold().perform()

    def mouse_up_at(self, locator, xoffset, yoffset):
        """Support `mouse up at` for Selenium2Library.

        Right now use click off-line button to end mouse behaviour.

        Offsets are relative to the top-left corner of the element.

        Args:
         - locator: robot framework locator.
         - xoffset: X offset to end.
         - yoffset: Y offset to end.

        Examples:
        | Mouse Up At | id=canvas | 320 | 830 |
        """
        element = self.apu._element_find(locator, True, True)

        if element is None:
            raise AssertionError("ERROR: Element %s not found." % locator)

        # The release() function here could not rightly performed. Use click
        # off-line button instead.
        ActionChains(self.apu._current_application()).\
            move_to_element_with_offset(element, 1, 1).\
            move_by_offset(xoffset, yoffset).click().perform()

    def drag_and_drop_by_offset(self, locator, xoffset, yoffset):
        """Drag element identified with locator.

        Element will be moved by xoffset and yoffset, each of which is a
        negative or positive number specify the offset.

        Examples:
        | Drag And Drop By Offset | myElem | 50 | -35 |
         # Move myElem 50px right and 35px down. |
        """
        element = self.apu._element_find(locator, True, True)

        if element is None:
            raise AssertionError("ERROR: Element %s not found." % locator)

        ActionChains(self.apu._current_application()).\
            drag_and_drop_by_offset(locator, xoffset, yoffset).perform()

    def get_matching_xpath_count(self, xpath):
        """Returns number of elements matching `xpath`

        One should not use the xpath= prefix for 'xpath'. XPath is assumed.

        Correct:
        | count = | Get Matching Xpath Count | //div[@id='sales-pop']
        Incorrect:
        | count = | Get Matching Xpath Count | xpath=//div[@id='sales-pop']

        If you wish to assert the number of matching elements, use
        `Xpath Should Match X Times`.
        """
        count = len(self.apu._element_find("xpath=" + xpath, False, False))
        return str(count)

    def select_frame(self, locator):
        """Sets frame identified by `locator` as current frame.

        Key attributes for frames are `id` and `name.` See `introduction` for
        details about locating elements.
        """
        element = self.apu._element_find(locator, True, True)
        self.apu._current_application().switch_to_frame(element)

    def unselect_frame(self):
        """Sets the top frame as the current frame."""
        self.apu._current_application().switch_to_default_content()

    def get_element_attribute(self, attribute_locator):
        """Return value of element attribute.

        `attribute_locator` consists of element locator followed by an @ sign
        and attribute name, for example "element_id@class".
        """
        locator, attribute_name = self._parse_attribute_locator(
            attribute_locator)
        element = self.apu._element_find(locator, True, False)
        if element is None:
            raise ValueError("Element '%s' not found." % (locator))
        return element.get_attribute(attribute_name)


    # Private

    def _is_visible(self, locator):
        element = self.apu._element_find(locator, True, False)
        if element is not None:
            return element.is_displayed()
        return None

    def _get_text(self, locator):
        element = self.apu._element_find(locator, True, True)
        if element is not None:
            return element.text
        return None

    def _parse_attribute_locator(self, attribute_locator):
        parts = attribute_locator.rpartition('@')
        if len(parts[0]) == 0:
            raise ValueError("Attribute locator '%s' does not contain "
                             "an element locator." % (attribute_locator))
        if len(parts[2]) == 0:
            raise ValueError("Attribute locator '%s' does not "
                            "contain an attribute name." % (attribute_locator))
        return (parts[0], parts[2])
