import unittest
import os
from datetime import datetime

try:
    os.remove("test.db")
except FileNotFoundError:
    pass


class DatabaseTests(unittest.TestCase):
    def test_import(self):
        import datadriver

    def test_client_create(self):
        import datadriver
        datadriver.DatabaseClient("sqlite:///test.db", echo=True)

    def test_create_user(self):
        import datadriver
        client = datadriver.DatabaseClient("sqlite:///test.db", echo=True)
        client.create_user(id=1234, join_date=datetime.utcnow(), messages=10)

        client.save()


if __name__ == '__main__':
    unittest.main()
