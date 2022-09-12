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
from RSECTION.enums import LineArcAlphaAdjustmentTarget, PointReferenceType

if __name__ == '__main__':

    Model(True, "Demo") # crete new model called Demo

    Model.clientModel.service.begin_modification()

    Material(1, 'S235')

    # Section(1, 'IPE 200')

    Point(1, 0.0, 0.2)
    Point(2, 0.2, 0,0)
    Point.Standard(3, 2, [0.0,0.2])
    Point.BetweenTwoPoints(4, 1, 2, PointReferenceType.REFERENCE_TYPE_L, [True, 0.5], -0.1)
    Point.BetweenTwoPoints(5, 1, 3, PointReferenceType.REFERENCE_TYPE_Y, [False, 0.08], -0.1)
    # Point.BetweenTwoPoints(6, 1, 3, PointReferenceType.REFERENCE_TYPE_L, [True, 50], 0.1)
    Point.BetweenTwoPoints(6, 1, 3, PointReferenceType.REFERENCE_TYPE_L, [True, 0.5], 0.1)
    # Point.BetweenTwoPoints(7, 1, 2, PointReferenceType.REFERENCE_TYPE_Y, [False, 0.101], 0.1)
    Point.BetweenTwoLocations(7, 0.0, 0.0, -0.2, 0.4, PointReferenceType.REFERENCE_TYPE_L, [True, 0.5], 0.0)
    Point.BetweenTwoLocations(8, -0.2, 0.0, 0.0, 0.4, PointReferenceType.REFERENCE_TYPE_Z, [False, 0.2], -0.1)
    # Point.DeletePoint('7 8')
    Point(10, 0, -0.2)
    Point(11, 0.6, -0.2)

    Line(1, '1 2')
    Line.Polyline(2, '1 3')
    Line.Arc(3, [1, 3], [0.1,0.3], LineArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_ARC_CONTROL_POINT)
    Line.Circle(4, [-0.1, 0.0], 0.1)
    Line.Ellipse(5, [7 ,8], [-0.15,0.16])
    Line.Parabola(6, [1, 8], [-0.15,0.35], 0.1)
    Line.NURBS(7,'10 11', [[0,-0.2], [0.2,-0.3],[0.4,-0.1],[0.6,-0.2]],[1,1,1,1],3)
    # Line.DeleteLine('4 6')

    Point.OnLine(9, 1, PointReferenceType.REFERENCE_TYPE_Y, [False, 0.1])


    Model.clientModel.service.finish_modification()

