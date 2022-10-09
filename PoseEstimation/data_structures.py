import enum
from enum import Enum, unique

@unique
class FeatureDetectionMode(Enum):
    INITIALIZATION = 1
    ACTIVE = 2
    

