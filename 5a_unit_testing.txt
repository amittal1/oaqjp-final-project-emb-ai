import pytest
from EmotionDetection import emotion_detector
import json

tests  = [
("I am glad this happened", "joy"),
("I am really mad about this", "anger"),
("I feel disgusted just hearing about this", "disgust"),
("I am so sad about this", "sadness"),
("I am really afraid that this will happen", "fear"),
]

@pytest.mark.parametrize("input, expected", tests)
def test_emotion(input, expected):
    """
    Test the add function with various inputs and expected outputs.
    """
    res = emotion_detector(input)
    r = json.loads(res)
    print(expected)
    assert r.get('dominant_emotion') == expected
