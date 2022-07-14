# The Rasa Demo Bot

## Introduction
The purpose of this repo is to showcase a contextual AI assistant built with the open source Rasa framework.

- Understanding the Rasa framework
- Getting started with Rasa
- Subscribing to the Rasa newsletter
- Handling basic chitchat

## ‍ Installation
To install Sara, please clone the repo and run:

```sh
pip install -r requirements.txt
cd Chatbot
```

This will install the bot and all of its requirements.
Note that this bot should be used with python 3.6 or 3.7.


## To run:

Use `rasa train` to train a model (this will take a significant amount of memory to train,
which is why it was done on Google Cloud Platform.

Then, to run, first set up your action server in one terminal window:
```bash
rasa run actions
```

There are some custom actions that require connections to external services,
specifically `SubscribeNewsletterForm` and `SalesForm`. For these
to run you would need to have your own MailChimp newsletter and a Google sheet
to connect to.

In another window, run the bot:
```bash
rasa shell
```

## ‍Overview of the files

`data/stories` - contains stories

`data/nlu` - contains NLU training data

`actions` - contains custom action code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble


## License
Licensed under the GNU General Public License v3. Copyright 2018 Rasa Technologies
GmbH. [Copy of the license](https://github.com/RasaHQ/rasa-demo/blob/main/LICENSE).
Licensees may convey the work under this license. There is no warranty for the work.