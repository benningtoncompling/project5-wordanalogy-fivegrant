class Vectors:
    # Pass in a list of readlines
    def __init__(self, *data):
        self.vectors = {}
        for line in data:
            key = (float(cell) for cell in data.split(' ')[1:])
            self.vectors.update({key:data.split(' ')[0]})

    def __str__(self):
        return '\n'.join([word + ': ' str(key) for key, 
         word in self.vectors.items()])

        
        
