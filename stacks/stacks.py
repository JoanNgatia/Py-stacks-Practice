class Stack(object):
    """Base class for stack creation and operations."""

    def __init__(self):
        """Initialize stack as an empty python list."""
        self.original = []

    def push(self, element):
        """Handle addition of elements to a stack."""
        self.original.append(element)
        return self.original

    def pop(self):
        """Handle removal and return an element from the stack."""
        return self.original.pop()

    def is_empty(self):
        """Check if a stack has any elements."""
        return len(self.original) == 0

    def peek(self):
        """Return the last element in a stack."""
        return self.original[-1]


def check_brackets(s):
    """Function to check if all brackets have been sufficiently closed once opened.

    Takes in a string,s, and loops through it.
    """
    if '(' not in s or ')' not in s:
        return False

    new_stack = Stack()
    for val in s:
        if val == '(':
            new_stack.push(val)
        elif val == ')' and not new_stack.is_empty():
            new_stack.pop()
        elif val == ')' and new_stack.is_empty():
            return False

    return new_stack.is_empty()
