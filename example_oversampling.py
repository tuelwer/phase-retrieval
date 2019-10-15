import numpy as np
import imageio
import matplotlib.pyplot as plt
from phase_retrieval import fienup_phase_retrieval

np.random.seed(12345)
image = imageio.imread('cameraman.png', as_gray=True)
magnitudes = np.abs(np.fft.fft2(image))
result = fienup_phase_retrieval(magnitudes,
                                steps=1000,
                                verbose=False)

image_padded = np.pad(image, 128, 'constant')
magnitudes_oversampled = np.abs(np.fft.fft2(image_padded))
mask = np.pad(np.ones((256,256)), 128, 'constant')
result_oversampled = fienup_phase_retrieval(magnitudes_oversampled,
                                            steps=1000,
                                            mask=mask,
                                            verbose=False)

plt.figure(figsize=(10,10))
plt.subplot(221)
plt.imshow(image, cmap='gray')
plt.title('Image')
plt.subplot(222)
plt.imshow(result, cmap='gray')
plt.title('Result')
plt.subplot(223)
plt.imshow(image_padded, cmap='gray')
plt.title('Image padded')
plt.subplot(224)
plt.imshow(result_oversampled, cmap='gray');
plt.title('Reconstruction oversampled')
plt.show()
