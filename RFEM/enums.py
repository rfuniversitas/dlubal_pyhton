from enum import Enum

class MemberType(Enum):
    '''
    Member Type | Enum
    '''
    TYPE_BEAM, TYPE_BUCKLING, TYPE_CABLE, TYPE_COMPRESSION, TYPE_COUPLING_HINGE_HINGE,\
    TYPE_COUPLING_HINGE_RIGID, TYPE_COUPLING_RIGID_HINGE, TYPE_COUPLING_RIGID_RIGID,\
    TYPE_DEFINABLE_STIFFNESS, TYPE_RIB, TYPE_RIGID, TYPE_TENSION, TYPE_TRUSS, TYPE_TRUSS_ONLY_N = range(14)


class NodalSupportType(Enum):
    '''
    Nodal Support Type | Enum
    '''
    FIXED, HINGED, ROLLER, ROLLER_IN_X, ROLLER_IN_Y, ROLLER_IN_Z = range(6)


class StaticAnalysisType(Enum):
    '''
    Static Analysis Type | Enum
    '''
    GEOMETRICALLY_LINEAR, LARGE_DEFORMATIONS, LARGE_DEFORMATIONS_POSTRCRITICAL, SECOND_ORDER_P_DELTA = range(4)


class AnalysisType(Enum):
    '''
    Analysis Type | Enum
    '''
    ANALYSIS_TYPE_CREEP_AND_SHRINKAGE, ANALYSIS_TYPE_CUTTING_PATTERN, ANALYSIS_TYPE_MODAL, ANALYSIS_TYPE_RESPONSE_SPECTRUM,\
    ANALYSIS_TYPE_STATIC, ANALYSIS_TYPE_TIME_DEPENDENT, ANALYSIS_TYPE_TIME_HISTORY, ANALYSIS_TYPE_WIND_SIMULATION = range(8)


class LoadDirectionType(Enum):
    '''
    Load Direction Type | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,\
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z = range(6)

class MemberLoadDirection(Enum):
    '''
    Member Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_PROJECTED, LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE,\
    LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE,\
    LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,\
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_PRINCIPAL_U,\
    LOAD_DIRECTION_PRINCIPAL_V = range(11)

class MemberLoadType(Enum):
    '''
    Member Load Type | Enum
    '''
    E_TYPE_MASS, LOAD_TYPE_AXIAL_DISPLACEMENT, LOAD_TYPE_AXIAL_STRAIN, LOAD_TYPE_DISPLACEMENT, LOAD_TYPE_FORCE,\
    LOAD_TYPE_FORM_FINDING, LOAD_TYPE_INITIAL_PRESTRESS, LOAD_TYPE_MOMENT, LOAD_TYPE_PIPE_CONTENT_FULL,\
    LOAD_TYPE_PIPE_CONTENT_PARTIAL, LOAD_TYPE_PIPE_INTERNAL_PRESSURE, LOAD_TYPE_PRECAMBER, LOAD_TYPE_ROTARY_MOTION,\
    LOAD_TYPE_ROTATION, LOAD_TYPE_TEMPERATURE, LOAD_TYPE_TEMPERATURE_CHANGE = range(16)


