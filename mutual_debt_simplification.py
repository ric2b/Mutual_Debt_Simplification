debts = [('D', 'R', 3),
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

def debt_list_to_graph(debt_list):
    '''
    List of 3-tuples with (debtor, collector, debt_value)
    TODO: type hints
    '''
    debt_graph = {}
    for debt in debt_list:
        debt_graph[debt[0]] = debt_graph.get(debt[0], []) + [(debt[1], debt[2])] 
        debt_graph[debt[1]] = debt_graph.get(debt[1], []) + [(debt[0], -debt[2])]
    
    return debt_graph

def simplify_debt_graph(debt_graph):
    collectors, debtors = collectors_and_debtors(debt_graph)
    return graph_from_collectors_and_debtors(collectors, debtors)

def collectors_and_debtors(debt_graph):
    collectors = {}
    debtors = {}
    for participant in debt_graph:
        total_owed = sum([value for collector, value in debt_graph[participant]])
        if total_owed > 0: # positive debt, is a debtor
            debtors[participant] = total_owed
        elif total_owed < 0: # negative debt, is a collector
            collectors[participant] = -total_owed # switch to positive because it's now a credit instead of a debt

    return collectors, debtors

def graph_from_collectors_and_debtors(collectors, debtors):
    debt_graph = {}
    for collector in sorted(collectors): # from biggest collector
        for debtor in sorted(debtors, reverse=True): # from biggest debtor
            credit, debt = collectors[collector], debtors[debtor]

            if credit != 0 and debt != 0:
                transaction_value = min(credit, debt)
                debt_graph[debtor] = debt_graph.get(debtor, []) + [(collector, transaction_value)]

                if credit >= debt:              
                    collectors[collector] += debt
                    debtors[debtor] = 0
                else:
                    collectors[collector] = 0
                    debtors[debtor] -= credit

    return debt_graph


def draw_graph(debt_graph):
    import graphviz

if __name__ == '__main__':
    print(debt_list_to_graph(debts))
    print(simplify_debt_graph(debt_list_to_graph(debts)))
