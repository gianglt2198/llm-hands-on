from model import get_ai_response

def call_model(system_prompt, user_prompt):
    response = get_ai_response(system_prompt, user_prompt)
    
    print("Response: \n", response)

call_model("You are a helpful assistant who provides concise and accurate answers", "What is the capital of Canada? Tell me a cool fact about it as well")