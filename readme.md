# ZDD-based covering array generation 

This page contains a python program for generating covering arrays. 
The program uses [graphillion](https://github.com/takemaru/graphillion), a ZDD-based graph manipulating library. 

The algorithm behind the program is elaborated in our paper:

[Teru Ohashi, Tatsuhiro Tsuchiya:
Generating High Strength Test Suites for Combinatorial Interaction Testing Using ZDD-Based Graph Algorithms. PRDC 2017: 78-85](https://ieeexplore.ieee.org/document/7920599)

The usage of the program should be clear if you look at the code. 

As presented in the paper, the algorithm sometimes works faster than [PICT](https://github.com/microsoft/pict), a well-known 
covering array generation tool, but can hardly beat [ACTS](https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software), a more recent tool. 

The program was originally written in Python 2 by Teru Ohashi and was then rewritten in Python 3 by Tatsuhiro Tsuchiya.
