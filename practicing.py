import math
class Integer_Info(object):
    #reverse the integer reverse_int
    #check if it's prime is_prime

    def reverse_int(self, num):
        #reverses the integer but keeps the sign still
        result = 0
        if num>0:
            while num>0:
                result = (result*10) + (num%10)
                num = int(num/10)
            return result
        else:
            num = num*-1
            while num>0:
                result = (result*10) + (num%10)
                num = int(num/10)
            return result * -1

    def is_prime(self, num):

        def pos_is_prime(var):
            #function to find prime regardless of sign
            if var<4:
                return True
            for i in range(2,int(math.sqrt(var))+1):
                if var%i == 0:
                    return False
            return True

        if num>0:
            #num is positive
            return pos_is_prime(num)
        else:
            #num is negative
            num = num *-1
            return pos_is_prime(num)


class Word_Info(object):
    #is_palindrome and other_is_palindrome checks if word is palindrome
    #is_anagram

    def is_palindrome(self, word):
        #reverse word and check if it's the same
        word_list = (word.lower())
        return word_list == word_list[::-1]

    def other_is_palindrome(self, word):
        #get the last letter and first letter check if it's same do in increments
        word = word.lower()
        length = len(word)
        for i in range(int(length / 2)):
            last_index = length - 1 - i
            if word[i] != word[last_index]:
                return False
        return True

    def is_anagram(self,word, other_word):
        #check if word is anagram but not the same word
        word = word.lower()
        other_word = other_word.lower()
        if word == other_word:
            return False
        if sorted(word)==sorted(other_word):
            return True
        else:
            return False

