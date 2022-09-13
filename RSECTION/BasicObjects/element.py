from RSECTION.initModel import Model, clearAtributes, ConvertToDlString, ConvertStrToListOfInt
from RSECTION.enums import ElementType

class Element():

    def __init__(self,
                 no: int = 1,
                 points_no: str = '1 2',
                 thickness: float = 0.0,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:

        '''

        # Client model | Element
        clientObject = model.clientModel.factory.create('ns0:element')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Points No.
        clientObject.definition_points = ConvertToDlString(points_no)

        # Element Thickness

        clientObject.thickness = thickness

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_element(clientObject)

    def SingleLine(self,
                   no: int = 1,
                   points_no: str = '1 2',
                   thickness: float = 0.0,
                   effective_thickness: list = [False, None],
                   comment: str = '',
                   params: dict = None,
                   model = Model):

        '''
        Args:

        '''

        # Client model | Element
        clientObject = model.clientModel.factory.create('ns0:element')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Points No.
        clientObject.definition_points = ConvertToDlString(points_no)

        # Element Type
        clientObject.type = ElementType.TYPE_SINGLELINE.name

        # Element Thickness

        clientObject.thickness = thickness

        # Effective Thickness

        if effective_thickness[0] == True:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        else:

            clientObject.effective_thickness_checked = effective_thickness[0]
            clientObject.effective_thickness = effective_thickness[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_element(clientObject)
