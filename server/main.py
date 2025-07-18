from fastapi import FastAPI




app = FastAPI(title="RAG-Chatbot")




@app.get("/test")
async def test():
    return {"Message": "Test Successful"}