## This code

##Importing and loading the pre-trained skip-gram word2vec NLP model trained on 3 million words in 300 dimensions


from gensim import models
from gensim.models import KeyedVectors
import tkinter as tk

ml = models.KeyedVectors.load_word2vec_format(
    '/Users/arslanmac/GoogleNews-vectors-negative300.bin', binary=True)

## GUI for the function of the word2vec model that shows cosine similarity between 2 


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
root.title("Similarity")
canvas1.pack()


#The entry widget and box for the word 1

Word_1 = tk.Entry(root)
canvas1.create_window(200, 70, window = Word_1)


#The entry widget and box for the word 2

Word_2 = tk.Entry(root)
canvas1.create_window(200, 140, window = Word_2)


#The function that calculates the similarity beteween word 1 and word 2

def get_similarity():
    
    w1 = Word_1.get()
    w2 = Word_2.get()
    
    label1 = tk.Label(root, text = ml.distance(w1, w2))
    canvas1.create_window(200, 230, window=label1)
    

#Button that when pressed runs the function get_similarity()

button = tk.Button(root, text='Get Similarity', command = get_similarity)
canvas1.create_window(200, 180, window = button)

root.mainloop()

