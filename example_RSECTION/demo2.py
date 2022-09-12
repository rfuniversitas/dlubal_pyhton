#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/..')


from RSECTION.initModel import Model
from RSECTION.BasicObjects.material import Material
from RSECTION.BasicObjects.section import Section
from RSECTION.BasicObjects.point import Point
from RSECTION.BasicObjects.line import Line
from RSECTION.BasicObjects.part import Part
from RSECTION.BasicObjects.opening import Opening
from RSECTION.enums import LineArcAlphaAdjustmentTarget, PointReferenceType

if __name__ == '__main__':

    Model(True, "Demo2") # crete new model called Demo

    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    # Section(1, 'IPE 200')

    Point(1, 1, 1)
    Point(2, 1, -1)
    Point(3, -1, -1)
    Point(4, -1, 1)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')
    Line.Circle(5, [0, 0], 0.5)

    Part(1, '1 2 3 4')

    Opening(1, '5')

    Model.clientModel.service.finish_modification()

