"""
Test suite for merge function
"""
from merge import merge

# 1. Always sliding the list towards index 0
# 2. Same numbers are merged,
# 3. Merged numbers are multiplied by 2
# 4. Merged numbers are reduced into 1 element
# 5. Returns a new list
#
def testMerge():
    testCase1 = [1,2,3,4]
    testCase2 = [1,1,2,3]
    testCase3 = [1,1,1,2]
    testCase4 = [1,1,1,1]
    testCase5 = [1,2,3,3]
    testCase6 = [1,2,2,3]
    testCase7 = [1,'',2,2]
    testCase8 = ['','',2,2]

    result = merge(testCase8)
    iCount = 0
    bResult = 1
    for element in [4,0,0,0]:
        print "expected " + str(element) + " result: " + str(result[iCount])

        if element != result[iCount]:
            print "test failed"
            break
        else:
            iCount += 1

testMerge()
