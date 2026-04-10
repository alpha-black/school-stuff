#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class GraphNode:
    val: int
    neighbors: List = field(default_factory=list)
    weights: Optional[List[int]] = None
