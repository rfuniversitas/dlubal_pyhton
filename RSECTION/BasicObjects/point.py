from RSECTION.enums import *
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