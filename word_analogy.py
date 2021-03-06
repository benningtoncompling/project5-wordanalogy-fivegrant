#!/usr/bin/env python3
from problems import *
from vectors import *
import sys, os

vector_content = ''
with open(sys.argv[1]) as file:
    vector_content = Vectors(file.readlines(), sys.argv[6], sys.argv[5])

for access in os.listdir(sys.argv[2]):
    if access.endswith('.txt'):
        print(access)
        with open(os.path.join(sys.argv[2], access), 'r') as file:
            correct = [0,0]
            with open(os.path.join(sys.argv[3], access), 'w') as output:
                for line in file.readlines():
                    correct[1] += 1
                    analogy = Problem(line.split(' '))
                    guess =  vector_content.d_val(analogy.blind())
                    if analogy.quality_check(guess):
                        correct[0] += 1
                    output.write(str(guess))
                
            eval_file = sys.argv[3] + '/eval.txt'
            with open(eval_file, 'a') as eval:
                eval.write(access)
                eval.write(f'\nACCURACY TOP1: {correct[0]/correct[1]}% ({correct[0]}/{correct[1]})\n')
