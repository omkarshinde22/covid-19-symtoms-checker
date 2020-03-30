# Corona Test built with the Rasa Stack

## 🏥 Introduction

This is an open source starter pack for developers to show how to automate full conversations in healthcare sector.

It supports the following user goals:

- Provide a test to patient to understand their health condition.
- Handling basic chitchat.

## 💾 How to install and setup Corona Test

**Step 1**: To install Corona Test, please clone the repo:
```
git clone https://github.com/omkarshinde22/omkarshinde22-hotmail.com.git
```
The Corona Test uses **Python 3.6 and 3.7** and has not been tested with other versions.
Use the requirements.txt file to install the appropriate dependencies
via pip. If you do not have pip installed yet first do:
```
sudo easy_install pip
```
otherwise move to the next step directly.

**Step 2**: Install requirements:
```
pip install -r requirements.txt
```

**Step 3**: Install the spaCy English language model by running:
```
python3 -m spacy download en
```

This will install the bot and all of its requirements.

## 🤖 How to run Corona Test

**Step 1**: Train the core model by running:
```
make train-core
```
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

**Step 2**: Train the NLU model by running:
```
make train-nlu
```
This will train the NLU model and store it inside the `/models/current/nlu` folder of your project directory.

**Step 3**: In a new terminal start the server for the custom action by running:
```
make action-server
```

**Step 4**: Now to test the Corona Test with both these models you can run:
```
make cmdline
```
After the bot has loaded you can start chatting to it. If you start by saying `Hi` for example,
the bot will reply by asking you what you are looking for and show you a number of options in form of buttons.
Since those buttons do not show when testing the bot in the command line, you can imitate a button click by copy
and pasting the intent of the button of your choice as your input.

An example conversation in the command line could look something like this:
```
Your input ->  Hi
Hi. What are you looking for ?
Buttons:
1: Sure (/inform{"corona": "sure"})
2: Not now (/inform{"corona": "not now"})

Your input ->  /inform{"corona": "sure"}

...
```

Try out different conversations and see what the current state of the bot can do!
After playing around a bit you can try to modify and extend the bot by adding custom actions and intents for example.
Find help for this in the [Rasa Docs](https://rasa.com/docs/).

A helpful option to extend training data and get to know your bot is interactive learning,
here you can correct your bot at every step in the conversation and automatically save the data for future training.

**Step 5**: To run Corona Test in interactive learning mode run:
```
make interactive
```

## 📱 Use Telegram as Chat platform
In order to chat to the Corona Test through Telegram you can do the following:

**Step 1**: First if you don't already use Telegram, download it and set it up with your phone.
Once you are registered with Telegram you start by setting up a Telegram bot.

**Step 2**: To setup your own bot go to the [Telegram BotFather](https://web.telegram.org/#/im?p=@BotFather),
enter `/newbot` and follow the instructions.
You should get your `access_token`, and the username you set will be your `verify`. Save this information as you will need it later.

**Step 3**: Now you will need to connect to Telegram via a webhook. To create a local webhook from your machine you can use [Ngrok](https://ngrok.com/). Follow the instructions on their site to
set it up on your computer. Move `ngrok` to your working directory and in a new terminal run:
```
./ngrok http 5005
```
Ngrok will create a https address for your computer. For Telegram you need the address in this format:
`https://xxxxxx.ngrok.io/webhooks/telegram/webhook`

**Step 4**: Go to the *credentials.yml* file that you downloaded from the repo and input your personal `access_token`, `verify` and `webhook_url`.
You will have to update the `webhook_url` everytime you do redo Step 3, the `access_token` and `verify` will stay the same.

**Step 5**: In a new terminal start the server for the custom action by running:
```
make action-server
```

**Step 6**: In a new terminal connect to Telegram by running:
```
make telegram
```

**Step 7**: Now you and anyone on Telegram are able to chat to your bot. You can find it by searching for its name on Telegram.

Detailed information about this can also be found in the [Rasa Docs](https://rasa.com/docs/core/connectors/#telegram-connector).


## Get API running by install Flask



## 👩‍💻 Overview of the files

`data/core/` - contains stories for Rasa Core

`data/nlu_data.md` - contains example NLU training data

`actions.py` - contains custom action/api code

`domain.yml` - the domain file for Core

`nlu_config.yml` - the NLU config file

`core_config.yml` - the Core config file

`credentials.yml` - contains credentials for the use with Telegram

`endpoints.yml` - contains url for endpoint

## 🛠 Makefile overview
Run `make help` to see an overview of all make commands available.

`train-nlu` - Train the NLU model.

`train-core` - Train the Core model.

`interactive` - Run the Corona Test interactive learning mode.

`cmdline` - Run the bot on the command line.

`action-server` - Start the action server.

`telegram` - Run the bot in the Telegram channel.


