# pytuning
musical tuning function used to create well tuned computers. sister to [tuning-js](https://github.com/kousun12/tuning-js)

## Usage

```python
from tuning import Tuning

# initialize with either scale ratio strings or cent values, per the .scl spec
basic = Tuning(['5/4', '233.9850002884625', '375.', '2'])

print(basic.ratios())
# [1.25, 1.5, 1.9152065613971474, 2.0]

print(basic.frequency(0))
# 440

print(basic.frequencies())
# [440, 550.0, 660.0, 842.6908870147448]

print(basic.frequencies(-1)) # frequencies for the octave below tonic
# [220.0, 275.0, 330.0, 421.3454435073724]

print(basic.frequency(0, 1)) # tonic frequency for 1 octave up
# 880


# Tuning where the second semitone of a 4 tone scale is pinned to 440 Hz
pinning = Tuning(['5/4', '233.9850002884625', '375.', '2'], (440, 1))

print(pinning.tonic_hz_raw)
# 352.0

print(pinning.frequencies())
# [352.0, 440.0, 528.0, 674.1527096117959]
```

As a bonus you can hear the mythical [well ascending shepard](https://colab.research.google.com/drive/1iDOjyfbgq4mPUXI6wdC0uTIlL2gHlNuO#scrollTo=e4C4PYN13QKY).
