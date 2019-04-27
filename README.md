# chatbot

This project was generated using [Bocadillo CLI][repo] version 0.2.1.

[repo]: https://github.com/bocadilloproject/bocadillo-cli

## Install

Create a python 3.6 or 3.7 virtualenv and activate it
```bash
python3 -m venv venv
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Start the uvicorn server:

```bash
uvicorn chatbot.asgi:app
```

To enable hot reload, use the `--reload` option. The server will run at `http://localhost:8000`.

### Start the cli client:

```bash
python client.py
```

### Sample chat

```
> Hi
Hello
> How are you?
I am doing well.
> Thats good to know
Are you a robot?
> I'm a human, I think.
No it is not. The cake is delicious.
> Cake, what cake?
I'm doing well. How are you?
> I'm fine
Hi, How is it going?
> well
What are you?
> not a robot
Yes I am.
> are you?
Good.
> 

```

### Front End

Place you built project in the `./dist` folder