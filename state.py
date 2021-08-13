from dataclasses import dataclass
from typing import List, Tuple, Dict

@dataclass()
class State:
    index: int
    label: str
    successors: Dict[str, int]
    output: Tuple[str]
