from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import Text, Dict, Any, List, Union
from rasa_sdk import Action
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
import random
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,)
import re
import pyjokes
from SendEmailAPI import *

class GetJoke(Action):
    def name(self):
        return "get_joke"

    def run(self, dispatcher, tracker, domain):
        result = pyjokes.get_joke()
        dispatcher.utter_message(result)

        return []

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
SubjectList = ["machine learning", "ml", "AI", "ai", "ML", "artificial intelligence", "deep learning", "Deep Learning", "Deep learning", "Machine learning", "Machine Learning", "Computer Vision", "computer vision", "Computer vision", "Neural Networks"]

class ActionSubmitSubscribeNewsletterForm(Action):
    def name(self) -> Text:
        return "action_submit_subscribe_newsletter_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        """Once we have an email, attempt to add it to the database"""

        print('Sending email...' + tracker.get_slot("email"))
        send_email(tracker.get_slot("email"))
        return []


class ValidateSubscribeNewsletterForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_subscribe_newsletter_form"

    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        email = tracker.get_slot("email")
        if re.search(regex, email):
            dispatcher.utter_message(text="Thank you for your email!")
            return {"email": email}  # slot_value
        else:
            dispatcher.utter_message(text="Your email is invalid! Please input a valid email.")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"email": None}


class ActionSubmitRegisterTrainingForm(Action):
    def name(self) -> Text:
        return "action_submit_register_training_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        """Once we have an email, attempt to add it to the database"""
        if int(tracker.get_slot("age")) > 17:
            print('Sending email...' + tracker.get_slot("email"))
            send_program_email(tracker.get_slot("email"), tracker.get_slot("name"), tracker.get_slot("age"), tracker.get_slot("phone"), tracker.get_slot("occupation"), tracker.get_slot("topic"))
            dispatcher.utter_message(text="A confirmation email has been sent! Please check your spam folder in case you cant find it.")
        else:
            dispatcher.utter_message(text="I have saved your email. Come back to us when you have turned 18.")
        return []


class ValidateRegisterTrainingForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_register_training_form"

    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        email = tracker.get_slot("email")
        if re.search(regex, email):
            dispatcher.utter_message(text="Thank you for your email!")
            return {"email": email}  # slot_value
        else:
            dispatcher.utter_message(text="Your email is invalid! Please input a valid email.")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"email": None}

    def validate_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        name = tracker.get_slot("name")
        if len(name) > 2:
            dispatcher.utter_message(text="Nice to meet you, {name}!".format(name=name))
            return {"name": name}  # slot_value
        else:
            dispatcher.utter_message(text="Your name is too short. I assume you misspelled.")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"name": None}

    def validate_age(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        raw_age = tracker.get_slot("age")
        ar_age = [int(character) for character in raw_age.split() if character.isdigit()]
        age = "";
        for num in ar_age:
            age = age + str(num);
        age = int(age)
        if int(age) > 18:
            return {"age": age}  # slot_value
        else:
            dispatcher.utter_message(text="You are too young for this course. Maybe try again later")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"age": age}

    def validate_occupation(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        occupation = tracker.get_slot("occupation")
        if occupation is not None:
            return {"occupation": occupation}  # slot_value
        else:
            dispatcher.utter_message(text="I'm sorry, I didn't quite get that. Maybe try putting in a monthly or yearly estimate instead.")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"occupation": None}

    def validate_phone(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        phone = tracker.get_slot("phone")
        if phone is not None:
            dispatcher.utter_message(text="Thank you for your phone number!")
            return {"phone": phone}  # slot_value
        else:
            dispatcher.utter_message(text="Please give me a valid phone number.")
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"phone": phone}

    def validate_topic(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        topic = str(tracker.get_slot("topic"))
        for subject in SubjectList:
            if str(topic) == subject:
                condition = 1
                break
            else:
                condition = 0
        if condition == 1:
            dispatcher.utter_message(text="Great choice! I will now subscribe you to the {program} program".format(program=topic))
            return {"topic": topic}  # slot_value
        else:
            dispatcher.utter_message(text="I'm sorry. This isn't a subject that we normally teach. Please choose from one of the following: Machine Learning, Deep Learning, and Computer Vision.")

            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"topic": None}

