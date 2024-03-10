# TODO find a way to graph all the items/objects inside a QCAlgorithm class since it is a steep learning curve

import inspect
from graphviz import Digraph
from AlgorithmImports import *

def graph_class_properties_and_methods(cls):
    dot = Digraph()
    dot.node('Class', cls.__name__)

    for name, obj in inspect.getmembers(cls):
        if inspect.isfunction(obj):
            dot.node(name, f'Method: {name}')
            dot.edge('Class', name)
        elif not name.startswith('__'):
            dot.node(name, f'Property: {name}')
            dot.edge('Class', name)

    return dot

# Example usage
dot = graph_class_properties_and_methods(QCAlgorithm)
dot.render('class_diagram', format='png')  # This saves the diagram as 'class_diagram.png'