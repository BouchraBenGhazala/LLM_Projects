

import streamlit as st
from secret_key import openapi_key_sygma
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain


os.environ["OPENAI_API_KEY"]= openapi_key_sygma
llm=OpenAI(temperature=0.2)


def generate_restaurant_name_and_items(cuisine):
    prompt_template_name=PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine}. Suggest a fancy name for this"
    )
    name_chain=LLMChain(llm=llm,prompt=prompt_template_name,output_key="restaurant_name")

    prompt_template_items=PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest me ten menu items for {restaurant_name} without subitems of recipees for each menu, dont include the word item in the top"
    )

    food_items_chain=LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")

    chain= SequentialChain(
    chains=[name_chain,food_items_chain],
    input_variables=['cuisine'],
    output_variables=['restaurant_name','menu_items']
    )
    response=chain({'cuisine':cuisine})
    return response