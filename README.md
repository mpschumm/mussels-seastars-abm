# mussels-seastars-abm
Using 3-D agent-based modeling to build a mechanistic understanding of mussel bed boundary formation.

To run on HPC:

1) Download NetLogo 6.0.4 (64-bit Linux) and unpack in home directory

2) Comment out the model code that sets values for turtle (agent) variables.

3) Increase heap size by editing ``netlogo-headless.sh`` to change
   ``-Xmx1024m`` to ``-Xmx2048m``

4) Create subdirectories ~/output and /scratch/t.cri.mschumm/results

5) Verify/edit configuration at the top of ``generate-experiments.py`` (e.g.,
   you may want to set the seed for the random number generator to make the
   result reproducible). Run this script to generate a list of experiments.

6) Verify/edit script (``mussels-seastars-abm.script``)

7) Upload the following files to your home directory:

   - ``mussels-seastars-abm.nlogo3d``
   - ``mussels-seastars-abm.script``
   - ``mussels-experiments.xml``

8) Submit job with:

       qsub mussels-seastars-abm.script

Make sure to save ``mussels-experiments.xml`` so that results can be
replicated (this includes not only the variable values for each run but also
the random number seed(s) used).

Also, remember that BehaviorSpace runs once *before* ``setup`` is run. Thus,
if you include something like ``clear-all`` in ``setup``, you will blow away
the variable values set by BehaviorSpace.

Support with Python and Java coding for use with cluster: Phil Schumm (pschumm)
