"""Application definition."""
from bocadillo import App, discover_providers, Templates, static

app = App()
discover_providers("chatbot.providerconf")
templates = Templates(app, directory='dist')

# Create routes here.
@app.route('/')
async def index(req, res):
    res.html = await templates.render("index.html")

@app.websocket_route("/conversation")
async def converse(ws, diego, save_client):
    async for message in ws:
        response = diego.get_response(message)
        await ws.send(str(response))


@app.route("/client-count")
async def client_count(req, res, clients):
    res.json = {"count": len(clients)}