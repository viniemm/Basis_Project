import unittest

from databases.DTable import DTable


class TestDTable(unittest.TestCase):
    def test_add(self):
        dt = DTable()
        t = dt.add(["wkhs", "sne", "aapl", "googl", "msft"])
        self.assertTrue(all(t) is True)

    def test_remove(self):
        dt = DTable()
        t = dt.remove(["msft", "aapl", "googl"])
        self.assertTrue(all(t) is True)

    def test_1(self):
        dt = DTable()
        self.assertTrue(all(dt.remove(["baby", "shark", "doo doo"])) is False)

    def test_2(self):
        dt = DTable()
        self.assertFalse(all(dt.add(["mmob", "bbb", "aaa", "ddd"])) is True)

    def test_3(self):
        dt = DTable()
        dt.sub_done()
        dt.done()


# if __name__ == "__main__":
#     unittest.main()
