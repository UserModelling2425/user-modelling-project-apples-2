#!/usr/bin/env python
import pandas as pd

def main():
    '''Preprocess data with random split to two sets, one for each block.'''

    # data is from https://github.com/fsense/parameter-stability-paper/blob/master/materials/list%20of%20materials.pdf
    #We use the first 74 words from the data used in Sense, Behrens, Meijer & Van Rijn (2015), which in turn is a subset from van den Broek, Segers, Takashima, & Verhoeven (2014).
    words = pd.read_csv("swahili_words.csv", sep=" ")

    # there are no duplicates
    #unq_words = words.drop_duplicates()
    #print(len(unq_words))

    # drop last row, to get even number of words for the 2 subsets
    even_words = words.head(-1)
    print(even_words)
    # random_state for reproducability
    first_set = even_words.sample(frac=0.5,random_state=123)
    #print(first_set, "\n\n\n")
    second_set = pd.concat([even_words,first_set]).drop_duplicates(keep=False)
    #print(second_set)

    # to csv
    first_set.to_csv('first_set_words.csv', index=False)
    second_set.to_csv('second_set_words.csv', index=False)



if __name__ == '__main__':
    main()