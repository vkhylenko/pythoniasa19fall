"""
Assignment 1-A
==============

Update the Python script below to make it more compact and readable; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

"""
last = ["That kept the cock that crow'd in the morn,",
        "That waked the priests all shaven and shorn,",
        "That married the man all tatter'd and torn,",
        "That kissed the maiden all forlorn,",
        "That milk'd the cow with the crumpled horn,",
        "That tossed the dog,",
        "That worried the cat,",
        "That killed the rat,",
        "That ate the malt",
        "That lay in the house that Jack built."]


k = -1

def list(k):
       b = last[len(last)-k-1: len(last)]
       print('\n'.join(b))
       return k +1



print("This is the house that Jack built.")
k = list(k)
print("This is the malt")
k = list(k)
print("\nThis is the rat,")
k = list(k)
print("\nThis is the cat,")
k = list(k)
print("\nThis is the dog,")
k = list(k)
print("\nThis is the cow with the crumpled horn,")
k = list(k)
print("\nThis is the maiden all forlorn")
k = list(k)
print("\nThis is the man all tatter'd and torn,")
k = list(k)
print("\nThis is the priest all shaven and shorn,")
k = list(k)
print("\nThis is the cock that crow'd in the morn, ")
k = list(k)
print("\nThis is the farmer sowing his corn, ")
k = list(k)

poem = '''
This is the house that Jack built.

This is the malt 
That lay in the house that Jack built.

This is the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cow with the crumpled horn, 
That toss'd the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milked the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cock that crow'd in the morn, 
That waked the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the farmer sowing his corn, 
That kept the cock that crow'd in the morn, 
That waked the priest all shaven and shorn,
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That killed the rat, 
That ate the malt 
That lay in the house that Jack built.
'''

#print(poem)
