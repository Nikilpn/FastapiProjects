from fastapi import FastAPI,HTTPException
from app.schemas import PostCreate,PostCreateResponse

app=FastAPI()

@app.get("/hello-world")
def hello_world():
    return{"message":"hello world"}


###########################3
text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {"title": "Python Tip", "content": "Use list comprehensions for cleaner loops."},
    3: {"title": "Daily Motivation", "content": "Consistency beats intensity every tim"},
    4: {"title": "Fun Fact", "content": "The first computer bug was an actual moth fou"},
    5: {"title": "Update", "content": "Just launched my new project! Excited to share"},
    6: {"title": "Tech Insight", "content": "Async IO in Python can massively speed up"},
    7: {"title": "Quote", "content": "Programs must be written for people to read, an"},
    8: {"title": "Weekend Plans", "content": "Might finally clean up my GitHub repos.."},
    9: {"title": "Question", "content": "What's the most underrated Python library you"},
    10: {"title": "Mini Announcement", "content": "New video drops tomorrow—covering"},
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id:int)->PostCreateResponse:
    if id  not in text_posts:
        raise HTTPException(status_code=404,detail="post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post:PostCreate)->PostCreateResponse:
    new_post={"title":post.title,"content":post.content}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post
