import time
import httpx
import asyncio
from fastapi import FastAPI, APIRouter
from fastapi.responses import StreamingResponse

app = FastAPI(docs_url="/stream_api/docs", openapi_url="/stream_api/openapi.json", redoc_url=None)
router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello Gideon!"}

@router.get("/get-posts")
async def get_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        return response.json()

def story_streamer():
    full_story = [
        "Once upon a time in a world not unlike our own, there was a mysterious forest untouched by time. \
        The forest was said to be the home of an ancient spirit that guarded the secrets of the past. \
        Adventurers from all over the land would come seeking the spirit's wisdom, hoping to gain insight into history's greatest mysteries. \
        However, the forest was treacherous, and few who entered ever returned. \
        One day, a young scholar named Elara mustered the courage to venture into the woods. \
        She was determined to uncover the truth and believed that knowledge was worth any risk. \
        Elara encountered many challenges on her journey, from riddles that twisted the mind to pathways that seemed to loop back on themselves. \
        As night fell, she finally reached the heart of the forest, where the spirit awaited. \
        The spirit recognized her pure intent and shared tales of ancient civilizations and long-forgotten lore. \
        Elara listened with rapt attention, her thirst for knowledge finally being quenched. \
        With a promise to share the stories with the world, she made her way back to the edge of the forest, \
        carrying with her a newfound understanding of the universe and her place within it."
    ]
    for part in full_story:
        words = part.split()
        for word in words:
            yield word + ' '
            time.sleep(0.2)

@router.get("/get-stream")
async def get_stream():
    return StreamingResponse(story_streamer())        

app.include_router(router, prefix="/stream_api")
