import dspy
import os

# Use environment variable for API key instead of hardcoding
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required")

lm = dspy.LM('openai/gpt-4.1', api_key=api_key)
dspy.configure(lm=lm)

# Sample page text
page1 = """This is a found text, and thus far, the identity of The Author-the original author-has yet to be definitively located. In this way, the content of this novel resembles the Giallo films of Italian cinema where a killer's identity is withheld from the audience until the film's final act in order to intensify a great and ruinous mystery. Alternatively, this collection may also resemble an American detective novel such as Raymond Chandler's The Big Sleep, famous for its author's confessed bewilderment regarding the identity of the killer deeply entwined within Chandler's very own intricately constructed and labyrinthian plot."""

# Summarize
summarizer = dspy.ChainOfThought(dspy.Signature("page -> summary"))
summary1 = summarizer(page=page1).summary
print("Summary:", summary1)

# Reflect
reflector = dspy.ChainOfThought(dspy.Signature("page, summary -> reflection"))
reflection1 = reflector(page=page1, summary=summary1).reflection
print("Reflection:", reflection1)

# Dream prompts
dreamer = dspy.ChainOfThought(dspy.Signature("page, summary, reflection -> prompts"))
prompts1 = dreamer(page=page1, summary=summary1, reflection=reflection1).prompts
print("Dream Prompts:", prompts1) 