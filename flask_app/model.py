from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import JsonOutputParser

from pydantic import BaseModel, Field

from config import MODEL_ID, DEFAULT_PARAMS

def initialize_model(model_id=MODEL_ID, params=DEFAULT_PARAMS):
    llm = ChatOpenRouter(
        model=model_id,
        **params
    )
    return llm

llm = initialize_model()

gemma_template = PromptTemplate(
    template="""
<|turn|>sytem
{system_prompt}\n{format_prompt}<turn|>
<|turn|>user
{user_prompt}<turn|>
<|turn>model
""",
    input_variables=["system_prompt", "format_prompt", "user_prompt"]
)

class AIResponse(BaseModel):
    summary: str = Field(description="Summary of the user\'s prompt")
    sentiment: str = Field(description="Sentiment of the user\'s prompt")
    response: str = Field(description="Response to the user\'s prompt")

# JSON output parser
json_parser = JsonOutputParser(pydantic_object=AIResponse)

def get_ai_response(system_prompt, user_prompt, model=llm, template=gemma_template):
    chain = template | model | json_parser
    return chain.invoke({"system_prompt": system_prompt, "user_prompt": user_prompt, 'format_prompt':json_parser.get_format_instructions()})