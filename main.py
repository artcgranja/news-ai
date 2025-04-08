from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4o",
    input="What's the latest news about AI?",
    tools=[
        {
            "type": "web_search"
        }
    ]
)

print(json.dumps(response.output, default=lambda o: o.__dict__, indent=2))