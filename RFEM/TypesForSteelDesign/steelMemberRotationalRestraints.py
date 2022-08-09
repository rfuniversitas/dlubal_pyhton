from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import *

class SteelMemberRotationalRestraint():
    def __init__(self,
                no: int = 1,
                user_defined_name: list = [False],
                definition_type = SteelMemberRotationalRestraintType.TYPE_CONTINUOUS,
                members: str = "",
                member_sets: str = "",
                categories: list = [],
                parameters: list = [],
                comment: str = '',
                params: dict = None,
                model = Model):
        """
        Args:
            no (int): Steel Member Rotational Restraint Tag
            user_defined_name (list): User Defined Member Rotational Restraint Name
                for user_defined_name[0] == False:
                    pass
                for user_defined_name == True:
                    user_defined_name[1] = Defined Name
            definition_type (enum): Steel Member Rotational Restraint Type Enumeration
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            categories (list): Categories List
                for definition_type = SteelMemberRotationalRestraintType.TYPE_CONTINUOUS:
                    categories[0] = Sheeting Material Name
                    categories[1] = Sheeting Name
                    categories[2] = Position of Sheeting
                    categories[3] = Continuous Beam Effect
                    categories[4] = Section Deformation Option
                for definition_type = SteelMemberRotationalRestraintType.TYPE_DISCRETE:
                    categories[0] = Section Material Name
                    categories[1] = Section Name
                    categories[2] = Rotational Stifness
                    categories[3] = Continuous Beam Effect
                    categories[4] = Section Deformation Option
                for definition_type = SteelMemberRotationalRestraintType.TYPE_MANUALLY:
                    categories = None
            parameters (list): Parameters List
                for definition_type = SteelMemberRotationalRestraintType.TYPE_CONTINUOUS:
                    parameters[0] = Modulus of Elasticity
                    parameters[1] = Sheeting Thickness
                    parameters[2] = Sheeting Moment of Inertia
                    parameters[3] = Sheeting Distance of Ribs
                    parameters[4] = Width of Sheeting Flanges
                    parameters[5] = Spring Stiffness
                    parameters[6] = Beam Spacing
                for definition_type = SteelMemberRotationalRestraintType.TYPE_DISCRETE:
                    parameters[0] = Modulus of Elasticity
                    parameters[1] = Section Moment of Inertia
                    parameters[2] = Purlin Spacing
                    parameters[3] = Beam Spacing
                for definition_type = SteelMemberRotationalRestraintType.TYPE_MANUALLY:
                    parameters[0] = Rotational Spring Stifness
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model / Types For Steel Design Member Rotational Restraints
        clientObject = model.clientModel.factory.create('ns0:steel_member_rotational_restraint')

        # Clears Object Attributes / Sets all the attributes to None
        clearAtributes(clientObject)

        # Member Rotational Restraint No.
        clientObject.no = no

        # Member Rotational Restraint Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Member Rotational Restraint Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Member Rotational Restraint Name
        if user_defined_name[0]:
            clientObject.user_defined_name_enabled = user_defined_name[0]
            clientObject.name = user_defined_name[1]
        else:
            clientObject.user_defined_name_enabled = user_defined_name[0]

        # Member Rotational Restraint Definition Type
        clientObject.type = definition_type.name

        # Member Rotational Restraint Categories
        if definition_type == SteelMemberRotationalRestraintType.TYPE_CONTINUOUS:
            clientObject.material_name = categories[0]
            clientObject.sheeting_name = categories[1]
            clientObject.position_of_sheeting = categories[2].name
            clientObject.continuous_beam_effect = categories[3].name
            clientObject.section_deformation_cdb = categories[4]
        elif definition_type == SteelMemberRotationalRestraintType.TYPE_DISCRETE:
            clientObject.material_name = categories[0]
            clientObject.section_name = categories[1]
            clientObject.rotational_stiffness = categories[2].name
            clientObject.continuous_beam_effect = categories[3].name
            clientObject.section_deformation_cdb = categories[4]

        # Member Rotational Restraint Parameters
        if definition_type == SteelMemberRotationalRestraintType.TYPE_CONTINUOUS:
            clientObject.modulus_of_elasticity = parameters[0]
            clientObject.sheeting_thickness = parameters[1]
            clientObject.sheeting_moment_of_inertia = parameters[2]
            clientObject.sheeting_distance_of_ribs = parameters[3]
            clientObject.width_of_section_flange = parameters[4]
            clientObject.spring_stiffness = parameters[5]
            clientObject.beam_spacing = parameters[6]

        elif definition_type == SteelMemberRotationalRestraintType.TYPE_DISCRETE:
            clientObject.modulus_of_elasticity = parameters[0]
            clientObject.section_moment_of_inertia = parameters[1]
            clientObject.purlin_spacing = parameters[2]
            clientObject.beam_spacing = parameters[3]

        elif definition_type == SteelMemberRotationalRestraintType.TYPE_MANUALLY:
            clientObject.total_rotational_spring_stiffness = parameters[0]

        #Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Adding Steel Member Rotational Restraint to Client Model
        model.clientModel.service.set_steel_member_rotational_restraint(clientObject)





