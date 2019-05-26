mkdir output00 output01 output02 output10 output11 output12
./word_analogy.py vector_model_5_10.txt GoogleTestSet output00 output00/eval.txt 0 0 &
./word_analogy.py vector_model_5_10.txt GoogleTestSet output01 output01/eval.txt 0 1 &
./word_analogy.py vector_model_5_10.txt GoogleTestSet output02 output02/eval.txt 0 2 &
./word_analogy.py vector_model_5_10.txt GoogleTestSet output10 output10/eval.txt 1 0 &
./word_analogy.py vector_model_5_10.txt GoogleTestSet output11 output11/eval.txt 1 1 &
./word_analogy.py vector_model_5_10.txt GoogleTestSet output12 output12/eval.txt 1 2 &
