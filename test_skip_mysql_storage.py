import unittest

# Skip this test if we are using MySQL storage (i.e., `HBNB_TYPE_STORAGE == 'db'`)
@unittest.skipIf(os.environ.get("HBNB_TYPE_STORAGE") == 'db', "MySQL is not relevant for this test.")
def test_some_feature(self):
    # test code here
    pass
