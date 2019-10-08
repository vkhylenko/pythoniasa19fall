"""
Assignment 2-A
==============
Wrap Assignment 1-A in function `poem()` that satisfies the doctest:
>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():
    last = ["That kept the cock that crowed in the morn,",
            "That waked the priest all shaven and shorn,",
            "That married the man all tattered and torn,",
            "That kissed the maiden all forlorn,",
            "That milked the cow with the crumpled horn,",
            "That tossed the dog,",
            "That worried the cat,",
            "That killed the rat,",
            "That ate the malt",
            "That lay in the house that Jack built."]

    k = -1

    def verse(k, result):
        b = last[len(last) - k - 1: len(last)]
        result += "\n".join(b)
        return k + 1, result + "\n"

    def print_poem(k):
        result = ""
        result += "This is the house that Jack built.\n"
        k,result = verse(k, result)
        result += "This is the malt\n"
        k,result = verse(k, result)
        result += "\nThis is the rat,\n"
        k,result = verse(k, result)
        result += "\nThis is the cat,\n"
        k,result = verse(k, result)
        result += "\nThis is the dog,\n"
        k,result = verse(k, result)
        result += "\nThis is the cow with the crumpled horn,\n"
        k,result = verse(k, result)
        result += "\nThis is the maiden all forlorn,\n"
        k,result = verse(k, result)
        result += "\nThis is the man all tattered and torn,\n"
        k,result = verse(k, result)
        result += "\nThis is the priest all shaven and shorn,\n"
        k,result = verse(k, result)
        result += "\nThis is the cock that crowed in the morn,\n"
        k,result = verse(k, result)
        result += "\nThis is the farmer sowing his corn,\n"
        k,result = verse(k, result)

        return result

    return print_poem(k)


poem()
if __name__ == '__main__':
    import doctest
    doctest.testmod()