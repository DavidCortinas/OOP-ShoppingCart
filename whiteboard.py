def length_of_last_word(s):
    s = s.split(" ")
    return len(s[-1])
    # s_list = s.split()
    # last_word = s_list[-1]
    # length = len(last_word)
    # return length
        
print(length_of_last_word("Hello World"))
