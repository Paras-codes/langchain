from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Initialize the embeddings model (make sure your GOOGLE_API_KEY is set in your .env)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",dimensions=32)

# Example usage
text = "LangChain makes AI easy."
embedding = embeddings.embed_query(text)
print(embedding)