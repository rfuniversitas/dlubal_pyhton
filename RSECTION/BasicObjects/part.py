from RSECTION.initModel import ConvertToDlString, Model, clearAtributes
from RSECTION.enums import ObjectTypes

class Part():

    def __init__(self,
                 no: int = 1,
                 boundary_lines: str = None,
                 material_no: int = 1,
                 integrated_objects: bool = True,
                 integrated_objects_auto : bool = True,
                 integrated_openings: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:

        '''

        # Client model | Part
        clientObject = model.clientModel.factory.create('ns0:part')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Boundary Lines for Part
        clientObject.boundary_lines = ConvertToDlString(boundary_lines)

        # Assigned Material

        clientObject.material = material_no

        # Integrated Objects

        if integrated_objects:

            if integrated_objects_auto == False:

                clientObject.auto_detection_of_integrated_objects = False
                clientObject.integrated_openings = ConvertToDlString(integrated_openings)

        else:
            clientObject.has_integrated_objects = False

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Point to client model
        model.clientModel.service.set_part(clientObject)
