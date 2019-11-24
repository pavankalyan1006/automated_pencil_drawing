import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import fftconvolve

from src.blend import composite_paper
from src.edge import get_edge_img
from src.multi_res import get_mr_img_from_rgb_img
from src.stroke import get_stroke_img
from src.utilities import show_img
from src.multi_res_lic import get_mrl

img_path = "../images/castle.jpeg"
img = cv2.imread(img_path)
bg_img = cv2.imread("paper.jpg")

if img_path == "../images/castle.jpeg":
    print(img.shape)
    img = cv2.resize(img, None, fx=2.0, fy=2.0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mr_img = get_mr_img_from_rgb_img(img)
_, _, edge_img = get_edge_img(mr_img, thresh=110, thresh2=0.1)
mrl_img = get_mrl(img)
strk_img = get_stroke_img(edge_img, mrl_img)
out = composite_paper(strk_img, bg_img,0.4)

edge_img = edge_img.astype(np.uint8)
show_img(img, splt=321,gray=False, title="Input")
show_img(edge_img, splt=322, title="Edge Image")
show_img(mrl_img, splt=323, title="Multi-resolution LIC Image")
show_img(strk_img, splt=324, title="Stroke Image")
show_img(out, splt=325, title="Output")
plt.show()
plt.figure()
plt.suptitle("Final Output")
show_img(img, splt=121, title="Input")
show_img(out, splt=122, title="Output")
plt.show()
plt.figure()
for ind, i in enumerate(range(3,9)):
    out = composite_paper(strk_img, bg_img, alpha=i/10)
    show_img(out, splt=321+ind)
plt.show()