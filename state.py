from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional

@dataclass()
class State:
    index: int
    label: str
    successors: Dict[str, str] # maps action to successor state label
    output: Tuple[str]
    on_entry: Optional[str] = None
    on_exit: Optional[str] = None
