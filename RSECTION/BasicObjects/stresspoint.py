from RSECTION.enums import StressPointType, PointCoordinateSystemType, PointReferenceType, ElementSide
from RSECTION.initModel import Model, clearAtributes, ConvertStrToListOfInt

class StressPoint():

    def __init__(self,
                 no: int = 1,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Arg:

        '''

        #Cleint model | Stress Point
        clientObject = model.clientModel.factory.create('ns0:stress_point')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Stress Point No.
        clientObject.no = no

        # Coordinates
        clientObject.coordinate_1 = coordinate_Y
        clientObject.coordinate_2 = coordinate_Z

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Stress Point to client model
        model.clientModel.service.set_stress_point(clientObject)

    @staticmethod
    def Standard(
                 no: int = 1,
                 coordinate_system: list = None,
                 reference_point: int = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
        '''

        # Client model | Stress Point
        clientObject = model.clientModel.factory.create('ns0:stress_point')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Stress Point No.
        clientObject.no = no

        # Stress Point Type
        clientObject.definition_type = StressPointType.TYPE_STANDARD.name

        # Coodinaates System type
        clientObject.coordinate_system_type = PointCoordinateSystemType.COORDINATE_SYSTEM_CARTESIAN.name

        # Coordinates

        if len(coordinate_system) != 2:
            raise Exception('WARNING: The coordinate system needs to be of length 2.')

        if not all(isinstance(x, (int, float)) for x in coordinate_system):
            raise Exception ('WARNING: Coordinate system should be type "int" or "float".')

        clientObject.reference_stress_point = reference_point

        clientObject.coordinate_1 = coordinate_system[0]
        clientObject.coordinate_2 = coordinate_system[1]

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Stress Point to client model
        model.clientModel.service.set_stress_point(clientObject)

    @staticmethod
    def OnLine(
                 no: int = 1,
                 line_no: int = 1,
                 point_reference = PointReferenceType.REFERENCE_TYPE_L,
                 parameters = [True, 0.5],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
        '''

        # Client model | Stress Point
        clientObject = model.clientModel.factory.create('ns0:stress_point')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Stress Point No.
        clientObject.no = no

        # Stress Point Type
        clientObject.definition_type = StressPointType.TYPE_ON_LINE.name

        # Line No.
        clientObject.on_line_reference_line = line_no

        # Point Reference and Distance between Point and Start Point
        clientObject.reference_type = point_reference.name

        if parameters[0]:  #if parameters[0]==True

            if parameters[1] <= 0 or parameters[1] >= 1:
                raise Exception ('Warning: Please enter correct percentage value between 0.0 and 1.0')

            else:
                clientObject.distance_from_start_relative = parameters[1]

        else:
            clientObject.distance_from_start_absolute = parameters[1]

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Stress Point to client model
        model.clientModel.service.set_stress_point(clientObject)

    @staticmethod
    def OnElement(
                 no: int = 1,
                 element_no: int = 1,
                 element_side = ElementSide.ELEMENT_SIDE_MIDDLE,
                 point_reference = PointReferenceType.REFERENCE_TYPE_L,
                 parameters = [True, 0.5],
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
        '''

        # Client model | Stress Point
        clientObject = model.clientModel.factory.create('ns0:stress_point')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Stress Point No.
        clientObject.no = no

        # Stress Point Type
        clientObject.definition_type = StressPointType.TYPE_ON_ELEMENT.name

        # Line No.
        clientObject.on_element_reference_element = element_no
        clientObject.on_element_element_side = element_side.name

        # Point Reference and Distance between Point and Start Point
        clientObject.reference_type = point_reference.name

        if parameters[0]:  #if parameters[0]==True

            if parameters[1] <= 0 or parameters[1] >= 1:
                raise Exception ('Warning: Please enter correct percentage value between 0.0 and 1.0')

            else:
                clientObject.distance_from_start_relative = parameters[1]

        else:
            clientObject.distance_from_start_absolute = parameters[1]

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Stress Point to client model
        model.clientModel.service.set_stress_point(clientObject)