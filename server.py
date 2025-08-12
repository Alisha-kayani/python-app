from app import app
from dotenv import load_dotenv
import os 

load_dotenv()

PORT = os.getenv("PORT")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app",host="0.0.0.0",port=int(PORT),reload=True)