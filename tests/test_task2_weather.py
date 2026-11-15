"""Автоматическая проверка логики задания 2 без реального API-ключа."""

import contextlib
import io
import os
import sys
import unittest
from unittest.mock import patch, Mock

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import task2_weather


class TestWeatherProgram(unittest.TestCase):
    @patch.dict(os.environ, {"OPENWEATHER_API_KEY": "test-api-key"})
    @patch("builtins.input", return_value="Moscow")
    @patch("task2_weather.requests.get")
    def test_city_temperature_and_description_are_printed(
        self, mock_get, mock_input
    ):
        fake_response = Mock()
        fake_response.status_code = 200
        fake_response.json.return_value = {
            "name": "Moscow",
            "main": {"temp": 12.5},
            "weather": [{"description": "небольшая облачность"}],
        }
        mock_get.return_value = fake_response

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            task2_weather.main()

        self.assertIn("Moscow", output.getvalue())
        self.assertIn("12.5", output.getvalue())
        self.assertIn("Небольшая облачность", output.getvalue())
        mock_get.assert_called_once()
        self.assertEqual(
            mock_get.call_args.kwargs["params"],
            {
                "q": "Moscow",
                "appid": "test-api-key",
                "units": "metric",
                "lang": "ru",
            },
        )


if __name__ == "__main__":
    unittest.main()
