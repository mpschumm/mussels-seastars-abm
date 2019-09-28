#!/usr/bin/env python

"""Generate BehaviorSpace XML file for use with NetLogo"""

import itertools
import random

# Set seed to specific integer to make result reproducible
random.seed(88804688)

OUTFILE = 'mussels-experiments.xml'

SETUP = {'repetitions':4,
         'steps':2008,
         'runMetricsEveryStep':'false',
         'setup':'setup',
         'go':'go',
         'final':'export-world "/scratch/t.cri.mschumm/results/World-{0}.csv"',
         'metric':'count turtles'}

VARS = {'disturbance-intensities':[0, 6.5, 8.5],
        'seastar-desiccation-coef':[0.05, 0.1],
        'starting-mussels':[0, 1000],
        'disturbance-freq':[182.5, 365],
        'predation-intensity':[1, 0.156],
        'growth-param':[-7.0E-4, -0.007, -0.07],
        'bed-thickness':[1, 1.05],
        'protection':[1, 0]}

def exp_header(exp_no):
    SETUP['exp_no'] = exp_no
    header = """  <experiment name="experiment-{exp_no}" repetitions="1" runMetricsEveryStep="{runMetricsEveryStep}">
    <setup>{setup}</setup>
    <go>{go}</go>
    <final>{final}</final>
    <timeLimit steps="{steps}"/>
    <metric>{metric}</metric>
""".format(**SETUP)
    return header.format(exp_no)

def format_vals(varname, values):
    result = []
    for value in values:
        result.append("""    <enumeratedValueSet variable="{0}">
      <value value="{1}"/>
    </enumeratedValueSet>\n""".format(varname, value))
    return result

def value_combinations():
    varlist = []
    for var in VARS:
        varlist.append(format_vals(var, VARS[var]))
    return list(itertools.product(*varlist))

with open(OUTFILE,'w') as file:
    exp_no = 0
    file.write('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE experiments SYSTEM "behaviorspace.dtd">\n<experiments>\n')
    for experiment in value_combinations():
        for rep in range(SETUP['repetitions']):
            exp_no = exp_no + 1
            file.write(exp_header(exp_no))
            file.write(format_vals('random-seed', [random.randint(-2147483648,2147483647)])[0])
            for variable in experiment:
                file.write(variable)
            file.write('  </experiment>\n')
    file.write('</experiments>\n')
