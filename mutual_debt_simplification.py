def debt_list_to_graph(debt_list, name_translation=None):
    """
    List of 3-tuples with (debtor, collector, debt_value)
    TODO: type hints
    """
    debt_graph = {}
    for debt in debt_list:
        debtor = name_translation[debt[0]] if name_translation else debt[0]
        creditor = name_translation[debt[1]] if name_translation else debt[1]
        debt_graph[debtor] = debt_graph.get(debtor, []) + [(creditor, debt[2])]
        debt_graph[creditor] = debt_graph.get(creditor, []) + [(debtor, -debt[2])]

    return debt_graph


def simplify_debt_graph(debt_graph):
    collectors, debtors = collectors_and_debtors(debt_graph)
    return graph_from_collectors_and_debtors(collectors, debtors)


def collectors_and_debtors(debt_graph):
    collectors = {}
    debtors = {}
    for participant in debt_graph:
        total_owed = sum([value for collector, value in debt_graph[participant]])
        if total_owed > 0:  # positive debt, is a debtor
            debtors[participant] = total_owed
        elif total_owed < 0:  # negative debt, is a collector
            collectors[participant] = -total_owed  # switch to positive because it's now a credit instead of a debt

    return collectors, debtors


def graph_from_collectors_and_debtors(collectors, debtors):
    debt_graph = {}
    for collector in sorted(collectors):  # from biggest collector
        for debtor in sorted(debtors, reverse=True):  # from biggest debtor
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
    try:
        from graphviz import Digraph
    except ImportError:
        Digraph = None

    if Digraph:
        viz = Digraph('Simplified Mutual Debt')
        viz.node_attr.update(color='orangered', shape='box', style='rounded', penwidth='2')
        for participant in debt_graph:
            viz.node(participant)
            for debt in debt_graph[participant]:
                viz.edge(participant, debt[0], xlabel=str(debt[1]))
        viz.view()
    else:
        print(debt_graph)
        print('(Please install graphviz for a much cleaner visualization of the graph)')


if __name__ == '__main__':
    import json
    debts = json.load(open('debt_list', 'r'))

    initial_debt_graph = debt_list_to_graph(debts['debt_list'], debts['names'])
    simplified_debt_graph = simplify_debt_graph(initial_debt_graph)
    draw_graph(initial_debt_graph)
