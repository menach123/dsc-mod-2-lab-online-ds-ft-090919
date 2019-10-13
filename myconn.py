import sqlite3

import pandas as pd

# ORM

class MyConn():


    def __init__(self, filename=None):
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()
        pass


    def list_tables(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        results = self.cursor.execute(query).fetchall()
        for r in results:
            print(r[0])
        pass


    def build_select_all_query(self, table_name=None):
        try:
            query = "select * from {}".format(self.table_name)
        except Exception as e:
            print("---no tablename in object, exception:---\n{}".format(e))
            query = "select * from {}".format(table_name)
        return query

    
    def get_table_description(self, table_name=None):
        try:
            query = 'select * from {}'.format(self.table_name)
        except:
            query = 'select * from {}'.format(table_name)
        self.cursor.execute(query)
        return [x[0] for x in self.cursor.description]
    

    def load_table_as_df(self, table_name):
        """
        Loads a table of your sqlite db into a pandas df
        Input
        table_name: str, name of your table
        
        Return
        df: pandas dataframe
        """
        query = self.build_select_all_query(table_name=table_name)
        df = pd.read_sql(query, self.conn)
        return df

    
    def load_query_as_df(self, query):
        df = pd.read_sql(query, self.conn)
        return df


class Customers(MyConn):

    def __init__(self, filename=None):
        super().__init__(filename=filename)
        self.table_name = 'customers'

    
    def select_customers_by_state(self, state=None):
        query = "select * from customers where state='{}'".format(state)
        df = self.load_query_as_df(query)
        return df


    def select_customers_by_country(self, country=None):
        query = "select * from customers where country='{}'".format(country)
        df = self.load_query_as_df(query)
        return df


class Employees(MyConn):


    def __init__(self, filename=None):
        super().__init__(filename=filename)
        self.table_name = 'employees'


    def get_employees_by_title(self, jobtitle=None):
        query = "select * from employees where jobtitle='{}'".format(jobtitle)
        df = self.load_query_as_df(query)
        return df
    