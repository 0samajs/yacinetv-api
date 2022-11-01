#  ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄   ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ 
# █  █ █  █      █       █   █  █  █ █       █       █  █ █  █  █       █       █   █
# █  █▄█  █  ▄   █       █   █   █▄█ █    ▄▄▄█▄     ▄█  █▄█  █  █   ▄   █    ▄  █   █
# █       █ █▄█  █     ▄▄█   █       █   █▄▄▄  █   █ █       █  █  █▄█  █   █▄█ █   █
# █▄     ▄█      █    █  █   █  ▄    █    ▄▄▄█ █   █ █       █  █       █    ▄▄▄█   █
#   █   █ █  ▄   █    █▄▄█   █ █ █   █   █▄▄▄  █   █  █     █   █   ▄   █   █   █   █
#   █▄▄▄█ █▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█   █▄▄▄█    █▄▄█ █▄▄█▄▄▄█   █▄▄▄█

# by aimadnet
# contact: t.me/aimadnet

from fastapi import FastAPI
from authx import ProfilerMiddleware
from fastapi.middleware.cors import CORSMiddleware

import routes

app = FastAPI(
    title="YacineTV",
    description="This is an unofficial api wrapper for yacineapp.tv in python",
    version="1.0.0",
)

app.include_router(routes.router)
app.add_middleware(ProfilerMiddleware)

yourPort = 2121
origins = [
    "http://localhost",
    f"http://localhost:{yourPort}",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return {"message": "Hello World"}
