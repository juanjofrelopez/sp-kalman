from pydmd import DMDc
from pydmd import DMD
from pydmd.plotter import plot_summary
import numpy as np


def fit(ticker):
  # format : ['open','close','high','low','volume']
  data = np.load(f"npy_files/{ticker}_quote_data.npy")
  inputs = data[0:4,:]
  control = data[4,:]
  dmd = DMD()
  dmd.fit(inputs)
  dynamic_modes = dmd.modes
  np.save(f"npy_files/{ticker}_dm",dynamic_modes)
  # dmdc = DMDc()
  # dmdc.fit(inputs,control)
  # plot_summary(dmdc)
  