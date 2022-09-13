from RSECTION.initModel import Model, clearAtributes, ConvertToDlString, ConvertStrToListOfInt
from RSECTION.enums import ElementType, ElementArcAlphaAdjustmentTarget

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

    @staticmethod
    def SingleLine(
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

    @staticmethod
    def Arc(
            no: int = 1,
            points_no: list = [1, 2],
            control_point: list = None,
            alpha_adjustment_target = ElementArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC,
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

        # Type
        clientObject.type = ElementType.TYPE_ARC.name

        # Points No. and Control Point Coordinates
        clientObject.arc_first_point = points_no[0]
        clientObject.arc_second_point = points_no[1]
        clientObject.arc_alpha_adjustment_target = alpha_adjustment_target.name
        clientObject.arc_control_point_y = control_point[0]
        clientObject.arc_control_point_z = control_point[1]

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

    @staticmethod
    def Circle(
                no: int = 1,
                center_of_cirle: list = [0.0, 0.0],
                circle_radius: float = 0.1,
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

        # Type
        clientObject.type = ElementType.TYPE_CIRCLE.name

        # Center of circle and Radius
        clientObject.circle_center_coordinate_y = center_of_cirle[0]
        clientObject.circle_center_coordinate_z = center_of_cirle[1]

        clientObject.circle_radius = circle_radius

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

    @staticmethod
    def Ellipse(
                no: int = 1,
                points_no: list = [1, 2],
                control_point: list = None,
                thickness: float = 0.0,
                effective_thickness: list = [False, None],
                comment: str = '',
                params: dict = None,
                model = Model):

        '''
        Args:
            control_point (list): Control Point coordinate for Ellipse in [Y, Z]

        '''

        # Client model | Line
        clientObject = model.clientModel.factory.create('ns0:element')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = ElementType.TYPE_ELLIPSE.name

        # Points No. and Ellipse Control Point Coordinates
        clientObject.ellipse_first_point = points_no[0]
        clientObject.ellipse_second_point = points_no[1]
        clientObject.ellipse_control_point_y = control_point[0]
        clientObject.ellipse_control_point_z = control_point[1]

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



