from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

import openai
from dotenv import load_dotenv
import os
from IPython.display import display, HTML, JSON, Markdown

load_dotenv()
# env variables that are used by LangChain
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_TYPE'] = "azure"
os.environ['OPENAI_API_VERSION'] = os.getenv("OPENAI_DEPLOYMENT_VERSION")
os.environ['OPENAI_API_BASE'] = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")

OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
OPENAI_DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

# Configure OpenAI API
openai.api_type = "azure"
openai.api_version = os.getenv("OPENAI_DEPLOYMENT_VERSION")
openai.api_base = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_pet_name(animal_type, pet_color):
    llm = AzureChatOpenAI(deployment_name=OPENAI_DEPLOYMENT_NAME,
                          model=OPENAI_MODEL_NAME,
                          temperature=0.2,
                          max_tokens=400,
                          model_kwargs={"stop": ["<|im_end|>"]})
    
    promp_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it. It is {pet_color} in color. Suggest me 5 cool names"
    )
    name_chain = LLMChain(llm=llm, prompt=promp_template_name, output_key="pet_name")
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})
    return response

def langchain_agent():
    llm = AzureChatOpenAI(deployment_name=OPENAI_DEPLOYMENT_NAME,
                          model=OPENAI_MODEL_NAME,
                          temperature=0.2,
                          max_tokens=400,
                          )
    
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    result = agent.run(
        "What is the Average Age of a Dog? Multiply it by 3"
    )
    print(result)
if __name__ == "__main__":   
    langchain_agent()