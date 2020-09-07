# libprogress

[![Build Status](https://drone.bbaovanc.com/api/badges/bbaovanc/libprogress/status.svg)](https://drone.bbaovanc.com/bbaovanc/libprogress)

![PyPI](https://img.shields.io/pypi/v/libprogress)
![PyPI - License](https://img.shields.io/pypi/l/libprogress)

Package that allows easy generation of progress bars. Originally on my [NameGenerator](https://github.com/BBaoVanC/NameGenerator) project.

## Features

* Easy to use
* Imported as module
* Always tested before release
* Supports latest three versions of Python 3

---

## How to Install

Run the command `pip install libprogress`. If you want to specify a specific Python version to use for pip, use a command such as `pip3` or `pip3.8`.

---

## Documentation

### API

The following is an example that utilizes a progress bar with default length.

``` python
import libprogress

for i in range(20):  # example loop
    do(something)  # put the code to do what you are tracking the progress of
    print(libprogress.genbar(curprg=i+1, maxprg=20), end="\r")  # print progress
print(libprogress.genfullbar(prg=20))  # print the last bar
```

Final output:

``` plaintext
[####################] 100% [20/20]...done
```

If you don't put `end="\r"`, then each progress bar won't overwrite the last. The output will look like the following:

``` plaintext
[#-------------------] 5% [1/20]
[##------------------] 10% [2/20]
[###-----------------] 15% [3/20]
[####----------------] 20% [4/20]
[#####---------------] 25% [5/20]
[######--------------] 30% [6/20]
[#######-------------] 35% [7/20]
[########------------] 40% [8/20]
[#########-----------] 45% [9/20]
[##########----------] 50% [10/20]
[###########---------] 55% [11/20]
[############--------] 60% [12/20]
[#############-------] 65% [13/20]
[##############------] 70% [14/20]
[###############-----] 75% [15/20]
[################----] 80% [16/20]
[#################---] 85% [17/20]
[##################--] 90% [18/20]
[###################-] 95% [19/20]
[####################] 100% [20/20]
[####################] 100% [20/20]...done
```

---

## License

_libprogress_ is licensed under the GPLv3 license. For more information, please refer to [`LICENSE`](https://git.bbaovanc.com/bbaovanc/libprogress/src/branch/master/LICENSE).
