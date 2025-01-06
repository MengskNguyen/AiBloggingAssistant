from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI
from dataclasses import dataclass

load_dotenv()


@dataclass
class BlogGeneratingStruct:
    title: str
    words_count: int
    keywords: str


def create_generate_blog_chain(data: BlogGeneratingStruct) -> str:
    model = ChatOpenAI(model="gpt-4o")
    translate_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a professional blogger, you will write about {title}"),
            ("human",
             "Write me a blog about {title}, no more than {words_count} words, make sure to incorporate following keywords in the blog: {keywords}")
        ]
    )

    generate_blog_chain = translate_prompt | model | StrOutputParser()

    response = generate_blog_chain.invoke(data)
    return response

