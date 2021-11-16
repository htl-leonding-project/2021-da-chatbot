import webuntis
import os

from typing import Any, Text, Dict, List
from dotenv import load_dotenv
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


load_dotenv()

s = webuntis.Session(
            server='mese.webuntis.com/WebUntis/jsonrpc.do',
            username= os.getenv('WEBUNTIS_USERNAME'),
            password= os.getenv('WEBUNTIS_PASSWORD'),
            school='htbla linz leonding',
            useragent='WebUntis Test'
        )

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


        if branch:
            if branch == "medientechnik":
                dispatcher.utter_message(text=f"Natürlich erzähl ich dir etwas über {branch.capitalize()}")
                dispatcher.utter_message(text="Die Ausbildungsrichtung vermittelt alle informationstechnischen Kenntnisse, die für die multimediale Computerwelt benötigt werden, jedoch wird auch ein klarer Schwerpunkt auf den kreativen Bereich des Mediendesigns gelegt.")
            elif branch == "informatik":
                dispatcher.utter_message(text=f"Natürlich erzähl ich dir etwas über {branch.capitalize()}")
                dispatcher.utter_message(text="Die Fachrichtung vereint eine EDV-technische und betriebswirtschaftliche Ausbildung. Diese Kombination bietet eine umfangreiche, praxisnahe Ausbildung, die später im Beruf direkt eingesetzt werden kann.")
            elif branch == "elektronik":
                dispatcher.utter_message(text=f"Natürlich erzähl ich dir etwas über {branch.capitalize()}")
                dispatcher.utter_message(text="Die vielseitige Ausbildung vereint Hardware und Software in nahezu unendlich vielen Anwendungen. Bis zur Matura sind Schüler und Schülerinnen in der Lage, umfangreichere elektronische Schaltungen und Systeme aufzubauen und zu programmieren.")
            elif branch == "medizintechnik":
                dispatcher.utter_message(text=f"Natürlich erzähl ich dir etwas über {branch.capitalize()}")
                dispatcher.utter_message(text="In der Medizintechnik ist Elektronik eines der wichtigsten Elemente und wird daher in der Ausbildung entsprechend behandelt. Zugleich erfolgt eine Einführung in medizinische Themenbereiche wie Anatomie und Physiologie sowie Biosignalverarbeitung und Medizin- und Gesundheitsinformatik.")
            else:
                dispatcher.utter_message(text=f"Die Fachrichtung {branch} kenne ich leider nicht.")

        return []


class ActionNumberOfTeachers(Action):

    def name(self) -> Text:
        return "action_number_of_teachers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        counter = 0

        s.login()

        for teacher in s.teachers():
            counter+=1

        s.logout()

        dispatcher.utter_message(text=f"Derzeit gibt es {counter} Lehrerinnen und Lehrer an der HTL Leonding.")
        return []

class ActionNumberOfClasses(Action):

    def name(self) -> Text:
        return "action_number_of_classes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        counter = 0

        s.login()

        for klasse in s.klassen():
            counter+=1

        s.logout()

        dispatcher.utter_message(text=f"Derzeit gibt es {counter} Klassen an der HTL Leonding.")
        return []


class ActionNumberOfStudents(Action):

    def name(self) -> Text:
        return "action_number_students"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        counter = 0

        dispatcher.utter_message(text=f"Username: {os.getenv('WEBUNTIS_USERNAME'} Password: {os.getenv{'WEBUNTIS_PASSWORD'}")

        s.login()

        for student in s.students():
            counter+=1

        s.logout()

        dispatcher.utter_message(text=f"Derzeit gibt es {counter} Schülerinnen und Schüler an der HTL Leonding.")
        return []

class ActionHolidayList(Action):

    def name(self) -> Text:
        return "action_get_holidays"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output = "Dieses Schuljahr gibt es folgende schulautonome Tage:\n"

        s.login()

        for holiday in s.holidays():
            print(f"{holiday}\nStart: {holiday.start} Name: {holiday.name} End: {holiday.end} Short_name: {holiday.short_name}")
            output += f"- {holiday.name}: Von {holiday.start.strftime('%d. %m. %Y')} bis {holiday.end.strftime('%d. %m. %Y')}\n"

        s.logout()

        dispatcher.utter_message(text=output)
        return []
