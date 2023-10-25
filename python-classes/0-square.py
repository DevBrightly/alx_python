class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        get_size(): Get the size of the square.
        set_size(size): Set the size of the square.
        area(): Calculate and return the area of the square.
    """

    def __init__(self, size):
        """
        Initialize a Square object with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def get_size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    def set_size(self, size):
        """
        Set the size of the square.

        Args:
            size (int): The new size for the square.
        """
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
