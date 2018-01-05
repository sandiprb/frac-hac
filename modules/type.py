from aenum import Enum


class SentimentType(Enum):
    NEGATIVE, NEUTRAL, POSITIVE = -1, 0, 1
