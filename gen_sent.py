import os
import openai

def gen_sent(words,language):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    sentences = []
    
    for w in words:
        p = f"Create a simple sentence in {language} that includes the word '{w}'. It is extremely important that the sentence include exactly one instance of the word '{w}' in the exact same form that it is written here."
        response = openai.Completion.create(
          prompt=p,
          model="text-davinci-003",
          temperature=0.9,
          max_tokens=60,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )

        sentences += [response['choices'][0]['text']]
    return sentences