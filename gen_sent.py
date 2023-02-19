import re
import os
import openai

def gen_sent(words,language):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    max_tries = 3
    sentences = []
    ind = 1
    
    for w in words:
        solved = False
        num_tries = 0
        p = f"Create a simple sentence in {language} that includes the word '{w}'. It is extremely important that the sentence include exactly one instance of the word '{w}' in the exact same form that it is written here."
        while (not solved) and (num_tries < max_tries):
            response = openai.Completion.create(
              prompt=p,
              model="text-davinci-003",
              temperature=0.9,
              max_tokens=60,
              top_p=1.0,
              frequency_penalty=0.0,
              presence_penalty=0.0
            )
            if re.search(r"\b"+w,response['choices'][0]['text']):
                solved = True
            else:
                num_tries += 1
        
        if solved:
            sentences += [(re.sub(r"(.*)\b"+w+"(.*)",r"\1_______\2",response['choices'][0]['text']),ind,w,response['choices'][0]['text'])]
            ind += 1
    return sentences