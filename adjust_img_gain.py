import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# filename = R"C:\Users\zhangyue\OneDrive\报告\组会_20210905_MC仿真\照明视场\均匀光源\out_#photon480000000_a0.1_b0.4_g0.8_DiffuseTarget2D_distance8m_SingleLensDetector_3336x2706_detectorScale2.44318e-07_f0.01m_aperture0.05m_DivergentUniformPosition_angle0.0523599rad_FixTime.txt"

filename = R"D:\a.txt"
fs = cv2.FileStorage(filename, cv2.FILE_STORAGE_READ)
fn = fs.getNode("imgA")
img = np.array(fn.mat())
# 归一化
img_norm = (img-img.min())/(img.max()-img.min())
# gamma变换
gamma = 500
img_gamma = (img_norm ** 1/gamma)*255
cv2.imwrite("test.jpg",img_gamma)

