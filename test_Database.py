import unittest

from databases.DTable import DTable
from databases import Mailer as ml
import pandas as pd

dt = DTable("test_port")


class TestDTable(unittest.TestCase):

    def test_add(self):
        t = dt.add(["wkhs", "sne", "aapl", "googl", "msft"])
        self.assertTrue(all(t) is True)

    def test_remove1(self):
        t = dt.remove(["wkhs", "sne"])
        self.assertTrue(all(t) is True)

    def test_remove2(self):
        nt = dt.remove(["mmm", "jj"])
        self.assertFalse(all(nt) is True)

    def test_get1(self):
        df1 = dt.get("hello")
        self.assertTrue(df1.empty)

    def test_get2(self):
        df2 = dt.get(["msft", "googl"])
        self.assertFalse(df2.empty)

    def test_all(self):
        df3 = dt.all()
        self.assertFalse(df3.empty)

    def test_done(self):
        t = dt.done()
        self.assertTrue(t)

    def test_sub_done(self):
        st = dt.sub_done()
        self.assertTrue(st)


class TestMailer(unittest.TestCase):
    def test_mail1(self):
        t = ml.mail("vinayakrulez@gmail.com", "test_port.csv")
        self.assertTrue(t)

    def test_mail2(self):
        nt = ml.mail("fakeemail", "test_port.csv")
        self.assertFalse(nt)

if __name__ == "__main__":
     unittest.main()
