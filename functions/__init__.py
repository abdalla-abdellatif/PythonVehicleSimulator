# -*- coding: utf-8 -*-

from .kinematics import sat,Smtrx,Hmtrx,Rzyx,Tzyx,attitudeEuler,m2c,crossFlowDrag
from .mainLoop import simulate,simInfo
from .plotTimeSeries import plotVehicleStates, plotControls
from .guidance import refModel3
from .control import PIDpolePlacement