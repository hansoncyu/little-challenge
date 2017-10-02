import string, unittest

def remove_chars_without_dropping_length(paragraph, length):
    dict = {}
    count_characters(paragraph, dict)
    revr_sorted = sorted(dict, key=dict.get, reverse=True)
    keep_chars = cannot_be_removed(revr_sorted, dict, length)
    discard_chars = can_be_removed(keep_chars, dict)
    return discard_chars

# maps each letter in a paragraph with its count value
def count_characters(paragraph, dict):
    assert type(paragraph) is str

    for char in paragraph:
        dict[char] = dict.get(char, 0) + 1

# from a reverse sorted list of characters based on its count,
# get letters with highest count that can't be removed to stay above desired length
# can pass certain characters like whitespace or numbers by passing if char == ' ' or char in string.digits in for loop
def cannot_be_removed(sorted, dict, length):
    cur_len = 0
    keep_chars = []
    for char in sorted:
        cur_len += dict[char]
        keep_chars += char
        if cur_len >= length:
            return keep_chars

# returns all other characters besides ones that can't be removed to stay above length
def can_be_removed(keep_chars, dict):
    can_discard = []
    for char in dict:
        if char in keep_chars:
            pass
        else:
            can_discard += char
    return can_discard


input = "If you want to jumpstart the process of talking to us about this role, here’s a little challenge: write a program that outputs the largest set of characters that can be removed from this paragraph without letting its length drop below 50. For example: [‘H’, ‘i’, ‘!’, ‘ ‘]"
discard = remove_chars_without_dropping_length(input, 50)
print(discard)

# unit tests
class TestHelperFunctions(unittest.TestCase):

    def test_count_characters(self):
        paragraph = 'abbccc'
        dict = {}
        count_characters(paragraph, dict)
        self.assertEqual(dict['a'], 1)
        self.assertEqual(dict['b'], 2)
        self.assertEqual(dict['c'], 3)
        with self.assertRaises(AssertionError):
            count_characters(1231241, dict)

    def test_cannot_be_removed(self):
        dict = {'a': 50, 'b': 40, 'c': 30, 'd': 20, 'e': 10}
        sorted = ['a', 'b', 'c', 'd', 'e']
        keep_50 = cannot_be_removed(sorted, dict, 50)
        keep_51 = cannot_be_removed(sorted, dict, 51)
        keep_140 = cannot_be_removed(sorted, dict, 140)
        self.assertEqual(keep_50, ['a'])
        self.assertEqual(keep_51, ['a', 'b'])
        self.assertEqual(keep_140, ['a', 'b', 'c', 'd'])

    def test_can_be_removed(self):
        keep_chars = ['a', 'b', 'c', 'd']
        dict = {'a': 50, 'b': 40, 'c': 30, 'd': 20, 'e': 10}
        discard = can_be_removed(keep_chars, dict)
        self.assertEqual(discard, ['e'])


if __name__ == '__main__':
    unittest.main()



