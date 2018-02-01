import unittest


def best_two_keys(dict):
  if len(dict.keys()) < 2:
    raise ValueError('dictionary must have at least two keys')
  kv_pairs = []
  for k in dict.keys():
    if not type(k) == str:
      raise ValueError('dictionary keys must be strings')
    kv_pairs.append((k, dict[k]))
  kv_pairs.sort() # sorts by first key
  sorted_pairs = sorted(kv_pairs, key=lambda t: t[1])
  return ((sorted_pairs[0][0], sorted_pairs[1][0]))




class TestBest2(unittest.TestCase):

  def testIt(self):
    dict1 = {"one": 1, "two": 2, "three": 3}
    dict2 = {"one": 1}
    dict3 = {"one": 1, "two": 2, "also_two": 2}
    dict4 = {1: "one"}

    self.assertEqual(best_two_keys(dict1), ("one", "two"))
    self.assertEqual(best_two_keys(dict3), ("one", "also_two"))
    self.assertRaises(ValueError, best_two_keys, dict2)
    self.assertRaises(ValueError, best_two_keys, dict4)


unittest.main()
