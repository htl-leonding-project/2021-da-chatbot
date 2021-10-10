# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHoursPerBranch(Action):

    def name(self) -> Text:
        return "action_hours_per_branch"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        branch = tracker.get_slots('branch')
        grade = tracker.get_slots('grade')
        subject = tracker.get_slots('subject')

        dispatcher.utter_message(
            text=f"Du willst also die Stunden von {branch} wissen?") if not subject or not grade else dispatcher.utter_message(
            text=f"Du willst also die {subject} Stunden von der {grade}. Klasse {branch} wissen?")

        return []


class ActionRoomInfo(Action):

    def name(self) -> Text:
        return "action_room_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        classroom = tracker.get_slots('class')

        dispatcher.utter_message(text=f"Du willst also wissen wo der Raum {classroom} ist?")

        return []


class ActionConsultationTeacher(Action):

    def name(self) -> Text:
        return "action_consultation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        teacher = tracker.get_slots('teacher')

        dispatcher.utter_message(text=f"Du willst also die Sprechstunden von Herrn {teacher} wissen?")

        return []
