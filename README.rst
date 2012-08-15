====
maze
====

A maze game in Tkinter.

procedural_maze_gen.py
----------------------

A script to generate random mazes based on `Depth-first search algorithm`_

.. _Depth-first search algorithm: http://en.wikipedia.org/wiki/Maze_visit_the_celleration_algorithm#Depth-first_search

Example::

    $ python procedural_maze_gen.py --width=21 --height=21 --verbose
    # # # # # # # # # # # # # # # # # # # # # 
    #   #               #               #   # 
    #   #   #   # # #   # # # # #   #   #   # 
    #       #       #               #       # 
    #   # # # # #   # # # # # # # # # # #   # 
    #   #       #           #           #   # 
    #   #   # # # # # # #   # # #   #   #   # 
    #       #               #       #   #   # 
    # # # # #   # # # # # # #   # # # # #   # 
    #           #           #       #       # 
    #   # # # # #   # # #   #   #   #   # # # 
    #   #       #       # @ #   #   #       # 
    #   # # #   #   #   # # #   #   # # #   # 
    #       #       #   #       #           # 
    #   #   # # # # #   #   # # # # # # #   # 
    #   #           #           #       #   # 
    #   # # # # #   #   # # # # #   #   # # # 
    #   #       #   #       #       #       # 
    #   #   #   #   # # # # #   # # # # #   # 
    #       #   #                       # X # 
    # # # # # # # # # # # # # # # # # # # # # 
    Steps from @ to X: 128
