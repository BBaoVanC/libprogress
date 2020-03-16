#!/usr/bin/env python3
"""
NameGenerator Progress Package.

by BBaoVanC

This package allows easy generation of progress bars.

Copyright (C) 2020 BBaoVanC
"""


# Generate bar
def genbar(length=20, curprg=0, maxprg=100):
    """
    Generate a progress bar.

    Arguments:
    length -- the length of the bar
    curprg -- the current progress
    maxprg -- the maximum progress

    The design of the progress bar:
    [#####---------------] 25% [253/1000]
    """
    percent = round(curprg / maxprg, 2)  # percentage has two decimal places
    barsfilled = int(round(length * percent, 0))  # calculate bars filled
    barsunfilled = int(length - barsfilled)  # calculate bars not filled
    progbar = "[{}{}]".format("#" * barsfilled, "-" * barsunfilled)  # make bar
    barinfo = "{}% [{}/{}]".format(int(percent * 100), curprg, maxprg)
    return "{} {}".format(progbar, barinfo)  # return output


# Generate a full bar
def genfullbar(length=20, prg=100):
    """
    Generate a filled progress bar.

    Arguments:
    length -- the length of the bar
    prg -- the progress total

    The design of the progress bar:
    [####################] 100% [1000/1000]...done
    """
    fullbar = "{}...done".format(genbar(length, prg, prg))
    return fullbar
