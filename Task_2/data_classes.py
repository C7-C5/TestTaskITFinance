from typing import List
from dataclasses import dataclass, field

@dataclass
class ChemicalElement:
    atomic: str
    name: str
    weight: str

@dataclass
class ChemicalElements:
    elements: List[ChemicalElement] = field(default_factory=list)
