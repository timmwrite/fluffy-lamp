import os
from unittest import TestCase

from mongo_config import MongoConfig
from mongo_test_data import (insert_many_data, insert_one_data, print_many_query_data,
                  print_many_query_2_data, update_one_query, set_values, update_many_query, set_values_2)

BAD_CONNECTION_URL = os.getenv('BAD_CONNECTION_URL')

class MongoTestCase(TestCase):

    def setUp(self):
        self.db = MongoConfig()
    
    def test_get_client(self):
        self.assertNotEqual(self.db.get_client(),
                             "Unable to create MongoClient")
        
    def test_fail_get_client(self):
        self.assertEqual(self.db.get_client(BAD_CONNECTION_URL),
                         "Unable to create MongoClient")

    def test_list_dbs(self):
        self.assertNotEqual(self.db.list_dbs(),
                            "Unable to list databases")

    def test_fail_list_dbs(self):
        self.assertEqual(self.db.list_dbs(BAD_CONNECTION_URL),
                            "Unable to list databases")

    def test_use_db(self):
        self.assertNotEqual(self.db.use_db('my_database'),
                            "Unable to use database")

    def test_use_collection(self):
         self.assertNotEqual(self.db.use_collection('my_database', 'customers'),
                             "Unable to use collection")

    def test_insert_one(self):
         self.assertNotEqual(self.db.insert_one('my_database', 'customers', insert_one_data),
                             "Unable to insert document")

    def test_insert_many(self):
         self.assertNotEqual(self.db.insert_many('my_database', 'customers', insert_many_data),
                             "Unable to insert more documents")

    def test_find_one(self):
         self.assertNotEqual(self.db.find_one('my_database', 'customers'),
                             "Unable to find one document")

    def test_find_many(self):
        self.assertNotEqual(self.db.find_many('my_database', 'customers'),
                              "Unable to print documents")

        self.assertNotEqual(self.db.find_many('my_database', 'customers',print_many_query_data),
                             "Unable to print documents")

        self.assertNotEqual(self.db.find_many('my_database', 'customers',print_many_query_2_data),
                             "Unable to print documents")

    def test_update_one(self):
        self.assertNotEqual(self.db.update_one(
            'my_database', 'customers', update_one_query, set_values), 'Unable to update document')

    def test_fail_update_one(self):
        self.assertEqual(self.db.update_one(
            'my_database', 'customers', update_one_query, set_values, BAD_CONNECTION_URL), 'Unable to update document')

    def test_update_many(self):
        self.assertNotEqual(self.db.update_many(
            'my_database', 'customers', update_many_query, set_values_2), 'Unable to update the documents')

    def test_fail_update_many(self):
        self.assertEqual(self.db.update_many(
            'my_database', 'customers', update_many_query, set_values_2, BAD_CONNECTION_URL), 'Unable to update the documents')
