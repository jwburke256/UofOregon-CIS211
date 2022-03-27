"""
CIS 211 Spring 2021 Week 5 Lab 5

Author: Jacob Burke

Credits: Krishna - For find_common_time identified that the set could
 not be indexed, so to return the int pop method should be used.

Created a set of classes that create clubs and accompanying times that do
not conflict based on student schedules. Demonstrates looping through
sets and being cognizant of aliasing.
"""

from typing import List, Set, Dict, Optional


class Student:

    def __init__(self, name: str,
                 interests: List[str]):
        self.name = name
        self.interests = interests
        self.freetimes = set([8, 9, 10, 11, 12, 13, 14, 15])
        self.meetings: List[int] = []

    def schedule_meeting(self, time: int):
        if time in self.freetimes:
            self.meetings.append(time)
            self.freetimes.remove(time)


class Club:

    def __init__(self, name: str):
        self.name = name
        self.members: List[Student] = []
        self.meeting_time: Optional[int] = None

    def join(self, student: Student):
        self.members.append(student)

    def find_common_time(self) -> int:
        times = set([8, 9, 10, 11, 12, 13, 14, 15])
        for student in self.members:
            times = times.intersection(student.freetimes)
        if len(times) == 0:
            return 0
        else:
            return times.pop()

    def schedule(self, time: int):
        for member in self.members:
            member.schedule_meeting(time)
        self.meeting_time = time

    def __str__(self) -> str:
        member_names = [member.name for member in self.members]
        return f"{self.name} ({', '.join(member_names)})"


class ASUO:

    def __init__(self):
        self.students: List[Student] = []
        self.clubs: List[Club] = []

    def enroll(self, s: Student):
        self.students.append(s)

    def form_clubs(self):
        clubs_to_form: Dict[str, Club] = {}
        for student in self.students:
            for interest in student.interests:
                if interest in clubs_to_form:
                    clubs_to_form[interest].join(student)
                else:
                    clubs_to_form[interest] = Club(interest)
                    clubs_to_form[interest].join(student)
        for key in clubs_to_form:
            self.clubs.append(clubs_to_form[key])

    def schedule_clubs(self):
        for club in self.clubs:
            club.schedule(club.find_common_time())

    def print_club_schedule(self):
        for club in self.clubs:
            if club.meeting_time is not None:
                print(f"{club} meets at {club.meeting_time}")

asuo = ASUO()
asuo.enroll(Student("Marty", ["badminton", "robotics"]))
asuo.enroll(Student("Kim", ["backgammon"]))
asuo.enroll(Student("Tara", ["robotics", "horticulture", "chess"]))
asuo.enroll(Student("George", ["chess", "badminton"]))

asuo.form_clubs()
asuo.schedule_clubs()
asuo.print_club_schedule()