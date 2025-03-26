import ollama

response = ollama.chat(
    model='llama3.1', # User can provide a different model ID that supports tool calling
    messages=[{'role': 'user', 'content': 
        '[insert a question or command that requires a tool call here, e.g., "What is the weather in San Francisco?"]'}],

		# provide a weather checking tool to the model
    tools=[{
      'type': 'function',
      'function': {
        'name': 'get_current_weather',
        'description': 'Get the current weather for a city',
        'parameters': {
          'type': 'object',
          'properties': {
            'city': {
              'type': 'string',
              'description': 'The name of the city',
            },
          },
          'required': ['city'],
        },
      },
    },
  ],
)

print(response['message']['tool_calls'])