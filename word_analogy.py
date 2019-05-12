#!/usr/bin/env python3
from problems import *
from vectors import *
import sys, os

vector_content = ''
with open(sys.argv[1]) as file
    vector_content = Vectors(file.readlines(), sys.argv[6], sys.argv[5])

for access in os.listdir(sys.argv[2]):
    if access.endswith('.txt'):
        filepath = os.path.join(sys.argv[2], access)
	with open(filepath, 'r') as file:
            with open(sys.argv[3], access) as output:
                correct = [0,0]
                for line in file.readlines():
                    correct[1] += 1
                    analogy = Problem(line.split(' '))
                    guess =  vector_content.d_val(analogy.blind())
                    if analogy == guess:
                        correct[0] += 1
                    output.write(guess)
                
            eval_file = os.path.join(sys.argv[3], 'eval.txt')
            with open(output, 'w') as evaluation:
                evalutation.write(access)
                evalutation.write('ACCURACY TOP1: ' + \
                 str(correct[0]/correct[1]) + '(' + str(correct[0]) + \
                 '/' + str(correct[1]))
                

            
