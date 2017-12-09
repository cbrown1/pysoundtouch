[![Build Status](https://travis-ci.org/cbrown1/pysoundtouch.svg?branch=master)](https://travis-ci.org/cbrown1/pysoundtouch)

# pysoundtouch

A python binding to the soundtouch library.

At this point only one function is implemented: shift_pitch.

## Prerequisites

- [soundtouch](https://www.surina.net/soundtouch/)

## Installing

### Download:

```bash
git clone https://github.com/cbrown1/pysoundtouch.git
```

### Compile and install:

```bash
python setup.py build
sudo python setup.py install
```

## Usage
```python
alpha = -1 # shift 1 octave down in frequency
shift_pitch(sig, fs, alpha)
```

## Authors

- **Olli Parviainen** - Original soundtouch library

- **Christopher Brown**

## License

This project is licensed under the GPLv3 - see the [LICENSE.md](LICENSE.md) file for details.
