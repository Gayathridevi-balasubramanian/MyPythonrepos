def sort_string(string):
    str_sorted = [(word.lower(),word) for word in string.split() ]
    print(type(str_sorted))
    str_sorted.sort()
    str = " ".join(word[1] for word in str_sorted)
    print(str)
    str = " ".join(word[0] for word in str_sorted)
    print(str)
    

sort_string("This is the string to be sorted")

'''  to sort an sentences 
        we need to split the sentences in the words and convert them to lower case
        into a list with words (actual) and with the lower case converted words
          sort the words based on the index
           and access the words (actual) in the sorted list with the capitalised sentences '''