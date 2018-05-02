from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi, sqrt, cos, log10
import os

class ConstantVolume:
    # def timeSeries(startDate=None, endDate=None, timestep=None, boundarycondition=None):
        #generate time series

    def constantVolume(model_segs):
        time_s = np.arange(startDate, endDate, timestep)
        nsegments = len(model_segs)
        names = list(model_segs['name'])
        names.insert(0, "t")
        names.insert(1, "flow_in")
        Q_out = pd.DataFrame(np.zeros((len(time_s), nsegments+2)), columns=names)
        Q_out['t'] = time_s
        for t in range((len(time_s))):
            for i in range(nsegments):
                Q_out.iloc[t, i + 2] = Q_out.iloc[t, i + 1]  # + tributary flow

