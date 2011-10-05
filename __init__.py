'''
SNPY 1.0
Author:  Chris Burns (cburns@ociw.edu)

SNPY (or SNOOPY) is a Python package for fitting the light-curves of TypeIa
supernovae.  It is NOT an off-the-shelf program that will do all the work
for you from the command line.  It is meant to be run interactively.  It
provides many tools, but does not lock you into a specific routine for fitting
and therefore allows for a great deal of customization.  The package also 
contains a number of stand-alone sub-packages that can be installed seperately.

Documentation can be found the the doc/ directory under the source tree.  But
briefly, here is what SNOOPY can do:

   - Fit lightcurve templates to data.  These templates were constructed
     from the Carnegie Supernova Project's low-z data set (as outlined in
     Contreras et al. (2009) and Follatelli et al. (2009)).  These include
     templates for the CSP uBVgriYJH filter set.  You can also use Jose-
     Louis Prieto's templates to fit Johnson/Kron/Cousins BRVI lightcurves.

   - Using templates, fit for distance (and dm15, E(B-V), stretch, time of 
     maximum, etc.  This uses the calibration of Follatelli et al. (2009) 
     for the CSP filter set, or Prieto et al. (2006) for the BVRI set.

   - Alternatively, fit for light-curve parameters only (dm15, stretch,
     time of maximum, maximum light, colors, etc).

   - Compute k-corrections based on the spectral energy distribution
     template of Hsiao et al. (2007).  This includes color-matching the
     SED template to the observed filters.  You can do plain K-corrections
     or cross-band K-corrections.

   - Fit splines to light-curves to do your own analysis, independent of the
     light-curve templates.

   - Built-in Lira Law to estimate E(B-V).

   - Various plotting routines.

   - Interact with a properly set-up SQL database.

The subpackages include:

   - filters:   a package for working with filter systems.  computing
     zero-points, producing synthetic spectra, etc.

   - dm15temp:  a python wrapper to Jose-Louis Prieto's light-curve
     generator

   - CSPtemp:  a generator for the CSP light-curve templates.

   - dust_getval:  Compute the E(B-V) by Milky way using the Schlegel
     dust maps.

   - spline2:  a python wrapper to the Hyperspline (or spline2) algorithm,
     which uses the Durbin-Watson statistic rather than chi-square.  Good
     if you don't trust your error bars.

   - tspack:  a python wrapper to the TSPACK library:  generating tension
     splines.'''

from sn import *
