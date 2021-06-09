
# opyrator launch-ui ArithmaticOps:listOps

import json
from enum import Enum
import numpy as np

from pydantic import BaseModel, Field, SecretStr
from typing import Dict, List, Optional, Set

from opyrator.components.types import FileContent

class SelectionValue(str, Enum):
    Add = "Add Elements"
    Multiply = "Multiply Elements"
    Square = "Square Elements and Sum"
    Cube = "Cube Elements and sum"

class InputModel(BaseModel):
    
    
    int_list: List[int] = Field(..., description="List of int values")
    operations: Set[SelectionValue] = Field(
        ..., description="Allows multiple items from a set."
    )
    

class OutputModel(BaseModel):
    #message: str
    total: Dict

def listOps(input: InputModel) -> OutputModel:
    """Take list of int and generate addition
    """
    total = {}
    for oper in input.operations:
        if oper == SelectionValue("Add Elements"):
            total[oper] = sum(input.int_list)
        elif oper == SelectionValue("Multiply Elements"):
            total[oper] = np.prod(np.array(input.int_list))
        elif oper == SelectionValue("Square Elements and Sum"):
            total[oper] = sum([i**2 for i in input.int_list])
        elif oper == SelectionValue("Cube Elements and Sum"):
            total[oper] = sum([i**3 for i in input.int_list])
        else:
            pass

    #print(total)
    return OutputModel(total=total)

    
    
    