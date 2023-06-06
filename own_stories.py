class Own_story:
    """
    newstory = Own_story()

    """
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """


    """Madlibs story.

    To  make a story, pass a code, a title, a list of prompts,
    and the text of the template.

        >>> s = Story(
        ...     "simple",
        ...     "A Simple Tale",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self,code,title,words,text,):
        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text
    

    # A science fiction story
story2 = Own_story(
    "science fiction",
    "The Last Spaceship",
    ["noun", "verb", "adjective"],
    """In a galaxy far, far away, the {adjective} {noun}
       {verb} through space, searching for a new home."""
)

# A mystery story
story3 = Own_story(
    "mystery",
    "The Missing Diamond",
    ["noun", "verb", "adjective"],
    """The {adjective} {noun} was missing, and everyone
       was a suspect. It was up to the detective to {verb}
       the culprit and solve the case."""
)

# A romance story
story4 = Own_story(
    "romance",
    "A Love Story",
    ["noun", "verb", "adjective", "plural_noun"],
    """She looked into his {adjective} {noun}, and knew
       that he was the one. They {verb} off into the
       sunset, hand in hand, dreaming of {plural_noun}."""
)

# To generate text from a story, pass in a dictionary-like thing
#of {prompt: answer, promp:answer):
stories = {}
storyList = [story2,story3,story4]
for story in storyList:
    stories[story.code] = stories.get((story.code), story)





# answer = story.code story for story in story




