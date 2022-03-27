"""
CIS 211 Spring 2021 Week 1 Appointments Project

Author: Jacob Burke

Credits: Anna Scott: pointed out that Agenda is not iterable as an object.
Needed to be the items in the agenda

Created two classes, appt and agenda. Appt is then used to compare and find time
conflicts in the agenda class.
"""

from datetime import datetime


class Appt:
    """An appointment has a start time, an end time, and a title.
    The start and end time should be on the same day.
    Usage example:
        appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
        appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
        if appt2 > appt1:
            print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")
        elif appt1.overlaps(appt2):
            print("Oh no, a conflict in the schedule!")
            print(appt1.intersect(appt2))
    Should print:
        Oh no, a conflict in the schedule!
        2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """
    def __init__(self, start: datetime, finish: datetime, desc: str):
        """An appointment from start time to finish time, with description desc.
        Start and finish should be the same day.
        """
        assert finish > start, f"Period finish ({finish}) must be after start ({start})"
        self.start = start
        self.finish = finish
        self.desc = desc

    def __str__(self) -> str:
        """The textual format of an appointment is
        yyyy-mm-dd hh:mm hh:mm  | description
        Note that this is accurate only if start and finish
        are on the same day.
        """
        date_iso = self.start.date().isoformat()
        start_iso = self.start.time().isoformat(timespec='minutes')
        finish_iso = self.finish.time().isoformat(timespec='minutes')
        return f"{date_iso} {start_iso} {finish_iso} | {self.desc}"

    def __repr__(self) -> str:
        return f"Appt({repr(self.start)}, {repr(self.finish)}, {repr(self.desc)})"

    def __eq__(self, other: 'Appt') -> bool:
        """Equality means same time period, ignoring description"""
        return self.start == other.start and self.finish == other.finish

    def __lt__(self, other: 'Appt') -> bool:
        """Less than means the first time period is before the second
        given time period, ignoring description"""
        return self.finish <= other.start

    def __gt__(self, other: 'Appt') -> bool:
        """Greater than means the first time period is after the second
        given time period, ignoring description"""
        return self.start >= other.finish

    def start_time(appt: 'Appt') -> datetime:
        return appt.start

    def overlaps(self, other: 'Appt') -> bool:
        """Is there a non-zero overlap between these periods?"""
        if self < other or self > other:
            return False
        else:
            return True

    def intersect(self, other: 'Appt') -> 'Appt':
        """The overlapping portion of two Appt objects"""
        assert self.overlaps(other)  # Precondition
        if self.start < other.start:
            if self.finish < other.start:
                return Appt(other.start, other.finish, str(self.desc + " and " + other.desc))
            else:
                return Appt(other.start, self.finish, str(self.desc + " and " + other.desc))
        elif self.start > other.start:
            if other.finish > self.finish:
                return Appt(self.start, self.finish, str(self.desc + " and " + other.desc))
            else:
                return Appt(self.start, other.finish, str(self.desc + " and " + other.desc))


class Agenda:
    """An Agenda is a collection of appointments,
    similar to a list.

    Usage:
    appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
    appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda.text()}")
        print(f"Conflicts:\n {ag_conflicts}")

    Expected output:
    In agenda:
    2018-03-15 13:30 15:30 | Early afternoon nap
    2018-03-15 15:00 16:00 | Coffee break
    Conflicts:
    2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """
    def __init__(self):
        self.elements = [ ]

    def __str__(self):
        """Each Appt on its own line"""
        lines = [ str(e) for e in self.elements ]
        return "\n".join(lines)

    def __repr__(self) -> str:
        """The constructor does not actually work this way"""
        return f"Agenda({self.elements})"

    def __eq__(self, other: 'Agenda') -> bool:
        """Delegate to __eq__ (==) of wrapped lists"""
        return self.elements == other.elements

    def __len__(self) -> int:
        """Delegate to __len__ (len()) of wrapped lists"""
        return self.elements.__len__()

    def append(self, list: list):
        """Delegate to append()  of wrapped lists"""
        self.elements.append(list)

    def sort(self):
        """Sort agenda by appointment start times"""
        self.elements.sort(key=lambda appt: appt.start)

    def conflicts(self) -> 'Agenda':
        """Returns an agenda consisting of the conflicts
        (overlaps) between appointments in this agenda.
        Side effect: This agenda is sorted
        """
        self.sort()
        conflict_list = Agenda()
        counter = 0
        for appt in self.elements:
            counter += 1
            for later_appt in self.elements[counter:]:
                if appt.overlaps(later_appt) == True:
                    conflict_list.append(appt.intersect(later_appt))
                    counter +=1
                else:
                    break
        return conflict_list

if __name__ == "__main__":
    appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
    appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
    if appt2 > appt1:
        print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")
    elif appt1.overlaps(appt2):
        print("Oh no, a conflict in the schedule!")
        print(appt1.intersect(appt2))

'''
coffee_start = datetime(2019, 1, 1, 8)
coffee_end = datetime(2019, 1, 1, 10)
coffee = Appt(coffee_start, coffee_end, "Coffee with neighbors")
brunch_start = datetime(2019, 1, 1, 9)
brunch_end = datetime(2019, 1, 1, 13)
brunch = Appt(brunch_start, brunch_end, "Brunch with neighbors")
'''