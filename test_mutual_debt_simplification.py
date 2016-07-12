import unittest
from mutual_debt_simplification import simplify_debt_graph, debt_list_to_graph

debts = [('D', 'R', 3.5),
         ('D', 'S', 5),
         ('D', 'P', 6),
         ('R', 'D', 1),
         ('R', 'N', 1),
         ('R', 'P', 5),
         ('P', 'S', 3),
         ('P', 'N', 2),
         ('S', 'D', 7),
         ('S', 'D', 4),
         ('S', 'R', 2),
         ('S', 'N', 4),
         ]


class MutualDebtSimplificationTests(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual({'D': [('P', 2.5)], 'S': [('N', 7), ('P', 2)], 'R': [('P', 1.5)]}, simplify_debt_graph(debt_list_to_graph(debts)))


if __name__ == '__main__':
    unittest.main()
