from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from model import llm_model

text = """
<|turn|>sytem
You are an expert assistant who provides concise and accurate answers.<turn|>
<|turn|>user
What is the capital of France?<turn|>
<|turn>model
"""

prompt = PromptTemplate.from_template(text)

def format_prompt(variables):
    return prompt.format(**variables)

joke_chain = (
    RunnableLambda(format_prompt) | llm_model() | StrOutputParser()
)

if __name__ == "__main__":
    variables = {
        "adjective": "silly",
        "content": "cats"
    }
    response = joke_chain.invoke(variables)
    print(response)