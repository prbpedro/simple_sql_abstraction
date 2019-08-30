'''
Created on 27 de ago de 2019

@author: Pedro Ribeiro Baptista
'''
import unittest
from simple_sql_abs import dao
from tests import test_entity


class ModuleTest(unittest.TestCase):

    def test(self):
        try:
            data_base_location = 'database.db'
            dao.ConnectionManager(data_base_location, test_entity.__name__,
                                  test_entity.DDLCOMMAND, in_memory=False,
                                  clear_data_base=True)

            _dao = dao.BaseDao()
            _dao.delete(test_entity.TestTable)

            t = test_entity.TestTable()
            t.id = 1
            t.code = 1

            _id = _dao.insert(t)
            select = _dao.select(test_entity.TestTable, id=_id)

            self.assertEqual(1, len(select))
            self.assertEqual(1, select[0].id)
            self.assertEqual(1, select[0].code)

            t2 = select[0]

            t2.code = 2
            _dao.update(t2, id=t2.id)
            select = _dao.select(test_entity.TestTable, id=_id)
            self.assertEqual(1, len(select))
            self.assertEqual(1, select[0].id)
            self.assertEqual(2, select[0].code)

            _dao.delete(test_entity.TestTable, id=_id)
            select = _dao.select(test_entity.TestTable, id=_id)
            self.assertEqual(0, len(select))
        except Exception as e:
            print(e)
            self.assertFalse(True)


if __name__ == "__main__":
    unittest.main()
