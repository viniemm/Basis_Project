import unittest

from DTable import DTable


class TestDTable(unittest.TestCase):
    def test_add(self):
        # Tests the add method in DTable
        dt = DTable()
        self.assertFalse(all(dt.add("mmm bbb aaa ddd")) == True)
        t = dt.add("wkhs sne aapl")
        self.assertTrue(all(t) == True)

    def test_remove(self):
        # Tests the remove method in DTable
        dt = DTable()
        print(dt.remove("wkhs qqq msft"))
        self.assertTrue(all(dt.remove("wkhs aapl msft")) == True)
        self.assertTrue(all(dt.remove("baby shark doo doo")) == False)
        self.assertListEqual(dt.remove(["hello", "not hello"]), [])
        self.assertListEqual(dt.remove("hello not hello tqqq"), [False, False, False, True])
