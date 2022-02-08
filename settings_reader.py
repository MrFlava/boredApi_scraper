import os
import json
import logging


def read_settings_from_json(dir_path: str):
    """
    Getting script settings from settings.json
    Args:
        :param dir_path: str - path of directory
        :return settings: dict - script settings
    """

    try:
        settings_json_file_path = os.path.join(dir_path, 'settings.json')

        with open(settings_json_file_path, "r") as jsonFile:
            settings = json.load(jsonFile)

        return settings

    except Exception as e:
        logging.error(f'read_settings_from_json: {e}')
