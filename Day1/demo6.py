#!/usr/bin/env python3
# Demo usage of dataclasses 

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(23,32)
print(p)