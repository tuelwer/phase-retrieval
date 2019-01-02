import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
from phase_retrieval import fienup_phase_retrieval

np.random.seed(1)
image = scipy.ndimage.imread('test.png', flatten=True)
magnitudes = np.abs(np.fft.fft2(image))
result = fienup_phase_retrieval(magnitudes, steps=500,
                                verbose=False)

plt.show()
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Image')
plt.subplot(122)
plt.imshow(result, cmap='gray');
plt.title('Reconstruction')
plt.show()
