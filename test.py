import pytest
from utils import matchingStrings

@pytest.mark.set1
def test_matchingStrings():
	expected_result = {"ab": 2, "abc": 1, "bc": 0}
	input_sentence = "ab,ab,abc"
	assert matchingStrings(input_sentence,"ab,abc,bc") == expected_result,"test failed"


# next time i'll use mock way for testing my code, there is a lot more to test.
