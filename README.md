# Phase retrieval: Fienup's algorithms
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python implementation of Fienup's phase retrieval algorithms, which allow reconstruction of greyscale images only from measurements of the magnitudes. The following methods are implemented:
- input-output algorithm
- output-output algorithm
- hybrid input-output algorithm

## Example

```python
image = scipy.ndimage.imread('test.png', flatten=True)
magnitudes = np.abs(np.fft.fft2(image))
result = fienup_phase_retrieval(magnitudes, steps=500, verbose=False)
```

## Requirements
- Python (>= 3.6.5)
- NumPy (>= 1.15.4)

## References
[1] E. Osherovich, Numerical methods for phase retrieval, arXiv:1203.4756, 2012
    
[2] J. R. Fienup, Phase retrieval algorithms: a comparison, Applied Optics, 1982
    
[3] https://github.com/cwg45/Image-Reconstruction
