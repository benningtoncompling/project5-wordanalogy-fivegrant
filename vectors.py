import numpy
import math

class Vectors:
    # Pass in a list of readlines
    def __init__(self, data, similarity, normalize):
        self.vectors = {}
        self.similarity = similarity
        for line in data:
            line = line.strip('\n')
            key = numpy.array([float(cell) for cell in line.split(' ')[1:]])
            self.vectors.update({key:line.split(' ')[0]})
        if normalize:
            for word, vector in self.vectors.items():
                length = sqrt(sum([element**2 for element in vector]))
                self.vectors[word] = [element/length for element in vector]

    def __str__(self):
        return '\n'.join([word + ': ' + str(key) for key, 
         word in self.vectors.items()])

    def euclidian(self, compare):
        distances = {}
        for word, vector in self.vectors:
            distance = sqrt(sum(element**2 for element in (vector - compare)))
        word_ref = min(distances.keys())
        return distances[word_ref]

    def manhattan(self, compare):
        distances = {}
        for word, vector in self.vectors:
            distance = sum(for element in (vector - compare))
        word_ref = min(distances.keys())
        return distances[word_ref]

# https://en.m.wikipedia.org/wiki/Cosine_similarity
    def cosine(self, compare):
        distances = {}
        for word, vector in self.vectors:
            denominator = sqrt(sum([element**2 for element in vector])) * \
             sqrt(sum([element**2 for element in compare]))
            distance = vector.dot(compare)/denominator
        word_ref = max(distances.keys())
        return distances[word_ref]

    def d_val(self, problem):
        d_vec = problem.base_pair[1] - problem.base_pair[0]
        d_vec += problem.sec_pair[0]
        d_word = self.euclidian(d_vec) if self.similarity == 0 else \
         self.manhattan(d_vec) if self.simliarity == 1 else \
         self.cosine(d_vec)
        problem.solve(d_word)
        return problem
        
#nvrmnd we can use numpy
#    def d_vector(self, a_vec, b_vec, c_vec):
#        return tuple(c_vec[i] + b_vec[i] - a_vec[i] \
#         for i in range(0, a_vec(length))
        

        
        
