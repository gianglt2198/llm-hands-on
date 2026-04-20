from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from model import llm_model

template = """Tell me a {adjective} joke about {content}."""
prompt = PromptTemplate.from_template(template)

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