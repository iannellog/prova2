from datetime import datetime

from activity import Activity
from timeslot import TimeSlot


class Agenda:
    """
    Represents an agenda with information about the planned
    activities and their timeslots
    Timeslots are assumed to be time intervals closed on the left (start time)
    and opened on the right (end time)
    """

    def __init__(self):
        """
        Initializes an empty agenda
        """
        pass

    def load(self, url: str):
        """
        Loads the agenda from the given url
        :param url: url where the agenda information is stored
        :return: None
        """
        pass

    def add_activity(self, activity: Activity) -> bool:
        """
        Adds an activity to the agenda if its time slot is free
        do nothing otherwise
        :param activity: activity to be inserted in the agenda
        :return: True if the insertion was successful, False otherwise
        """
        return False

    def next_activity(self, time: datetime) -> Activity | None:
        """
        Returns the first activity in the agenda that ends after the given time if any
        returns None if there is no activity in the agenda after the given time
        :return: an Activity object or None
        """
        return Activity('', datetime(1, 1, 1), datetime(1, 1, 1))

    def get_free_timeslot(self, timeslot: TimeSlot) -> TimeSlot | None:
        """
        Returns the first free timeslot in the agenda in the given timeslot
        returns None if there is no free timeslot in the agenda
        :param timeslot: timeslot in which search a free timeslot
        :return: a free timeslot or None
        """
        return TimeSlot(datetime(1, 1, 1), datetime(1, 1, 1))

    def free_timeslot(self, timeslot: TimeSlot) -> list:
        """
        Frees the given timeslot in the agenda and returns the list of the activities
        that have been deleted
        Also activities that partially overlap with the given timeslot must be deleted
        :param timeslot: timeslot to be freed
        :return: the list of the activities that have been deleted
        """
        return list()

    def get_activities(self, timeslot: TimeSlot) -> list:
        """
        Returns the list of activities that have been planned in the given timeslot
        Also activities that partially overlap with the given timeslot must be returned
        :param timeslot: timeslot in which search planned activities
        :return: the planned activities in the given timeslot
        """
        return list()

    def del_activity(self, activity: Activity) -> bool:
        """
        Deletes the given activity from the agenda
        Do nothing if activity is not in the agenda
        :param activity: activity to be deleted
        :return: if the activity was deleted
        """
        return False

    def save(self, url: str):
        """
        Saves the agenda in the given url
        :param url: where the agenda will be saved
        :return: None
        """
        pass


if __name__ == '__main__':
    agenda = Agenda()
    agenda.add_activity(
        Activity('xxx',
                 datetime(2020, 2, 1, 10, 0),
                 datetime(2020, 2, 1, 10, 20)))
    print(agenda.get_activities(TimeSlot(datetime(2020, 1, 1, 0, 0),
                                         datetime(2021, 1, 1, 0, 0))))
