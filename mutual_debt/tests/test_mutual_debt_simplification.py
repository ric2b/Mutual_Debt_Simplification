import unittest

from mutual_debt.mutual_debt_simplification import simplify_debt_graph, \
    debt_list_to_graph

test_names = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}

debts = [('A', 'B', 3.5),
         ('A', 'C', 5),
         ('A', 'D', 6),
         ('B', 'A', 1),
         ('B', 'E', 1),
         ('B', 'D', 5),
         ('D', 'C', 3),
         ('D', 'E', 2),
         ('C', 'A', 7),
         ('C', 'A', 4),
         ('C', 'B', 2),
         ('C', 'E', 4),
         ]

debts_zero_sum = [('A', 'B', 1),
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
        self.assertEqual({'A': [('B', 3.5), ('C', 5), ('D', 6)], 'D': [('C', 3), ('E', 2)], 'B': [('A', 1), ('E', 1), ('D', 5)], 'C': [('A', 7), ('A', 4), ('B', 2), ('E', 4)], 'E': []},
                         debt_list_to_graph(debts, test_names).get_raw_data())

    def test_simplify_debt_graph(self):
        self.assertEqual({'A': [('D', 2.5)], 'B': [('D', 1.5)], 'C': [('D', 2), ('E', 7)], 'D': [], 'E': []},
                         simplify_debt_graph(debt_list_to_graph(debts, test_names)).get_raw_data())

    def test_zero_sum(self):
        self.assertEqual({},
                         simplify_debt_graph(debt_list_to_graph(debts_zero_sum, {n: test_names[n] for n in ('A', 'B', 'C')})).get_raw_data())

    def test_feature_all(self):
        self.assertEqual({'A': [('B', 3), ('C', 1)], 'B': [], 'C': []},
                         simplify_debt_graph(debt_list_to_graph(debts_all, {n: test_names[n] for n in ('A', 'B', 'C')})).get_raw_data())

    def test_debts_lists(self):
        self.assertEqual({'A': [('C', 0.5)], 'B': [('C', 0.5)], 'C': []},
                         simplify_debt_graph(debt_list_to_graph(debts_lists, {n: test_names[n] for n in ('A', 'B', 'C')})).get_raw_data())

    def test_empty(self):
        self.assertEqual({},
                         simplify_debt_graph(debt_list_to_graph(debts_empty, {})).get_raw_data())


if __name__ == '__main__':
    unittest.main()
