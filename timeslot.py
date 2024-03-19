from datetime import datetime, timedelta


class TimeSlot:
    """
    Represents a time slot
    """
    def __init__(self, start_time: datetime, end_time: datetime):
        """
        Initializes a new instance of the class TimeSlot with the
        start and end date/time
        """
        self.start_time = start_time
        self.end_time = end_time

    def start_time(self) -> datetime:
        """
        :return: the start time of the time slot
        """
        return datetime(1,1,1)

    def end_time(self) -> datetime:
        """
        :return: The end time of the time slot
        """
        return datetime(1,1,1)

    def duration(self) -> timedelta:
        """
        :return: the duration of the time slot
        """
        return timedelta()
