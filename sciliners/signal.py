# -*- coding: utf-8 -*-

import numpy as np


def pow2db(x, ref=None):
    """
    Convert linear power values to decibel values
    relative to a reference power value.

    Parameters
    ----------
    x : array_like
        Power values.
    ref : array_like, optional
        Reference power level the decibels are calculated relative to.
        Default is 1.

    Returns
    -------
    y : ndarray
        The values of `x` in decibels.

    """
    x = np.asarray(x)
    if ref is None:
        return 10.*np.log10(x)
    else:
        ref = np.asarray(ref)
        return 10.*np.log10(x/ref)


def mag2db(x, ref=None):
    """
    Convert linear magnitude values to decibel values
    relative to a reference magnitude value.

    Parameters
    ----------
    x : array_like
        Magnitude values.
    ref : array_like, optional
        Reference magnitude level the decibels are calculated relative to.
        Default is 1.

    Returns
    -------
    y : ndarray
        The values of `x` in decibels.

    """
    x = np.asarray(x)
    if ref is None:
        return 20.*np.log10(x)
    else:
        ref = np.asarray(ref)
        return 20.*np.log10(x/ref)


def db2pow(y, ref=None):
    """
    Convert decibel values to linear power values
    relative to a reference power value.

    Parameters
    ----------
    x : array_like
        Decibel values.
    ref : array_like, optional
        Reference power level the decibels were calculated relative to.
        Default is 1.

    Returns
    -------
    y : ndarray
        The values of `x` in linear power.

    """
    x = np.asarray(x)
    if ref is None:
        return 10.**(y/10.)
    else:
        ref = np.asarray(ref)
        return 10.**(y/10.)*ref


def db2mag(y, ref=None):
    """
    Convert decibel values to linear magnitude values
    relative to a reference magnitude value.

    Parameters
    ----------
    x : array_like
        Decibel values.
    ref : array_like, optional
        Reference magnitude level the decibels were calculated relative to.
        Default is 1.

    Returns
    -------
    y : ndarray
        The values of `x` in linear magnitude.

    """
    x = np.asarray(x)
    if ref is None:
        return 10.**(y/20.)
    else:
        ref = np.asarray(ref)
        return 10.**(y/20.)*ref
