from vertexai.generative_models import GenerativeModel, Tool, FunctionDeclaration

model = GenerativeModel("gemini-1.5-flask-001")

display_cities_function = FunctionDeclaration.from_func(display_cities)
tool = Tool(function_declarations=[display_cities_function])

message = "I'd like to take a ski trip vith my family but I'm not sure where to go."

res - model.generate_content(message, tool=[tool])

print(f"Function Name: {res.candidates[0].content.parts[0].function_call.name}")
print(f"Function Args: {res.candidates[0].content.parts[0].function_call.args}")

# Function Name: display_cities
# Function Args: {'preferences': 'skiing', 'cities': ['Aspen', 'Vail', 'Park City']}