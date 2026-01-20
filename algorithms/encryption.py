
def greatest_common_divisor(a: int, b: int) -> int:
    """Finds the greatest common divisor of two integers
 
    Args:
        a(int)
        b(int)
 
    Returns:
        a(int): the greatest common divisor after a modulo calcuation
 
    Raises:
        N/A
 
    Examples:
        >>> greatest_common_divisor(2 3480)
        2
    """
    while b != 0:
        a, b = b, a % b
    return a

def modular_inverse(e: int, phi: int) -> int:
    """Finds the modular inverse of e and phi
 
    Args:
        e(int)
        phi(int)
 
    Returns:
        d(int): the modular inverse of e and phi
 
    Raises:
        N/A
 
    Examples:
        >>> modular_inverse(7, 3480)
        2983
    """

    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1


def power(base: int, expoent: int, m: int) -> int:
    """Performs modulo arithmetic on the message with the exponents (keys).
 
    Args:
        base(int): the given character in ASCII format
        exponent(int): public/private key
        m(int): public key
 
    Returns:
        output(int): encrypted/decrypted character
 
    Raises:
        N/A
 
    Examples:
        >>> power(72, 7, 3599)
        660
    """

    output = 1
    base = base % m

    while expoent > 0:
        if expoent & 1:
            output = (output * base) % m
        base = (base * base) % m
        expoent = expoent // 2

    return output

def generate_keys() -> list[int, int, int]:
    """Returns generated public and private keys.
 
    Args:
        N/A
 
    Returns:
        e(int): public key
        d(int): public key
        n(int): private key
 
    Raises:
        N/A
 
    Examples:
        >>> generate_keys()
        [7, 2983, 3599]
    """

    p = 59
    q = 61

    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 0
    for e in range(2, phi):
        if greatest_common_divisor(e, phi) == 1:
            break
    
    d = modular_inverse(e, phi)

    return [e, d, n]

def rsa_entry(encrypting: bool, message: str, keys: list[int, int, int] | bool = False) -> str:
    """Returns an encrypted message after conducting the neccesary RSA functions.
 
    Args:
        encrypting(bool): determines whether the function encrypts or decrypts
        message(str): the message that the RSA algorithm will encrypting, or decrypting
        keys(list[int, int, int]): the public and private keys
 
    Returns:
        encrypted_chars(string): when encrypting = True
        decrypted_chars(string): when encrypting = False
 
    Raises:
        N/A
 
    Examples:
        >>> rsa_entry(True, message="Hello", keys=[7, 2983, 3599])
        660 1607 1267 1267 2634
    """

    if keys == False:
        keys = generate_keys()
    
    e, d, n = keys[0], keys[1], keys[2]

    if encrypting:
        encrypted_chars = [str(power(ord(char), e, n)) for char in message]
        return " ".join(encrypted_chars)

    else:
        decrypted_chars = [chr(power(int(num), d, n)) for num in message.split()]
        return "".join(decrypted_chars)


#GeeksforGeeks (2017). RSA Algorithm in Cryptography. [online] GeeksforGeeks. 
#Available at: https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/.

print(rsa_entry(True, message="Hello"))