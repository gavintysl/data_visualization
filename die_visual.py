# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 02:13:51 2018

@author: tysl
"""

from die import Die

import pygal

# Create a D6.
die = Die()

# Make some rolls, and store the results in alist
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)
    
# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')