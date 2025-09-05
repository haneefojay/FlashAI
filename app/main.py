from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Flashcard Generator")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Flashcard backend running!"}

@app.post("/flashcards/generate")
def generate_flashcards(request: dict):
    # Your AI flashcard generation logic here
    return [{"question": "Sample?", "answer": "Sample answer"}]