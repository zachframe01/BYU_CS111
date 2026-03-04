# For you to try
def reverse(s):
    """Returns a string with the letters of s
    in the inverse order.
    >>> reverse('ward')
    'draw'
    """
    if len(s)==1:       # base case
        return s
    return s[-1] + reverse(s[:-1])

print(reverse("palindrome"))

# fUnKyCaSe with helper function
def fUnKyCaSe(text):
    """Returns text in fUnKyCaSe
    >>> fUnKyCaSe("wats up")
    'wAtS Up'
    """
    
    def toggle_case(letter, should_up_case):
        return letter.upper() if should_up_case else letter.lower()

    def up_down(text, should_up_case):
        if len(text) == 1:
            return toggle_case(text, should_up_case)
        else:
            return toggle_case(text[0], should_up_case) + up_down(text[1:], not should_up_case)

    return up_down(text, False)

print(fUnKyCaSe("wats up"))
print(fUnKyCaSe("TRYING AGAIN"))

# fUnKyCaSe without helper function
def fUnKyCaSe(text):
    """Returns text in fUnKyCaSe
    >>> fUnKyCaSe("wats up")
    'wAtS Up'
    """
    
    def up_down(text,should_up_case):
        if text == '':
            return ''
        else:
            if should_up_case:
                return text[0].upper() + up_down(text[1:],False)
            else:
                return text[0].lower() + up_down(text[1:],True)
    
    return up_down(text, False) 


print(fUnKyCaSe("wats up"))
print(fUnKyCaSe("TRYING AGAIN"))


# my version of reverse_digits
from math import log10
def reverse_digits(n):
    """Returns n with the digits reversed.
    >>> reverse_digits(123)
    321
    """
    if n < 10:
        return n
    else:
        last = n % 10
        rest = n // 10
        return (10 ** (int(log10(n)))) * last + reverse_digits(rest)

print(reverse_digits(123)) 
print(reverse_digits(1234567)) 


# another version of reverse_digits
def reverse_digits(n):
    """Returns n with the digits reversed.
    >>> reverse_digits(123)
    321
    """
    def reverse(n, r):
      r *= 10
      if n < 10:
        return r + n
      else:
        return reverse(n // 10, r + n % 10)
    return reverse(n, 0)

print(reverse_digits(123)) 
print(reverse_digits(1234567)) 
