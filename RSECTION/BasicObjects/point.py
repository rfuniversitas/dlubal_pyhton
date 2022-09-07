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

        # Node No.
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

        # Add Node to client model
        model.clientModel.service.set_point(clientObject)