class MemberLoadDistribution(Enum):
    '''
    Member Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_CONCENTRATED_1, LOAD_DISTRIBUTION_CONCENTRATED_2, LOAD_DISTRIBUTION_CONCENTRATED_2x2,\
    LOAD_DISTRIBUTION_CONCENTRATED_N, LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LOAD_DISTRIBUTION_PARABOLIC,\
    LOAD_DISTRIBUTION_TAPERED, LOAD_DISTRIBUTION_TRAPEZOIDAL, LOAD_DISTRIBUTION_UNIFORM, LOAD_DISTRIBUTION_UNIFORM_TOTAL,\
    LOAD_DISTRIBUTION_VARYING, LOAD_DISTRIBUTION_VARYING_IN_Z = range(12)

class MemberHingeAxialRelease(Enum):
    '''
    Member Hinge Axial Release | Enum
    '''
    NONLINEARITY_TYPE_DIAGRAM, NONLINEARITY_TYPE_FAILURE_ALL_IF_NEGATIVE, NONLINEARITY_TYPE_FAILURE_ALL_IF_POSITIVE,\
    NONLINEARITY_TYPE_FAILURE_IF_NEGATIVE, NONLINEARITY_TYPE_FAILURE_IF_POSITIVE, NONLINEARITY_TYPE_FRICTION_DIRECTION_1,\
    NONLINEARITY_TYPE_FRICTION_DIRECTION_1_2, NONLINEARITY_TYPE_FRICTION_DIRECTION_1_PLUS_2, NONLINEARITY_TYPE_FRICTION_DIRECTION_2,\
    NONLINEARITY_TYPE_NONE, NONLINEARITY_TYPE_PARTIAL_ACTIVITY, NONLINEARITY_TYPE_STIFFNESS_DIAGRAM = range(12)

class LineLoadType(Enum):
    '''
    Line Load Type | Enum
    '''
    E_TYPE_MASS, LOAD_TYPE_FORCE, LOAD_TYPE_MOMENT = range(3)

class LineLoadDistribution(Enum):
    '''
    Line Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_CONCENTRATED_1, LOAD_DISTRIBUTION_CONCENTRATED_2, LOAD_DISTRIBUTION_CONCENTRATED_2x2,\
    LOAD_DISTRIBUTION_CONCENTRATED_N, LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LOAD_DISTRIBUTION_PARABOLIC,\
    LOAD_DISTRIBUTION_TAPERED, LOAD_DISTRIBUTION_TRAPEZOIDAL, LOAD_DISTRIBUTION_UNIFORM, LOAD_DISTRIBUTION_UNIFORM_TOTAL,\
    LOAD_DISTRIBUTION_VARYING = range(11)
    
class SurfaceLoadDistribution(Enum):
    '''
    Surface Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_LINEAR, LOAD_DISTRIBUTION_LINEAR_IN_X, LOAD_DISTRIBUTION_LINEAR_IN_Y, LOAD_DISTRIBUTION_LINEAR_IN_Z,\
    LOAD_DISTRIBUTION_RADIAL, LOAD_DISTRIBUTION_UNIFORM, LOAD_DISTRIBUTION_VARYING_IN_Z = range(7)

class SurfaceLoadDirection(Enum):
    '''
    Surface Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_PROJECTED, LOAD_DIRECTION_GLOBAL_X_OR_USER_DEFINED_U_TRUE,\
    LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_GLOBAL_Y_OR_USER_DEFINED_V_TRUE,\
    LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE,\
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z = range(9)

class SurfaceLoadType(Enum):
    '''
    Surface Load Type | Enum
    '''
    LOAD_TYPE_AXIAL_STRAIN, LOAD_TYPE_FORCE, LOAD_TYPE_FORM_FINDING, LOAD_TYPE_MASS, LOAD_TYPE_PRECAMBER,\
    LOAD_TYPE_ROTARY_MOTION, LOAD_TYPE_TEMPERATURE = range(7)

class FreeConcentratedLoadLoadDirection(Enum):
    '''
    Load Concentrated Load Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X, LOAD_DIRECTION_GLOBAL_Y, LOAD_DIRECTION_GLOBAL_Z, LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, \
    LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_USER_DEFINED_U, LOAD_DIRECTION_USER_DEFINED_V, LOAD_DIRECTION_USER_DEFINED_W = range(9)

class FreeLoadLoadProjection(Enum):
    '''
    Free Load Load Projection | Enum
    '''
    LOAD_PROJECTION_XY_OR_UV, LOAD_PROJECTION_XZ_OR_UW, LOAD_PROJECTION_YZ_OR_VW = range(3)

class FreeConcentratedLoadLoadType(Enum):
    '''
    Free Concentrated Load Load Type | Enum
    '''
    LOAD_TYPE_FORCE, LOAD_TYPE_MOMENT = range(2)

class FreeLineLoadLoadDirection(Enum):
    '''
    Free Line Load Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_PROJECTED, LOAD_DIRECTION_GLOBAL_X_TRUE, LOAD_DIRECTION_GLOBAL_Y_PROJECTED, \
    LOAD_DIRECTION_GLOBAL_Y_TRUE, LOAD_DIRECTION_GLOBAL_Z_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_TRUE, \
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_USER_DEFINED_U_PROJECTED, \
    LOAD_DIRECTION_USER_DEFINED_U_TRUE, LOAD_DIRECTION_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_USER_DEFINED_V_TRUE, \
    LOAD_DIRECTION_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_USER_DEFINED_W_TRUE = range(15)

