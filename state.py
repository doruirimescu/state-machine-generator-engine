from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional

@dataclass()
class State:
    index: int
    label: str
    successors: Dict[str, int]
    output: Tuple[str]
    on_entry: Optional[str] = None
    on_exit: Optional[str] = None
