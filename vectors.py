from math import *
import numpy

class Vectors:
    # Pass in a list of readlines
    def __init__(self, data, similarity, normalize):
        self.vectors = {}
        self.similarity = int(similarity)
        for line in data:
            line = line.strip('\n')
            vec = [float(cell) for cell in line.split(' ')[1:]]
            self.vectors.update({line.split(' ')[0]: numpy.array(vec)})
        if bool(normalize):
            for word, vector in self.vectors.items():
                length = sqrt(sum([element**2 for element in vector]))
                self.vectors[word] = numpy.array([element/length for element in vector])

    def __str__(self):
        spit = ''
        for word, vec in self.vectors.items():
            processed = str([str(element) for element in list(vec)])
            spit += word + ': ' + processed + '\n'
        return spit

    def d_val(self, problem):
        try:
            d_vec = self.vectors[problem.base_pair[1]] - \
             self.vectors[problem.base_pair[0]]
            d_vec += self.vectors[problem.sec_pair[0]]
             
            distances = {}
            distance = None
            for word, vector in self.vectors.items():
                #el means element

                # Euclidian
                if self.similarity == 0:
                    distance = sqrt(numpy.sum(numpy.square(vector - d_vec)))

                # Manhattan 
                elif self.similarity == 1:
                    distance = numpy.sum(vector - d_vec)

                # Cosine
                ## https://en.m.wikipedia.org/wiki/Cosine_similarity
                ## Said we could just do dot product in class
                else:
                    distance = vector.dot(d_vec)

                distances.update({distance:word})

            word_ref = None
            if self.similarity > 1:
                word_ref = max(distances.keys())
            else:
                word_ref = min(distances.keys())
            d_word = distances[word_ref]
            problem.solve(d_word)
            return problem

        except KeyError: 
            problem.solve("FAILURE")
            return problem
        
