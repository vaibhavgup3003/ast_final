import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import engine.engine as engine


class ASTtest(unittest.TestCase):

    def setUp(self):
        self.str1 = """((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"""
        self.str2 = """((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"""
        self.data1 = {
            "age": 31,
            "department": "Sales",
            "salary": 25000,
            "experience": 5,
        }

        self.data2 = {
            "age": 31,
            "department": "Marketing",
            "salary": 25000,
            "experience": 5,
        }

    def test1(self):
        ast = engine.AST()
        root = ast.create_rule(self.str1)
        ast.set_root(root)
        self.assertIsNotNone(root)
        self.assertEqual(ast.evaluate_rule(self.data1), False)
        self.assertEqual(ast.evaluate_rule(self.data2), False)

    def test2(self):
        ast = engine.AST()
        root = ast.create_rule(self.str2)
        ast.set_root(root)
        self.assertIsNotNone(root)
        self.assertEqual(ast.evaluate_rule(self.data1), False)
        self.assertEqual(ast.evaluate_rule(self.data2), True)


if __name__ == "__main__":
    unittest.main()
