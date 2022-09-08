from enum import Enum


class ObjectTypes(Enum):
    '''
    Object Types
    '''

    E_OBJECT_TYPE_MATERIAL, E_OBJECT_TYPE_SECTION = range(2)


class PointType(Enum):
    '''
    Point Type | Enumeration
    '''
    TYPE_STANDARD = range(1)

class PointCoordinateSystemType(Enum):
    '''
    Point Coordinate System Type | Enum
    '''
    COORDINATE_SYSTEM_CARTESIAN = range(1)
