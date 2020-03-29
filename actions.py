# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, FollowupAction
from rasa_core_sdk.forms import FormAction


ENDPOINTS = {
    "base": "http://127.0.0.1:1234/checkup"
}

FACILITY_TYPES = {
    "Sure":
        {
            "name": "sure",
            "resource": "sure"
        },
    "Not now":
        {
            "name": "Not now",
            "resource": "Not now"
        }
}
count = 0


def _create_path(base) -> Text:
    """Creates a path to find provider using the endpoints."""

    return base


def _find_facilities(results: Text) -> List[Dict]:
    """Returns json of facilities matching the search criteria."""

    full_path = _create_path(ENDPOINTS["base"])

    results = requests.get(full_path).json()
    print("Path:", results)
    return results


def _resolve_name(facility_types, resource) -> Text:
    for key, value in facility_types.items():
        if value.get("resource") == resource:
            return value.get("name")
    return ""


class FindFacilityTypes(Action):
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "ask_corona"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        full_path = _create_path(ENDPOINTS["base"])

        results = requests.get(full_path).json()
        print("Path:", results[0])

        buttons = []
        for t in FACILITY_TYPES:
            facility_type = FACILITY_TYPES[t]
            payload = "/inform{\"corona\": \"" + facility_type.get(
                "resource") + "\"}"

            buttons.append(
                {"title": "{}".format(facility_type.get("name").title()),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_greet", buttons, tracker)
        return []



class Enquiry(Action):

    def name(self):

        return "enquiry"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        global count

        print("count:", count)

        full_path = _create_path(ENDPOINTS["base"])
        results = requests.get(full_path).json()

        if count == 13:

            dispatcher.utter_template('utter_continue', tracker)
            return []
        else:
            selected = results[count]
            count = count + 1

            print("count1:", count)
            print("result:", selected)
            print("que:", selected["question"])
            question = selected["question"]
            option1 = selected["option1"]
            option2 = selected["option2"]
            option3 = selected["option3"]

            buttons = []
            payload1 = "/inform{\"enquiry\": \"" + option1 + "\"}"
            payload2 = "/inform{\"enquiry\": \"" + option2 + "\"}"
            payload3 = "/inform{\"enquiry\": \"" + option3 + "\"}"

            buttons.append({"title": "{}".format(option1.title()), "payload": payload1})
            buttons.append({"title": "{}".format(option2.title()), "payload": payload2})
            buttons.append({"title": "{}".format(option3.title()), "payload": payload3})

        # TODO: update rasa core version for configurable `button_type`;;;;
        dispatcher.utter_button_message(question, buttons)
        # dispatcher.utter_button_template(question, buttons, tracker)
        return []


class Counter(Action):

    def name(self):
        return "counter"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["enquiry"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"enquiry": self.from_entity(entity="enquiry",
                                            intent=["inform"])}

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        full_path = _create_path(ENDPOINTS["base"])
        results = requests.get(full_path).json()
        selected = results[0]
        print("result:", selected)
        print("que:", selected["question"])
        question = selected["question"]
        option1 = selected["option1"]
        option2 = selected["option2"]
        option3 = selected["option3"]

        results_enq = tracker.get_slot('enquiry')

        print("***result:", results_enq)

        print("Hello Omkar. Counter class")

        return []




class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "action_chitchat"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        intent = tracker.latest_message['intent'].get('name')

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in ['ask_builder', 'ask_weather', 'ask_howdoing',
                      'ask_howold', 'ask_languagesbot', 'ask_restaurant',
                      'ask_time', 'ask_wherefrom', 'ask_whoami',
                      'handleinsult', 'telljoke', 'ask_whatismyname']:
            dispatcher.utter_template('utter_' + intent, tracker)

        return []
