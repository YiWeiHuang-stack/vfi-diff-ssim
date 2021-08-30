import cv2
from skimage.measure._structural_similarity import structural_similarity as compare_ssim

# 计算指标
def calc_index(i0,i1,interp):
    left_diff = 1 - compare_ssim(interp,i0,multichannel=True)
    right_diff = 1 - compare_ssim(interp,i1,multichannel=True)
    return abs(left_diff - right_diff)

im1 = cv2.imread('')
im2 = cv2.imread('')
print(calc_index(im1,im2))