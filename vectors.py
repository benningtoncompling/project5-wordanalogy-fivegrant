from math import *
from numpy import array

class Vectors:
    # Pass in a list of readlines
    def __init__(self, data, similarity, normalize):
        self.vectors = {}
        self.similarity = similarity
        for line in data:
            line = line.strip('\n')
            vec = [float(cell) for cell in line.split(' ')[1:]]
            self.vectors.update({line.split(' ')[0]: vec})
        if bool(normalize):
            for word, vector in self.vectors.items():
                length = sqrt(sum([element**2 for element in vector]))
                self.vectors[word] = [element/length for element in vector]

    def __str__(self):
        spit = ''
        for word, vec in self.vectors.items():
            processed = str([str(element) for element in list(vec)])
            spit += word + ': ' + processed + '\n'
        return spit

    def euclidian(self, compare):
        distances = {}
        for word, vector in self.vectors.items():
            #if list(compare) != vector:
            distance = sqrt(sum(element**2 for element in \
             (array(vector) - compare)))
            distances.update({distance:word})
        word_ref = min(distances.keys())
        return distances[word_ref]

    def manhattan(self, compare):
        distances = {}
        for word, vector in self.vectors.items():
            distance = sum(element for element in (array(vector) - compare))
            distances.update({distance:word})
        word_ref = min(distances.keys())
        return distances[word_ref]

# https://en.m.wikipedia.org/wiki/Cosine_similarity
    def cosine(self, compare):
        distances = {}
        for word, vector in self.vectors.items():
            denom = sqrt(sum([element**2 for element in array(vector)])) \
             * sqrt(sum([element**2 for element in compare]))
            distance = array(vector).dot(compare)/denom
            distances.update({distance:word})
        word_ref = max(distances.keys())
        return distances[word_ref]

    def d_val(self, problem):
        d_vec = array(self.vectors[problem.base_pair[1]]) - \
         array(self.vectors[problem.base_pair[0]])
        d_vec += array(self.vectors[problem.sec_pair[0]])
        d_word = self.euclidian(d_vec) if self.similarity == '0' else \
         self.manhattan(d_vec) if self.similarity == '1' else \
         self.cosine(d_vec)
        problem.solve(d_word)
        return problem
        
#nvrmnd we can use numpy
#    def d_vector(self, a_vec, b_vec, c_vec):
#        return tuple(c_vec[i] + b_vec[i] - a_vec[i] \
#         for i in range(0, a_vec(length))
        

        
        
