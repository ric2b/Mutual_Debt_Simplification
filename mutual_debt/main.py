"""Mutual Debt Simplification

Usage:
  simplify-debts [ <data_file> ] [ -a | --auto-open ]
  simplify-debts (-h | --help)

Options:
  -h --help        Show this screen.
  -a --auto-open   Automatically open the graph with the default PDF reader.
"""
import json
import sys

from docopt import docopt

from mutual_debt.simplification import debt_list_to_graph, \
    simplify_debt_graph, draw_graph


def print_error(*args, sep=' ', end='\n'):
    """ Prints values to the stderr stream """
    print("ERROR:", *args, sep, end, file=sys.stderr)


DEFAULT_DATA_FILE = 'debts.json'


def main():
    args = docopt(__doc__)
    data_file = args['<data_file>']
    open_file = args['--auto-open']

    print(open_file)

    if not data_file:
        print("INFO: using default data file `%s`" % DEFAULT_DATA_FILE)
        data_file = DEFAULT_DATA_FILE

    # Try to load debts from data file
    # On failure: show error and exit using error code
    try:
        with open(data_file) as file:
            debts = json.load(file)

    except IOError as error:
        print_error("failed to read data file:", str(error))
        sys.exit(1)

    initial_debt_graph = debt_list_to_graph(debts['debt_list'], debts['names'])
    draw_graph(initial_debt_graph, 'Initial_Mutual_Debt', open_file=open_file)
    simplified_debt_graph = simplify_debt_graph(initial_debt_graph)
    draw_graph(simplified_debt_graph, 'Simplified_Mutual_Debt')


if __name__ == '__main__':
    main()
