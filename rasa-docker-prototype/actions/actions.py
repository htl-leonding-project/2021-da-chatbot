import webuntis
import os
import requests
import json

from typing import Any, Text, Dict, List
from dotenv import load_dotenv
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


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
                dispatcher.utter_message(text="In der Medientechnik lernt man, wie in der Informatik, viel über Programmieren aber auch medientechnische Inhalte, wie Foto- und Videografie, Bildbearbeitung, Audio, Webseitenerstellung oder Mobile Computing kommen hier nicht zu kurz und unterscheiden die Medientechnik von der Informatik.")
                dispatcher.utter_message(json_message={
                    "branch": "medientechnik"
                })
            elif branch == "informatik":
                dispatcher.utter_message(text=f"Natürlich erzähl ich dir etwas über {branch.capitalize()}")
                dispatcher.utter_message(text="Die Fachrichtung vereint eine EDV-technische und betriebswirtschaftliche Ausbildung. Diese Kombination bietet eine umfangreiche, praxisnahe Ausbildung, die später im Beruf direkt eingesetzt werden kann.")
                dispatcher.utter_message(json_message={
                    "branch": "informatik"
                })
            elif branch == "elektronik":
                dispatcher.utter_message(text=f"Natürlich erzähl ich dir etwas über {branch.capitalize()}")
                dispatcher.utter_message(text="Die vielseitige Ausbildung vereint Hardware und Software in nahezu unendlich vielen Anwendungen. Bis zur Matura sind Schüler und Schülerinnen in der Lage, umfangreichere elektronische Schaltungen und Systeme aufzubauen und zu programmieren.")
                dispatcher.utter_message(json_message={
                    "branch": "elektronik"
                })
            elif branch == "medizintechnik":
                dispatcher.utter_message(text=f"Natürlich erzähl ich dir etwas über {branch.capitalize()}")
                dispatcher.utter_message(text="In der Medizintechnik ist Elektronik eines der wichtigsten Elemente und wird daher in der Ausbildung entsprechend behandelt. Zugleich erfolgt eine Einführung in medizinische Themenbereiche wie Anatomie und Physiologie sowie Biosignalverarbeitung und Medizin- und Gesundheitsinformatik.")
                dispatcher.utter_message(json_message={
                    "branch": "medizintechnik"
                })
            elif branch == "fachschule":
                dispatcher.utter_message(text=f"Natürlich erzähl ich dir etwas über {branch.capitalize()}")
                dispatcher.utter_message(text="Im fachpraktischen Unterricht wird fachtheoretisches Wissen gefestigt und durch die Herstellung verschiedener Werkstücke mit dem Erlernen von praktischen Fertigkeiten ergänzt. Die 4-jährige Fachschulausbildung unterscheidet sich u.a. zur 5-jährigen HTL-Ausbildung auch durch den höheren Praxisanteil an Unterrichtsstunden.")
                dispatcher.utter_message(json_message={
                    "branch": "null"
                })
            elif branch == "abendschule":
                dispatcher.utter_message(text=f"Natürlich erzähl ich dir etwas über {branch.capitalize()}")
                dispatcher.utter_message(text="Seit dem Schuljahr 2015/16 gilt der neue Lehrplan für Informatik an unserer Abendschule. Dieser Lehrplan sieht die Konzentration der Ausbildung auf Bildungsinhalte der Informatik vor. Als schulautonomer Schwerpunkt wird in Leonding Software-Engineering angeboten.")
                dispatcher.utter_message(json_message={
                    "branch": "null"
                })
            else:
                dispatcher.utter_message(text=f"Die Fachrichtung {branch} kenne ich leider nicht.")
                dispatcher.utter_message(json_message={
                    "branch": "null"
                })

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

class ActionTellJoke(Action):
    def name(self) -> Text:
            return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        session = requests.session()
        s.keep_alive = False
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        response = session.get("https://v2.jokeapi.dev/joke/Any?lang=de&blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
        print(response)
        json_str = json.dumps(response.json())
        resp = json.loads(json_str)

        print(resp["type"])
        if resp["type"] == "single":
            output = resp["joke"]
            dispatcher.utter_message(text=output)
        else:
            output1 = resp["setup"]
            output2 = resp["delivery"]
            dispatcher.utter_message(text=output1)
            dispatcher.utter_message(text=output2)

        return []
