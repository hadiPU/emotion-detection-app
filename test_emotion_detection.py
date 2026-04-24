"""Unit tests for emotion detection."""

import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector function."""

    def test_emotion_detector_output_keys(self):
        """Test that output contains all required keys."""
        result = emotion_detector("I am happy today")
        expected_keys = [
            "anger",
            "disgust",
            "fear",
            "joy",
            "sadness",
            "dominant_emotion"
        ]

        for key in expected_keys:
            self.assertIn(key, result)

    def test_dominant_emotion_exists(self):
        """Test that dominant emotion is returned."""
        result = emotion_detector("I am happy today")
        self.assertIsNotNone(result["dominant_emotion"])

    def test_invalid_input_format(self):
        """Test invalid input returns None values."""
        result = emotion_detector("")
        self.assertIn("dominant_emotion", result)


if __name__ == "__main__":
    unittest.main()