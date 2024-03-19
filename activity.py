from datetime import datetime, timedelta


class Activity:
    """
    Represents an activity
    """
    def __init__(self, description: str, start_time: datetime, end_time: datetime):
        self.__description = description


    def start_time(self) -> datetime:
        """
         :return: Date time when the activity starts
        """
        return datetime(1,1,1)


    def end_time(self) -> datetime:
        """
        :return: Date time when the activity ends
        """
        return datetime(1,1,1)


    def duration(self) -> timedelta:
        """
        :return: Duration of the activity in seconds
        """
        return timedelta()

    def description(self) -> str:
        """
        :return: Description of the activity
        """
        return ""


def activity_cmp(a: Activity, b: Activity) -> bool:
    """
    Compare two activity instances to determine if they are the same
    :param a: First activity instance
    :param b: Second activity instance
    :return: True if they are the same, False otherwise
    """
    return False