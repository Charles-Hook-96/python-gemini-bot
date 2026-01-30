import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError('API key is required')

client = genai.Client(api_key=api_key)

def get_response(prompt):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text

if __name__ == '__main__':
    print(get_response('put prompt here'))

