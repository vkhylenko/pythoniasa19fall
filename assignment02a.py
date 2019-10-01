"""
Assignment 2-A
==============
Wrap Assignment 1-A in function `poem()` that satisfies the doctest:
>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""


def poem():
    last = ["That kept the cock that crow'd in the morn,",
            "That waked the priest all shaven and shorn,",
            "That married the man all tatter'd and torn,",
            "That kissed the maiden all forlorn,",
            "That milk'd the cow with the crumpled horn,",
            "That tossed the dog,",
            "That worried the cat,",
            "That killed the rat,",
            "That ate the malt",
            "That lay in the house that Jack built."]

    k = -1

    def list():
        global k
        b = last[len(last) - k - 1: len(last)]
        print('\n'.join(b))
        k += 1

    print("This is the house that Jack built.")
    list()
    print("This is the malt")
    list()
    print("\nThis is the rat,")
    list()
    print("\nThis is the cat,")
    list()
    print("\nThis is the dog,")
    list()
    print("\nThis is the cow with the crumpled horn,")
    list()
    print("\nThis is the maiden all forlorn")
    list()
    print("\nThis is the man all tatter'd and torn,")
    list()
    print("\nThis is the priest all shaven and shorn,")
    list()
    print("\nThis is the cock that crow'd in the morn, ")
    list()
    print("\nThis is the farmer sowing his corn, ")


if __name__ == '__main__':
    import doctest
    doctest.testmod()