# -*- coding: utf-8 -*-

import numpy as np

from scipy.stats import _chk_asarray, _contains_nan


def rms(a, axis=None, *args, **kwargs):
    """
    Calculate the root mean square value of an array.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int or None, optional
        Axis along which to calculate the root mean square.
        Default is None. If None, compute over the whole array `a`.

    The remaining arguments are passed to `mean`.

    Returns
    -------
    y : ndarray
        The root mean square values.

    """
    a, axis = _chk_asarray(a, axis)
    return np.sqrt(np.mean(a**2, axis, *args, **kwargs))


def nanrms(a, axis=None, *args, **kwargs):
    """
    Calculate the root mean square value of an array, ignoring NaNs.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int or None, optional
        Axis along which to calculate the root mean square.
        Default is None. If None, compute over the whole array `a`.

    The remaining arguments are passed to `nanmean`.

    Returns
    -------
    y : ndarray
        The root mean square values.

    """
    a, axis = _chk_asarray(a, axis)
    return np.sqrt(np.nanmean(a**2, axis, *args, **kwargs))


def fano(a, axis=0, ddof=0, nan_policy='propagate'):
    """
    Compute the Fano factor, the ratio of the biased variance to the mean.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int or None, optional
        Axis along which to calculate the Fano factor.
        Default is 0. If None, compute over the whole array `a`.
    nan_policy : {'propagate', 'raise', 'omit'}, optional
        Defines how to handle when input contains nan. 'propagate' returns nan,
        'raise' throws an error, 'omit' performs the calculations ignoring nan
        values. Default is 'propagate'.

    Returns
    -------
    fano : ndarray
        The calculated Fano factoralong the requested axis.

    """
    a, axis = _chk_asarray(a, axis)

    contains_nan, nan_policy = _contains_nan(a, nan_policy)

    if contains_nan and nan_policy == 'omit':
        return np.nanvar(a, axis=axis, ddof=ddof) / np.nanmean(a, axis)

    return a.var(axis=axis, ddof=ddof) / a.mean(axis)


def signaltonoise(a, axis=0, ddof=0):
    """
    The signal-to-noise ratio of the input data.

    Returns the signal-to-noise ratio of `a`, here defined as the mean
    divided by the standard deviation.

    Parameters
    ----------
    a : array_like
        An array_like object containing the sample data.
    axis : int or None, optional
        Axis along which to operate. Default is 0. If None, compute over
        the whole array `a`.
    ddof : int, optional
        Degrees of freedom correction for standard deviation. Default is 0.

    Returns
    -------
    s2n : ndarray
        The mean to standard deviation ratio(s) along `axis`, or 0 where the
        standard deviation is 0.

    Note : This function is originally from scipy.  It has been removed.
    The code here is mostly the same as the original code.

    """
    a, axis = _chk_asarray(a, axis)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)
