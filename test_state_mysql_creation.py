import MySQLdb
import unittest
from models import storage
from models.state import State

class TestState(unittest.TestCase):
    
    def setUp(self):
        """Sets up MySQL connection before each test."""
        self.db = MySQLdb.connect(user='hbnb_test', passwd='hbnb_test_pwd', host='localhost', db='hbnb_test_db')
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT COUNT(*) FROM states")
        self.start_count = self.cursor.fetchone()[0]

    def test_create_state(self):
        """Tests that creating a state adds a record to the table."""
        # Creating a new state
        new_state = State(name="California")
        new_state.save()  # This will persist the state to the database
        
        # Rechecking the record count after save
        self.cursor.execute("SELECT COUNT(*) FROM states")
        end_count = self.cursor.fetchone()[0]
        
        # Assert that the number of records has increased by 1
        self.assertEqual(end_count, self.start_count + 1)

    def tearDown(self):
        """Cleans up after the test."""
        self.cursor.close()
        self.db.close()

if __name__ == "__main__":
    unittest.main()
