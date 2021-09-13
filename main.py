#MAIN

import numpy as np
import vtk
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as colors
import array
import yt
import trident


from vtk import vtkStructuredPointsReader
from vtk.util import numpy_support as VN
from matplotlib.colors import LogNorm

from numpy.random import multivariate_normal

simultype = ['', '-Al']
#simultype = ['_turb', '2AlTurb']
#simultype = ['_rad', '2-rad']
#simultype = ['_turb_rad', '2AlTurb-rad']

#DOWN-THE-BARREL

#ray_start = [0, -2, 0]
#ray_end   = [0, 22, 0]
#orient    = '-dtb'

#EDGE-ON

ray_start = [0., 10., -6.]
ray_end   = [0., 10., 6.]
orient    = '-eo'

for i in range(4):
    if i == 0:
        tstep = 0  #initial
    elif i == 1:
        tstep = 5  #compression
    elif i == 2:
        tstep = 30 #stripping
    else:
        tstep = 45 #break-out

    file_name = 'data.' + str(tstep).zfill(4) + '.vtk'
    input_directory = 'Wind_cloud'+ simultype[0] + '/Wind-Cloud-MHD' + simultype[1] +'/'
    output_directory = 'Wind_cloud' + simultype[0] + '/Spectral_analysis' + simultype[0] +'/'

    ds = fieldanalysis_yt(file_name, input_directory)
    spectra(output_directory, ds, tstep, simultype, orient, ray_start, ray_end)
