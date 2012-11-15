def rot13(s):
    
    """
    >>> type(rot13("bob"))
    <type 'str'>
    >>> len(rot13("foobar"))
    6
    >>> rot13("abc")
    'nop'
    >>> rot13("XYZ")
    'KLM'
    >>> rot13('5 The Parade')
    '5 Gur Cnenqr'
    >>> rot13('5 Gur Cnenqr')
    '5 The Parade'
    """
    
    # Create an empty string named result to store the encrypted text
    # Let char loop over each character in the input string
        # If this char is a letter:
            # Set char_low to be char converted to lower case
            # Note: the next 5 lines do not need to be changed - 
            #  they will modify the character as necessary
            if char_low <= 'm':
                dist = 13
            else:
                dist = -13
            char = chr(ord(char) + dist)
        # Push char onto the end of the result
    # Return the encrypted text