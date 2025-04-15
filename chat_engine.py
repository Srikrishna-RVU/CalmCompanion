import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from prompts import mental_health_prompt
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

conversation = None

def init_conversation():
    global conversation
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3,
        convert_system_message_to_human=True
    )

    memory = ConversationBufferMemory(memory_key="history")
    prompt = PromptTemplate.from_template(mental_health_prompt)

    conversation = ConversationChain(llm=model, memory=memory, prompt=prompt)

def get_response(user_input: str) -> str:
    return conversation.predict(input=user_input)
