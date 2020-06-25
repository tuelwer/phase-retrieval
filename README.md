# Phase retrieval: Fienup's algorithms
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python implementation of Fienup's phase retrieval algorithms, which allow reconstruction of greyscale images only from measurements of the magnitudes. The following methods are implemented:
- input-output algorithm
- output-output algorithm
- hybrid input-output algorithm

## Example

```python
image = imageio.imread('test.png', as_gray=True)
magnitudes = np.abs(np.fft.fft2(image))
result = fienup_phase_retrieval(magnitudes, steps=500, verbose=False)
```

## Requirements
- Python (>= 3.7.3)
- NumPy (>= 1.17.2)
- matplotlib (tested with 3.1.1) 
- imageio (tested with 2.6.0)

## References
[1] E. Osherovich, Numerical methods for phase retrieval, arXiv:1203.4756, 2012
    
[2] J. R. Fienup, Phase retrieval algorithms: a comparison, Applied Optics, 1982
    
[3] https://github.com/cwg45/Image-Reconstruction
