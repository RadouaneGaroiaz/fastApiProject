from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello word"

@app.get("/items")
def get_items():
    return [

        {"id": 1, "desc": "item 1"},
        {"id": 2, "desc": "item 2"},
        {"id": 3, "desc": "item 3"},
        {"id": 4, "desc": "item 4"},

            ]
