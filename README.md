[![Build Status](https://travis-ci.org/cbrown1/pysoundtouch.svg?branch=master)](https://travis-ci.org/cbrown1/pysoundtouch)

# pysoundtouch

A python binding to the soundtouch library.

This is the same code as [recapture](https://gist.github.com/jedahu/5028736#file-multichannel-play-record-jack-md) with a few minor bugfixes, and improved logging and option handling. But the essential code is identical.

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
