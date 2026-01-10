from dotenv import load_dotenv
load_dotenv('.env')
import requests
from google.genai import Client
from google.genai import types

client = Client()


# mul_fn_dec = {
#     "name": "mul",
#     "description": "Multiplies two numbers and returns output.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "a": {
#                 "type": "number",
#                 "description": "First number",
#             },
#             "b": {
#                 "type": "number",
#                 "description": "The second number",
#             },
#         },
#         "required": ["a", "b"],
#     },
# }

def mul(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns output.
    """
    return a * b


def get_user_information(user_id: int) -> dict:
    """
    Return user information based on user id.
    """
    res = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return res.json()


def db_tool(query: str):
    
    pass


# tools = types.Tool(function_declarations=[mul])
config = types.GenerateContentConfig(
    tools=[mul, get_user_information],
    system_instruction="Always answer with human readable format after tool calling."
)


user_input = "Give me information about user with id 4."


response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=f"""{user_input}""",
    config=config
)

response

print(response.text)


print(f"{13655216 * 1234531:,}")

if response.candidates[0].content.parts[0].function_call is not None:
    fn = response.candidates[0].content.parts[0].function_call
    print(fn.name)
    print(fn.args)
    if fn.name == 'mul':
        out = mul(**fn.args)

else:
    print(response.candidates[0].content.parts[0].text)

print(response.text)


print(f"{13655216 * 1234531:,}")
