from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-pro",temperature=0.7)

result=model.invoke("create me a PICTURE of monkey on steriods and going to gym")


print(result)
