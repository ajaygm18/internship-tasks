client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Add the final example
prompt = """Classify sentiment as 1-5 (negative to positive):
1. Comfortable, but not very pretty = 2
2. Love these! = 5
3. Unbelievably good! = 
4. Shoes fell apart on the second use. = 
5. The shoes look nice, but they aren't very comfortable. = 
6. Can't wait to show them off! = """

response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
print(response.choices[0].message.content)




client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  max_completion_tokens=150,
  messages=[
    {"role": 'system',
     "content": "You are a study planning assistant that creates plans for learning new skills."},
    {"role": "user",
     "content": "I want to learn to speak Dutch."}
  ]
)

# Extract the assistant's text response
print(response.choices[0].message.content)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

sys_msg = """You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": sys_msg},
    {"role": "user", "content": "Help me learn to rollerskating."}
  ]
)

print(response.choices[0].message.content)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {'role': 'user', 'content': 'Give me a quick summary of Portugal.'},
        {'role': 'assistant', 'content': 'Portugal is a country in Europe that borders Spain. The capital city is Lisboa'},
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
   model="gpt-4o-mini",
   # Add in the extra examples and responses
   messages=[
       {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
       {"role": "user", "content": "Give me a quick summary of Portugal."},
       {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
       {"role": "user", "content": example1},
       {"role": "assistant", "content": response1},
       {"role": "user", "content": example2},
       {"role": "assistant", "content": response2},
       {"role": "user", "content": example3},
       {"role": "assistant", "content": response3},
       {"role": "user", "content": "Give me a quick summary of Greece."}
   ]
)

print(response.choices[0].message.content)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = [
    {"role": "system", "content": "You are a helpful math tutor that speaks concisely."},
    {"role": "user", "content": "Explain what pi is."}
]

# Send the chat messages to the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_completion_tokens=100
)

# Extract the assistant message from the response
assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}

# Add assistant_dict to the messages dictionary
messages.append(assistant_dict)
print(messages)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = [{"role": "system", "content": "You are a helpful math tutor that speaks concisely."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

# Loop over the user questions
for q in user_msgs:
    print("User: ", q)
    
    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role": 'user', "content": q}
    messages.append(user_dict)
    
    # Create the API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=100
    )
    
    # Append the assistant's message to messages
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")



# Create the OpenAI client: you can leave "<OPENAI_API_TOKEN>" as is
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the conversation messages
conversation_messages = [
    {"role": 'system', "content": "You are a helpful event management assistant."},
    {"role": 'user', "content": "What are some good conversation starters at networking events?"},
    {"role": 'assistant', "content": ""}
]

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=conversation_messages
)
print(response.choices[0].message.content)


def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
response = get_response("Write a poem about ChatGPT")
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that follows the instructions
prompt = "Write a poem about chatgpt that uses basic english and a child can understand"

# Get the response
response = get_response(prompt)

print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that completes the story
prompt = f"This is a story delimited by triple backticks ```{story}``` complete this story by continuing it"

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)



client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that generates the table
prompt = 'create a table of 10 books of science fiction genre, it should include the columns Title, Author, Year'

# Get the response
response = get_response(prompt)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "Determine the language and generate a suitable title for the text that will be separated using triple backticks delimiters"

# Create the output format
output_format = """ The output you give should be in the format as follows
 Text: ...
 Language: ...
 Title: ...
 """

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = 'You will be given a text with triple backticks delimiter, your job is to determine its language and the number of sentences, if text contains more than one sentance generate a suitable title for it, otherwise write N/A as the title '

# Create the output format
output_format = """ The output response should be in the following format
Text: <text>
Language: <language>
Title: <title>
"""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = 'You will be given a text with triple backticks delimiter, your job is to determine its language and the number of sentences, if text contains more than one sentance generate a suitable title for it, otherwise write N/A as the title '

# Create the output format
output_format = """ The output response should be in the following format
Text: <text>
Language: <language>
Title: <title>
"""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)



client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a one-shot prompt
prompt = """
set {1, 3, 7, 12, 19} -> extract odd numbers -> {1, 3, 7, 19}
set {3, 5, 11, 12, 16} -> extract odd numbers -> 
"""

response = get_response(prompt)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  model = "gpt-4o-mini",
  # Provide the examples as previous conversations
  messages = [{"role": "user", "content": "The product quality exceeded my expectations"},
              {"role": "assistant", "content": "1"},
              {"role": "user", "content": "I had a terrible experience with this product's customer service"},
              {"role": "assistant", "content": "-1"},
              # Provide the text for the model to classify
              {"role": "user", "content": "The price of the product is really fair given its features"}
             ],
  temperature = 0
)
print(response.choices[0].message.content)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a single-step prompt to get help planning the vacation
prompt = "Plan a beach vacation"

response = get_response(prompt)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: 10, 4, 2 . Adding them: 10+4+2=16
             """

# Define the question
question = """Q: {15, 13, 82, 7, 14} 
              A:"""

# Create the final prompt
prompt = example + question
response = get_response(prompt)
print(response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the self_consistency instruction
self_consistency_instruction = 'you are provided with a prblem, solve the question by using 3 different individual experts and combine the results with majority vote to find the correct answer '

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = self_consistency_instruction + problem_to_solve

response = get_response(prompt)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = "Give me the top 10 pre-trained language models in a table format with the following columns model name, release year, owning company"

response = get_response(prompt)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
Time flies like an arrow -> no explicit emotion
They sat and ate their meal ->
"""

response = get_response(prompt)
print(response)







