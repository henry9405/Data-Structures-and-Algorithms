import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    sentence = sentence.lower()

    # Split the sentence into words and count their frequencies
    word_list = sentence.split()
    frequency_dict = {}

    for word in word_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

# Test the function with the sample input
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
