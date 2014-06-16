"""
Test suite for merge function in 2048
"""

import poc_simpletest

def run_test(merge):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test format_function on various inputs
    suite.run_test(merge([2, 0, 2, 4]), [4, 4, 0, 0], "Test #1:")
    suite.run_test(merge([0, 0, 2, 2]), [4, 0, 0, 0], "Test #2:")
    suite.run_test(merge([2, 2, 0, 0]), [4, 0, 0, 0], "Test #3:")
    suite.run_test(merge([2, 2, 2, 2]), [4, 4, 0, 0], "Test #4:")
    suite.run_test(merge([8, 16, 16, 8]), [8, 32, 8, 0], "Test #5:")

    suite.report_results()

