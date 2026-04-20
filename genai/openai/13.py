client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the product description
prompt = f'''Summarize the provided below text of product description and do not use more than five bullet points and the text is separated by a delimiter of triple backtick 
```{product_description}```'''

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to expand the product's description
prompt = f"""Expand the product description text provided below and write a one paragraph comprehensive overview that includes the key information of the product like unique features, benefits, potential applications.
```{product_description}```
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that translates
prompt = f''' 
Translate the below text from English to French, Spanish and Japanese the text is separated by a triple backtick delimiter
```{marketing_message}```
'''
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to change the email's tone
prompt = f"""Transform the given email text by changing its tone to be professional, positive and user-centric. the text is separated by delimiter of triple backticks
```{sample_email}```
"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to transform the text
prompt = f""" In a multi-step process do the following to the provided triple backtick delimited text
Step1 Proofread the given sentance without changing the structure
Step2 change its tone to be formal and friendly
```{text}```
"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to classify the ticket
prompt = f"""
Classify the provided ticket text as a technical issue, billing inquiry or product feedback and dont provide anything else in the response only one word, the text is separated by a triple backtick delimiter ```{ticket}```
"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a few-shot prompt to get the ticket's entities
prompt = f""" 
Extract the entities from the given tickets as provided below

Ticket: {ticket_1}   ->   Entity: {entities_1}
Ticket: {ticket_2}   ->   Entity: {entities_2}
Ticket: {ticket_3}   ->   Entity: {entities_3}
Ticket: {ticket_4}   ->   Entity: <>
"""

response = get_response(prompt)

print("Ticket: \n", ticket_4)
print("Entities: \n", response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that asks the model for the function
prompt = """Write a python function that receives a list of 12 floats representing monthly sales data as input and returns the month with the highest sales value as output"""

response = get_response(prompt)
print(response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = f"""Write a python function that has the appropriate code to perform the operation in such a way that we get the output for the provided data as the shown example that is separated by a triple backtick delimiter
```{examples}```"""

response = get_response(prompt)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = ____

response = get_response(prompt)
print(response)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f"""Explain the code step by step of the provided function that is separated by the triple backtick delimiter 
```{function}```
"""
 
response = get_response(prompt)
print(response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": 'system', "content": system_prompt},
      		  {"role": 'user', "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content

# Try the function with a system and user prompts of your choice 
response = get_response("You are a financial advisor who provides real world financial assistance for investment purposes", "What is better ? invest in low PE ratio companies or the ones with current price below low instrinsic value")
print(response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the order number condition
order_number_condition = "Ask the user for an order number if it has not been specified already"

# Define the technical issue condition
technical_issue_condition = "start the sentance with ```I'm sorry to hear about your issue with ...``` incase it is a technical issue "

# Create the refined system prompt
refined_system_prompt = base_system_prompt + order_number_condition + technical_issue_condition

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft the system_prompt using the role-playing approach
system_prompt = "Activate a textbook recommendation chatbot roleplay, you are now a learning advisor who can interpret learner queries as described and provide relavent textbook recommendations for beginner to advanced textbooks based on their background."

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

base_system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

# Define behavior guidelines
behavior_guidelines = " Incase the user has not provided their background, experience and goals ask them to provide. "

# Define response guidelines
response_guidelines = " Do not recommend more than 3 textbooks "

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"
response = get_response(system_prompt, user_prompt)
print(response)



client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = f'Roleplay as a customer service chatbot for delivery service and the main purpose is to assist the users regarding their queries in a gentle tone. A service description has been provided that is separated by a triple backtick delimiter ```{service_description}```'

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)

print(response)



