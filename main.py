from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Usher Njuguna",
        "title": "FastAPI is Awesome",
        "content": "I'm in love with this Framework",
        "date_posted": "February 5, 2025",
    },
    {
        "id": 2,
        "author": "Mitchelle Kwamboka",
        "title": "Usher's Python is massive",
        "content": "Python is fun",
        "date_posted": "February 6, 2025",
    },

]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts

