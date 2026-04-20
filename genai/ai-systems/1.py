client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response= client.chat.completions.create(
    model="gpt-4o-mini",
    # Add the message
    messages=message_listing,
    # Add your function definition
    tools=function_definition
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the function parameter type
function_definition[0]['function']['parameters']['type'] = 'object'

# Define the function properties
function_definition[0]['function']['parameters']['properties'] = {
    'title': {
        'type': 'string',
        'description': 'Title of the paper'
    },
    'year': {
        'type': 'string',
        'description': 'year of publication of the paper'
    }
}

response = get_response(messages, function_definition)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = get_response(messages, function_definition)

# Define the function to extract the data dictionary
def extract_dictionary(response):
  return response.choices[0].message.tool_calls[0].function.arguments

# Print the data dictionary
print(extract_dictionary(response))

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Append the second function
function_definition.append({'type': 'function', 'function':{'name': 'reply_to_review', 'description': 'Reply to to the user review is given', 'parameters': {'type': 'object', 'properties': {'reply': {'type': 'string', 'description': 'Reply to the user review'}}}}})

response = get_response(messages, function_definition)

# Print the response
print(response)
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response= client.chat.completions.create(
    model=model,
    messages=messages,
    # Add the function definition
    tools=function_definition,
    # Specify the function to be called for the response
    tool_choice={
        'type': 'function',
        'function': {
            'name': 'extract_review_info'
        }
    }
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Call the Chat Completions endpoint 
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      'role': 'system',
      'content': 'You will be provided with an input from the user that contains the airport code and you have to use the function appropriate for this and get the airport code and remember not to make any assumptions'
    },
    {"role": 'user', "content": "I'm planning to land a plane in JFK airport in New York and would like to have the corresponding information."}],
  tools=function_definition)

print_response(response)

# Check that the response has been produced using function calling
if response.choices[0].finish_reason=='tool_calls':
# Extract the function
    function_call = response.choices[0].message.tool_calls[0].function
    print(function_call)
else:
    print("I am sorry, but I could not understand your request.")



client = OpenAI(api_key="<OPENAI_API_TOKEN>")

message = "Can you show some example sentences in the past tense in French?"

# Use the moderation API
moderation_response = client.moderations.create(
    input=message
)

# Print the response
print(moderation_response.results[0].categories.violence)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

user_request = "Can you recommend a good restaurant in Berlin?"

# Write the system and user message
messages = [
    {
        'role': 'system',
        'content': 'you are a chatbot that provides advice for tourists visiting rome and must keep the topics in the response limited to questions covering only about food and drink, attractions, history and things to do around the city. In case the question is about any other topic then respond with Apologies, but I am not allowed to discuss this topic.'
    },
    {
        'role': 'user',
        'content': user_request
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages
)

# Print the response
print(response.choices[0].message.content)

