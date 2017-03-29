# -*- coding: utf-8 -*-
"""
Created on 25/03/2017

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

"""
**Search tree**

Left first, depth first enumeration

Take an element from the still to be considered items
if there is room for that item, a node is made that represents that choice, that will be the left node
always check the consequences of not taking the item, that will be the right node
This has to be recursively called to non-leaf nodes
"""
