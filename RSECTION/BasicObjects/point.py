from RSECTION.enums import PointType, PointCoordinateSystemType, PointReferenceType
from RSECTION.initModel import Model, clearAtributes

class Point():

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

        #Cleint model | None
        clientObject = model.clientModel.factory.create('ns0:point')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Point No.
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

        # Add Point to client model
        model.clientModel.service.set_point(clientObject)

    @staticmethod
    def Standard(
                 no: int = 1,
                 reference_point: int = None,
                 coordinate_system: list = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
        '''

        # Client model | Node
        clientObject = model.clientModel.factory.create('ns0:point')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Node No.
        clientObject.no = no

        # Point Type
        clientObject.type = PointType.TYPE_STANDARD.name

        # Coodinaates System type
        clientObject.coordinate_system_type = PointCoordinateSystemType.COORDINATE_SYSTEM_CARTESIAN.name

        # Coordinates

        if len(coordinate_system) != 2:
            raise Exception('WARNING: The coordinate system needs to be of length 2.')

        if not all(isinstance(x, (int, float)) for x in coordinate_system):
            raise Exception ('WARNING: Coordinate system should be type "int" or "float".')

        clientObject.reference_point = reference_point

        clientObject.coordinate_1 = coordinate_system[0]
        clientObject.coordinate_2 = coordinate_system[1]

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Point to client model
        model.clientModel.service.set_point(clientObject)

    @staticmethod
    def BetweenTwoPoints(
                 no: int = 1,
                 start_point_no: int = 1,
                 end_point_no: int = 2,
                 point_reference = PointReferenceType.REFERENCE_TYPE_L,
                 parameters = [True, 50],
                 offset: float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
        '''

        # Client model | Point
        clientObject = model.clientModel.factory.create('ns0:point')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Point No.
        clientObject.no = no

        # Point Type
        clientObject.type = PointType.TYPE_BETWEEN_TWO_POINTS.name

        # Start Point No.
        clientObject.between_two_points_start_point = start_point_no

        # End Point No.
        clientObject.between_two_points_end_point = end_point_no

        # Point Reference and Distance between Point and Start Point with Offset
        clientObject.reference_type = point_reference.name

        if clientObject.reference_type == "REFERENCE_TYPE_L":

            if parameters[0]:  #if parameters[0]==True

                if parameters[1] <= 0 or parameters[1] >= 1:
                    raise Exception ('Warning: Please enter correct percentage value between 0.0 and 1.0')

                else:
                    clientObject.distance_from_start_relative = parameters[1]

            else:
                clientObject.distance_from_start_absolute = parameters[1]

            clientObject.offset_in_local_direction = offset

        elif clientObject.reference_type == "REFERENCE_TYPE_Y":

            if parameters[0]:  #if parameters[0]==True

                if parameters[1] <= 0 or parameters[1] >= 1:
                    raise Exception ('Warning: Please enter correct percentage value as factor between 0.0 and 1.0')

                else:
                    clientObject.distance_from_start_relative = parameters[1]

            else:
                clientObject.distance_from_start_absolute = parameters[1]

            clientObject.offset_in_global_direction_z = offset

        elif clientObject.reference_type == "REFERENCE_TYPE_Z":

            if parameters[0]:  #if parameters[0]==True

                if parameters[1] <= 0 or parameters[1] >= 1:
                    raise Exception ('Warning: Please enter correct percentage value between 0.0 and 1.0')

                else:
                    clientObject.distance_from_start_relative = parameters[1]

            else:
                clientObject.distance_from_start_absolute = parameters[1]

            clientObject.offset_in_global_direction_y = offset

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Node to client model
        model.clientModel.service.set_point(clientObject)





