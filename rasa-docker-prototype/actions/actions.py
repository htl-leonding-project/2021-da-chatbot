# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionHoursPerBranch(Action):

    def name(self) -> Text:
        return "action_hours_per_branch"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        branch = next(tracker.get_latest_entity_values("branch"), None)
        grade = next(tracker.get_latest_entity_values("grade"), None)
        subject = next(tracker.get_latest_entity_values("subject"), None)

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
        classroom = next(tracker.get_latest_entity_values("class"), None)

        dispatcher.utter_message(text=f"Du willst also wissen wo der Raum {classroom} ist?")

        return []


class ActionConsultationTeacher(Action):

    def name(self) -> Text:
        return "action_consultation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        teacher = next(tracker.get_latest_entity_values("teacher"), None)

        dispatcher.utter_message(text=f"Du willst also die Sprechstunden von Herrn {teacher} wissen?")

        return []


class ActionLogIn(Action):

    def name(self) -> Text:
        return "action_log_in"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = next(tracker.get_latest_entity_values("name"), None)

        return [SlotSet("logged_in", True)]


class ActionUtterBranch(Action):

    def name(self) -> Text:
        return "action_utter_branch"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        branch = next(tracker.get_latest_entity_values("branch"), None)
        branch = branch.lower()

        dispatcher.utter_message(text=f"{branch}")

        if branch:
            if branch == "medientechnik":
                dispatcher.utter_message(text="Die Ausbildungsrichtung vermittelt alle informationstechnischen Kenntnisse, die für die multimediale Computerwelt benötigt werden, jedoch wird auch ein klarer Schwerpunkt auf den kreativen Bereich des Mediendesigns gelegt.")
            elif branch == "informatik":
                dispatcher.utter_message(text="Die Fachrichtung vereint eine EDV-technische und betriebswirtschaftliche Ausbildung. Diese Kombination bietet eine umfangreiche, praxisnahe Ausbildung, die später im Beruf direkt eingesetzt werden kann.")
            elif branch == "elektronik":
                dispatcher.utter_message(text="Die vielseitige Ausbildung vereint Hardware und Software in nahezu unendlich vielen Anwendungen. Bis zur Matura sind Schüler und Schülerinnen in der Lage, umfangreichere elektronische Schaltungen und Systeme aufzubauen und zu programmieren.")
            elif branch == "medizintechnik":
                dispatcher.utter_message(text="In der Medizintechnik ist Elektronik eines der wichtigsten Elemente und wird daher in der Ausbildung entsprechend behandelt. Zugleich erfolgt eine Einführung in medizinische Themenbereiche wie Anatomie und Physiologie sowie Biosignalverarbeitung und Medizin- und Gesundheitsinformatik.")
            else:
                dispatcher.utter_message(text=f"Die Fachrichtung {branch} kenne ich leider nicht.")




        return []
