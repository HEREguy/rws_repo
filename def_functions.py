#Create a function that calls a string with a mix of lower and upper case letters
# using even and odd similar to this example "dEcEmBeR"

'''def rfunc(ex):
    mylist = []
    for letter in range(len(ex)):
        if letter %2==0:
            mylist.append(ex[letter].upper())
        else:
            mylist.append(ex[letter].lower())
    return ''.join(mylist)

result = rfunc('hollywood')

print(result)'''

#03-Methods and Functions exercises

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

'''def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

result = lesser_of_two_evens(1110,248)
print(result)'''

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

'''def animal_crackers(x):
    words = x.lower().split()
    return words[0][0] == words[1][0]

result = animal_crackers('yes yellow')
print(result)'''

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

'''def makes_twenty(n1,n2):
    if (n1 + n2) == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False

result = makes_twenty(18,2)
print(result)'''

'''def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

result = old_macdonald('macdonald')

print(result)'''


#MASTER YODA: Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'#
'''def reverse_word(text):
    words = text.split()
    reverse = words[::-1]
    return ' '.join(reverse)

result = reverse_word('I am sleepy!')
print(result)'''