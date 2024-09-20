from matplotlib import pyplot as plt 
import numpy as np


def kalman_process(x_est_prev,P_est_prev,dm,z):
  A = np.squeeze(dm)
  H = np.identity(4)
  Q = np.identity(4)
  R =  np.identity(4)
  
  x_est = A * x_est_prev
  P = A * P_est_prev * A.transpose() + 100 * Q
  temp = H * P * H.transpose() + 0.01 * R
  K = P * H.transpose() * np.linalg.inv(temp);
  x_est = x_est + K * (z - H * x_est);
  P_est = (np.identity(4) - K * H) * P
  
  return [x_est,P_est]
  

  # Q = Q_discrete_white_noise(dim=dimension, dt=0.1, var=0.13)
def test(ticker):
  dm = np.load(f"npy_files/{ticker}_dm.npy")
  data = np.load(f"npy_files/{ticker}_quote_data.npy")
  out = []
  ctrl = []
  x_est_prev = np.zeros(4)
  P_est_prev = np.identity(4)
  for i in range(0, data.shape[1]):
    z = data[0:4,i]
    [x_est, P_est] = kalman_process(x_est_prev,P_est_prev,dm,z)
    out.append(x_est[0][0])
    ctrl.append(z[0])
    x_est_prev = x_est
    P_est_prev = P_est
    
  fig, ax = plt.subplots()
  ax.plot(out)
  ax.plot(ctrl)
  plt.show()
    
  