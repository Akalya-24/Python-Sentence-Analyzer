import string

def count_words(sentence):
    words = sentence.split()
    return len(words)


def find_longest_word(sentence):
    words = sentence.split()

    if not words:
        return "No words found"

    clean_words = [
        word.strip(string.punctuation) for word in words
    ]

    return max(clean_words, key=len)


def reverse_sentence(sentence):
    return sentence[::-1]


def check_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def main():
    sentence = input("Enter a sentence: ")
    number = int(input("Enter a number: "))

    print("\n--- SENTENCE ANALYSIS ---")
    print("Word Count:", count_words(sentence))
    print("Longest Word:", find_longest_word(sentence))
    print("Reversed Sentence:", reverse_sentence(sentence))

    print("\n--- PRIME NUMBER CHECK ---")

    if check_prime(number):
        print(number, "is a Prime Number")
    else:
        print(number, "is not a Prime Number")


main()
