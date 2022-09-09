from RSECTION.initModel import Model, clearAtributes, ConvertToDlString, ConvertStrToListOfInt
from RSECTION.enums import LineType, LineArcAlphaAdjustmentTarget


class Line():

    def __init__(self,
                 no: int = 1,
                 points_no: str = '1 2',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Points No.
        clientObject.definition_points = ConvertToDlString(points_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_line(clientObject)

    @staticmethod
    def Polyline(
                 no: int = 1,
                 points_no: str = '1 2',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_POLYLINE.name

        # Points No.
        clientObject.definition_points = ConvertToDlString(points_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_line(clientObject)

    @staticmethod
    def Arc(
            no: int = 1,
            points_no: list = [1, 2],
            control_point: list = None,
            alpha_adjustment_target = LineArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC,
            comment: str = '',
            params: dict = None,
            model = Model):

        '''
        Args:
            control_point (list): Control Point coordinate for Arc in [Y, Z]

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_ARC.name

        # Points No.
        clientObject.arc_first_point = points_no[0]
        clientObject.arc_second_point = points_no[1]
        clientObject.arc_alpha_adjustment_target = alpha_adjustment_target.name
        clientObject.arc_control_point_y = control_point[0]
        clientObject.arc_control_point_z = control_point[1]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line to client model
        model.clientModel.service.set_line(clientObject)

