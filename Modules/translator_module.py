from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI
from dataclasses import dataclass


@dataclass
class TranslatorStruct:
    content: str
    language: str


def translator_module(data: TranslatorStruct) -> str:
    model = ChatOpenAI(model="gpt-4o")
    translator_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a professional translator"),
            ("human", "translator the following content to {language}: \n{content}")
        ]
    )

    translator_chain = translator_prompt | model | StrOutputParser()
    response = translator_chain.invoke(data)
    return response


