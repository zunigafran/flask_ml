"""Madlibs Stories."""


class Story:
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

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

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


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["place", "verb", "adjective"],
    """ When you're on a holiday, You can't find the words to say, 
        All the things that ocme to you, And I wanna feel it too.
    
        At {place} in the sun, We'll be {verb} and having fun,
        And it makes me feel so {adjective} I {verb}."""
)

story3 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """In the quirky town of {place}, a group of {adjective} friends embarked on a {adjective} adventure. Armed with {noun} and a sense of emotion,
    they encountered a {adjective}{noun} that challenged their {adjective} skills. With teamwork and a touch of {noun}, they triumphantly emerged,
    forever bonding over their {adjective} memories."""
)

story4 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """In the mystical {place}, a curious {noun} began to {verb} with an {adjective} twist. Its {plural_noun} suddenly gained the ability to {verb} 
    with extraordinary {adjective} powers. The townsfolk marveled at the {noun}'s newfound talents, transforming their ordinary {place} into a whimsical
     haven of {adjective} wonders."""
)