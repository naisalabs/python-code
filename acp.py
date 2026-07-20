class ReverseString:
    def reverse_words(self, text):
        words = text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)
    
# create and obj
obj = ReverseString()


# get input from the user
sentence = input("enter a sentence: ")


print("reversed sentence:")
print(obj.reverse_words(sentence))