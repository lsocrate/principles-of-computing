"""
Test suite for 2048
"""

import poc_simpletest

def tester(TwentyFortyEight):
    tester = TwentyFortyEight(4, 4)
    tester.set_tile(0, 0, 4)
    tester.set_tile(0, 1, 2)
    tester.set_tile(0, 2, 2)
    tester.set_tile(0, 3, 2)
    tester.set_tile(1, 2, 2)
    tester.set_tile(1, 3, 8)
    tester.set_tile(2, 0, 4)
    tester.set_tile(2, 1, 2)
    tester.set_tile(2, 2, 2)
    tester.set_tile(2, 3, 8)
    tester.set_tile(3, 1, 2)
    tester.set_tile(3, 3, 4)

    return tester

def run_test(TwentyFortyEight):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test format_function on various inputs
    twentyfortyeight = TwentyFortyEight(4, 5)
    suite.run_test(len(twentyfortyeight._grid), 4, "Test #1:")
    suite.run_test(len(twentyfortyeight._grid[0]), 5, "Test #2:")

    twentyfortyeight.set_tile(2, 3, 4)
    suite.run_test(twentyfortyeight.get_tile(2, 3), 4, "Test #3:")
    suite.run_test(twentyfortyeight.get_tile(1, 2), 0, "Test #4:")

    move_tester_up = tester(TwentyFortyEight)
    move_tester_up.move(1)
    suite.run_test(move_tester_up.get_tile(0, 0), 8, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(0, 1), 4, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(0, 2), 4, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(0, 3), 2, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(1, 0), 0, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(1, 1), 2, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(1, 2), 2, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(1, 3), 16, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(2, 0), 0, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(2, 1), 0, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(2, 2), 0, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(2, 3), 4, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(3, 0), 0, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(3, 1), 0, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(3, 2), 0, "Test Move Up")
    suite.run_test(move_tester_up.get_tile(3, 3), 0, "Test Move Up")

    move_tester_right = tester(TwentyFortyEight)
    move_tester_right.move(4)
    suite.run_test(move_tester_right.get_tile(0, 0), 0, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(0, 1), 4, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(0, 2), 2, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(0, 3), 4, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(1, 0), 0, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(1, 1), 0, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(1, 2), 2, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(1, 3), 8, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(2, 0), 0, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(2, 1), 4, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(2, 2), 4, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(2, 3), 8, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(3, 0), 0, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(3, 1), 0, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(3, 2), 2, "Test Move Right")
    suite.run_test(move_tester_right.get_tile(3, 3), 4, "Test Move Right")

    move_tester_down = tester(TwentyFortyEight)
    move_tester_down.move(2)
    suite.run_test(move_tester_down.get_tile(0, 0), 0, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(0, 1), 0, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(0, 2), 0, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(0, 3), 0, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(1, 0), 0, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(1, 1), 0, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(1, 2), 0, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(1, 3), 2, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(2, 0), 0, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(2, 1), 2, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(2, 2), 2, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(2, 3), 16, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(3, 0), 8, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(3, 1), 4, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(3, 2), 4, "Test Move Down")
    suite.run_test(move_tester_down.get_tile(3, 3), 4, "Test Move Down")

    move_tester_left = tester(TwentyFortyEight)
    move_tester_left.move(3)
    suite.run_test(move_tester_left.get_tile(0, 0), 4, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(0, 1), 4, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(0, 2), 2, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(0, 3), 0, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(1, 0), 2, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(1, 1), 8, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(1, 2), 0, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(1, 3), 0, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(2, 0), 4, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(2, 1), 4, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(2, 2), 8, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(2, 3), 0, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(3, 0), 2, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(3, 1), 4, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(3, 2), 0, "Test Move Left")
    suite.run_test(move_tester_left.get_tile(3, 3), 0, "Test Move Left")


    suite.report_results()

