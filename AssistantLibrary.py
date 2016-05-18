# -*- coding: utf-8 -*-
"""Doc string."""

# import requests
import platform
import shutil
import xml.etree.ElementTree as ET
from selenium.webdriver.chrome.options import Options
# from utils.active_accommodations import name_to_value
from itertools import combinations


class AssistantLibrary(object):
    """Logic Library for generating different user to login the site.

    This library will ask the backend API to request different users login,
    so that to start the automation.
    """

    def __init__(self):
        """Init function.

        Load and store default variables in to variables.
        """
        pass

    def modify_configuration(self, config_file, key, value):
        """Modify the configuration file for the given key with the given value.

        This method will provide interface to read and return config value to
        robot framework testcase to modify values in the web.config

        Examples:
        | Modify Configuration | /Web/Web.config | webpages:Version | 2.2.2.2 |
        """
        tree = ET.parse(config_file)
        root = tree.getroot()
        item = root.findall(".//*[@key='%s']" % key)

        if len(item) > 0:
            # backup old file
            try:
                with open(config_file + ".bak"):
                    pass
            except IOError:
                shutil.copy(config_file, config_file + '.bak')

            item[0].set('value', value)
            tree.write(config_file)

    def revert_configuration(self, config_file):
        """Restore the configuration file back to original.

        This method will provide interface to restore config.ini file from
        robotframework keyword.

        Example:
        | Revert Configuration |
        """
        try:
            with open(config_file + ".bak"):
                shutil.move(config_file + '.bak', config_file)
        except IOError:
            pass

    def get_chrome_options(self, binary_location):
        """.

        Just return kiosk binary_location from variables file.
        """
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.binary_location = binary_location
        return chrome_options

    def get_user_by_accom(self, options):
        """Enter the student type options that will requst from API.

        Examples:
        | Get User By Accom | default  |
        """
        if options == 'default':
            return ['Practice-19035', 'RJHUKAQ2']
        elif options == 'regression':
            return ['555599991', '2749DA5E']
        elif options == 'network':
            return ['555599992', 'CD6E997E']
        elif options == 'session_code':
            return ['555599997', 'B79CCAC8']
        elif options == 'timeout':
            return ['555599999', 'E94DBB29']
        elif options == 'NoAccommodation':
            return ['555500001', '87CD25DD']
        elif options == 'operational':
            return ['555599998', 'E7F8FD38']
        else:
            return ['username', 'error_password']

        # end_point = "user/"
        # API_PATH = self.get_config('urls', 'api')
        # r = requests.post(API_PATH + end_point, data=options)

    # def num_to_options_number(self, data):
    #     combinations = []
    #     for x in data:
    #         arr = []
    #         for y in x:
    #             if 'spoken' == y:
    #                 arr.append(name_to_value['spoken'] + 3)
    #             elif 'magnification' == y:
    #                 arr.append(name_to_value['magnification'] + 3)
    #             elif 'masking' == y:
    #                 arr.append(name_to_value['masking'] + 3)
    #             elif 'invertcolourchoice' == y:
    #                 arr.append(name_to_value['invertcolourchoice'] + 3)
    #             elif 'linereader' == y:
    #                 arr.append(name_to_value['linereader'] + 3)
    #             elif 'colorschemes' == y:
    #                 arr.append(name_to_value['colorschemes'] + 3)
    #         combinations.append(arr)
    #     return combinations

    def get_single_combination(self, combinations, index):
        """Get single combination used for test cases by `index`.

        Return one single combination for clicking on the page.
        Because of RobotFramework could not manage array calculate.

        Examples:
        | Get Single Combination | [('a', 'b'), ('a', 'b', 'c')] | 1 |
        """
        return combinations[int(index)]

    def option_combinations(self, options):
        """Get all combinations used for test cases.

        Return all combinations for accommodation options list.

        Examples:
        | Options Combinations | ['spoken', 'magnification'] |
        """
        n = range(1, len(options) + 1)

        # select_combinations is something like `[(1), (1, 2), (1, 2, 3) ...]`
        select_combinations = []
        for i in xrange(0, len(options)):
            select_combinations += list(combinations(n, i))

        # convert_to_names is something like `[(spoken), (spoken, masking)..]`
        convert_to_names = []
        for i in select_combinations:
            single_combination = []
            # i = (1, 2, 3)
            for j in i:
                single_combination.append(options[j - 1])
            convert_to_names.append(single_combination)

        return convert_to_names

    def get_platform(self):
        """Get Platform name.

        Return the current running system name.

        Examples:
        | Get Platform |
        """
        return platform.system()
