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

debts_zeroed = [('A', 'B', 1),
                ('B', 'C',  1),
                ('C', 'A', 1)
                ]

debts_all = [('ALL', 'B', 6),
             ('B', 'C',  1),
             ('C', 'A', 1),
             ('A', 'C', 3)
             ]

debts_lists = [[['A', 'B'], 'C', 4],
               ['C', 'A', 3],
               ['A', 'B', 1.5],
              ]

debts_empty = []


class MutualDebtSimplificationTests(unittest.TestCase):
    def test_debt_list_to_graph(self):
        self.assertEqual({'D': [('R', 3.5), ('S', 5), ('P', 6)], 'P': [('S', 3), ('N', 2)], 'R': [('D', 1), ('N', 1), ('P', 5)], 'S': [('D', 7), ('D', 4), ('R', 2), ('N', 4)], 'N': []},
                         debt_list_to_graph(debts).get_raw_data())

    def test_simplify_debt_graph(self):
        self.assertEqual({'D': [('N', 2.5)], 'S': [('N', 3), ('P', 6)], 'R': [('N', 1.5)], 'P': [], 'N': []},
                         simplify_debt_graph(debt_list_to_graph(debts)).get_raw_data())

    def test_zero_sum(self):
        self.assertEqual({}, simplify_debt_graph(debt_list_to_graph(debts_zeroed)).get_raw_data())

    def test_feature_all(self):
        self.assertEqual({'A': [('B', 3), ('C', 1)], 'B': [], 'C': []}, simplify_debt_graph(debt_list_to_graph(debts_all)).get_raw_data())

    def test_debts_lists(self):
        self.assertEqual({'A': [('C', 0.5)], 'B': [('C', 0.5)], 'C': []}, simplify_debt_graph(debt_list_to_graph(debts_lists)).get_raw_data())

    def test_empty(self):
        self.assertEqual({}, simplify_debt_graph(debt_list_to_graph(debts_empty)).get_raw_data())


if __name__ == '__main__':
    unittest.main()
