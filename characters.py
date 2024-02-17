import os
# from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

class MainCharacterChain:

    PROMPT = """
    Generate a detailed profile for a main character in a novel based on the following attributes.
    Include the character's name, background, personality, and any relevant details that will be important in the story.

    Attributes: {attributes}

    Profile:"""

    def __init__(self) -> None:

        self.llm = ChatOpenAI()
        self.chain = LLMChain.from_string(
            llm=self.llm,
            template=self.PROMPT
        )

        self.chain.verbose = True

    def run(self, attributes):
        # Instead of loading a resume, we now generate a character profile based on attributes.
        return self.chain.predict(attributes=attributes)
        folder = 'I am a cowboy and I like to ride on my horse'
        return folder

    def run(self, file_name):
        docs = self.load_resume(file_name)
        resume = '\n\n'.join([doc.page_content for doc in docs])
        return self.chain.run(resume)