class FreeLineLoadLoadDistribution(Enum):
    '''
    Free Line Load Load Distribution | Enum
    '''
    LOAD_DISTRIBUTION_LINEAR, LOAD_DISTRIBUTION_UNIFORM = range(2)

class FreeRectangularLoadLoadDirection(Enum):
    '''
    Free Rectangular Load Load Direction | Enum
    '''
    LOAD_DIRECTION_GLOBAL_X_PROJECTED, LOAD_DIRECTION_GLOBAL_X_TRUE, LOAD_DIRECTION_GLOBAL_Y_PROJECTED, \
    LOAD_DIRECTION_GLOBAL_Y_TRUE, LOAD_DIRECTION_GLOBAL_Z_PROJECTED, LOAD_DIRECTION_GLOBAL_Z_TRUE, \
    LOAD_DIRECTION_LOCAL_X, LOAD_DIRECTION_LOCAL_Y, LOAD_DIRECTION_LOCAL_Z, LOAD_DIRECTION_USER_DEFINED_U_PROJECTED, \
    LOAD_DIRECTION_USER_DEFINED_U_TRUE, LOAD_DIRECTION_USER_DEFINED_V_PROJECTED, LOAD_DIRECTION_USER_DEFINED_V_TRUE, \
    LOAD_DIRECTION_USER_DEFINED_W_PROJECTED, LOAD_DIRECTION_USER_DEFINED_W_TRUE = range(15)

class FreeRectangularLoadLoadDistribution(Enum):

    LOAD_DISTRIBUTION_LINEAR_FIRST, LOAD_DISTRIBUTION_LINEAR_SECOND, LOAD_DISTRIBUTION_UNIFORM, \
    LOAD_DISTRIBUTION_VARYING_ALONG_PERIMETER, LOAD_DISTRIBUTION_VARYING_IN_Z, \
    LOAD_DISTRIBUTION_VARYING_IN_Z_AND_ALONG_PERIMETER = range(6)

class FreeRectangularLoadLoadLocationRectangle(Enum):
    '''
    Free Rectangular Load Load Location Rectangle | Enum
    '''
    LOAD_LOCATION_RECTANGLE_CENTER_AND_SIDES, LOAD_LOCATION_RECTANGLE_CORNER_POINTS = range(2)

class SetType(Enum):
    '''
    Line, Member, Surface, and Solid Set Type | Enum
    '''
    SET_TYPE_CONTINUOUS, SET_TYPE_GROUP = range(2)

class NodalLoadType(Enum):
    '''
    Nodal Load Type | Enum
    '''

    LOAD_TYPE_COMPONENTS, LOAD_TYPE_FORCE, LOAD_TYPE_MASS, LOAD_TYPE_MOMENT = range(4)

class NodalLoadSpecificDirectionType(Enum):
    '''
    Nodal Load Specific Direction Type | Enum
    '''

    DIRECTION_TYPE_DIRECTED_TO_NODE, DIRECTION_TYPE_PARALLEL_TO_CS_OF_LINE, DIRECTION_TYPE_PARALLEL_TO_CS_OF_MEMBER, DIRECTION_TYPE_PARALLEL_TO_TWO_NODES, DIRECTION_TYPE_ROTATED_VIA_3_ANGLES = range(5)

class NodalLoadAxesSequence(Enum):
    '''
    Nodal Load Axes Sequence | Enum
    '''

    SEQUENCE_XYZ, SEQUENCE_XZY, SEQUENCE_YXZ, SEQUENCE_YZX, SEQUENCE_ZXY, SEQUENCE_ZYX = range(6)

class NodalLoadMassAxisRotation(Enum):
    '''
    Nodal Load Mass Axis Rotation | Enum
    '''

    AXIS_OF_ROTATION_X_NEGATIVE, AXIS_OF_ROTATION_X_POSITIVE, AXIS_OF_ROTATION_Y_NEGATIVE, AXIS_OF_ROTATION_Y_POSITIVE, AXIS_OF_ROTATION_Z_NEGATIVE, AXIS_OF_ROTATION_Z_POSITIVE = range(6)