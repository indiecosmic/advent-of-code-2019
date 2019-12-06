from typing import Dict
from typing import List
from collections import defaultdict

class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        self.parent = None
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
        node.parent = self

def create_map(objects):
    map = {}
    for obj in objects:
        parent, child = obj.split(')')
        if parent not in map:
            map[parent] = []
        map[parent].append(child)
    return map

def orbit_count(key, tree):
    node = find_in_tree(key, tree)
    count = 0
    while node.parent != None:
        node = node.parent
        count += 1
    return count

def total_orbit_count(map: List[str]):
    tree = create_tree(map)
    planets = []
    for obj in map:
        parent, child = obj.split(')')
        if parent not in planets:
            planets.append(parent)
        if child not in planets:
            planets.append(child)
    
    count = 0
    for planet in planets:
        count += orbit_count(planet, tree)
    
    return count

def create_node_list(map):
    planets = []
    for obj in map:
        parent, child = obj.split(')')
        if parent not in planets:
            planets.append(parent)
        if child not in planets:
            planets.append(child)
    return planets

def create_tree(objects) -> Tree:
    map = create_map(objects)
    root = Tree('COM')
    create_node(root, map)
    return root

def create_node(parent, map):
    if parent.name not in map:
        return
    for child in map[parent.name]:
        node = Tree(child)
        parent.add_child(node)
        create_node(node, map)

def find_in_tree(key, tree):
    if tree == None:
        return None
    if tree.name == key:
        return tree
    for child in tree.children:
        res = find_in_tree(key, child)
        if res != None:
            return res
    return None

if __name__ == '__main__':
    with open('day6.txt') as f:
        contents = f.read()
        planets = contents.strip().split('\n')
        print(total_orbit_count(planets))