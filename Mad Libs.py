
#Function for mad libs.
def mad_libs():

    # input words from the user
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    # Story of Mad Libs
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."

    # Print the story
    print("\nYour Mad Libs story:")
    print(story)

#Call the mad libs function
mad_libs()
