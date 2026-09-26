def is_palindrome(s):

    """Check whether a string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if s reads the same forwards and backwards.

    Example:
        >>> is_palindrome("madam")
        True
    """
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text):
    """Count the number of words in a text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: Number of words separated by whitespace.

    Example:
        >>> count_words("Hello brave new world")
        4
    """

    """Check whether a string is a palindrome."""
    s = s.lower()
    return s == s[::-1]


def count_words(text):
    """Count the number of words in a text."""
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert temperature from Celsius to Fahrenheit.

    Args:
        c (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.

    Example:
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return c * 9 / 5 + 32


if __name__ == "__main__":
    # Testing is_palindrome
    print("is_palindrome('madam'):", is_palindrome("madam"))
    print("is_palindrome('hello'):", is_palindrome("hello"))

    # Testing count_words
    print("count_words('Hello brave new world'):", count_words("Hello brave new world"))

    # Testing celsius_to_fahrenheit
    print("celsius_to_fahrenheit(100):", celsius_to_fahrenheit(100))


# Testing the functions
print(is_palindrome("madam"))
print(count_words("Python is easy to learn"))
print(celsius_to_fahrenheit(25))
