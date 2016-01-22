"""
A test suite that uses poc_simpletest's TestSuite class to create tests
for TwentyFortyEight class
"""
from poc_simpletest import TestSuite as TestSuite
from merge import merge as merge
from TwentyFortyEight import TwentyFortyEight as TwentyFortyEight

# Test cases for merge function
MERGE_TEST_CASES = [[1, 2, 3, 4],
                    [1, 1, 2, 3],
                    [1, 1, 1, 2],
                    [1, 1, 1, 1],
                    [1, 2, 3, 3],
                    [1, 2, 2, 3],
                    [1, '', 2, 2],
                    ['', '', 2, 2]]
MERGE_EXPECTED_RESULTS = [[1, 2, 3, 4],
                          [2, 2, 3, 0],
                          [2, 1, 2, 0],
                          [2, 2, 0, 0],
                          [1, 2, 6, 0],
                          [1, 4, 3, 0],
                          [1, 4, 0, 0],
                          [4, 0, 0, 0]]

def run_2048_reset_test():
    """
    Test for reset function
    """
    print "Running test suite for reset function"
    suite = TestSuite()
    o_game_board = TwentyFortyEight(4, 4)
    arr_board = o_game_board.reset()
    i_test_count = 1
    for i_index_y in range(4):
        for i_index_x in range(4):
            suite.run_test(arr_board[i_index_y][i_index_x], 0,
                           "Test # " + str(i_test_count))
            i_test_count += 1
    suite.report_results()
    print o_game_board
    o_game_board.get_open_tile()

def run_2048_new_tile_test():
    """
    Checks if new_tile() creates a new tile of either number 2 with 90%
    possibility or a 4 with 10% possibility.
    """
    twos = 0
    fours = 0
    NUM_COUNTS = 1000
    for count in range(NUM_COUNTS):
        o_game_board = TwentyFortyEight(2, 2)
        o_game_board.new_tile()
        twos += sum([row.count(2) for row in o_game_board.arr_grid])
        fours += sum([row.count(4) for row in o_game_board.arr_grid])

    print "twos: %d / %d - %4.1f percent" % (twos, NUM_COUNTS, (twos * 100.0) / NUM_COUNTS)
    print "fours: %d / %d - %4.1f percent" % (fours, NUM_COUNTS, (fours * 100.0) / NUM_COUNTS)

def run_2048_move_test():
    """
    Checks if the grid has been redrawn correctly after a move command
    """
    # suite = TestSuite()
    o_game_board = TwentyFortyEight(4, 6)
    o_game_board.set_tile(0, 0, 2)
    o_game_board.set_tile(1, 0, 2)
    o_game_board.set_tile(1, 3, 2)
    o_game_board.set_tile(3, 3, 4)
    print o_game_board
    o_game_board.move(2)
    # o_game_board.move(3)
    # o_game_board.move(1)
    print o_game_board
    row1 = o_game_board.arr_grid[0].count(4)
    row2 = o_game_board.arr_grid[1].count(0)
    if row1 != 1:
        print "row1 != 4 test failed"
        # print row1
    if row2 != 2:
        print "row2 != 0 test failed"
        # print row2

def run_merge_test():
    """
    Test suite for testing merge function
    """
    print "Running test suite for merge function"
    suite = TestSuite()
    for i_index, case in enumerate(MERGE_TEST_CASES):
        suite.run_test(merge(case),
                       MERGE_EXPECTED_RESULTS[i_index],
                       "Test # " + str(i_index + 1))
    suite.report_results()

# Run the test
# run_merge_test()
# run_2048_reset_test()
# run_2048_new_tile_test()
run_2048_move_test()
