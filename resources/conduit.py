import sys

import openai

from resources import config

def get_completion(prompt):
    openai.api_key = config.get_api_key()
    engine = config.get_model()

    if prompt is None:
        print("Prompt is None")
    # print (f"Prompt: {prompt}")
    # print(f"Engine: {engine}")
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0.7,
        ).choices[0].text
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        sys.exit()
    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        sys,exit()
    except openai.error.RateLimitError as e:
        # Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        sys.exit()
    except openai.error.OpenAIError as e:
        print(f"OpenAI API returned an error: {e}")
        sys.exit()
    return response
