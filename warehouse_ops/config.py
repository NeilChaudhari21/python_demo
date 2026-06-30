"""Configuration file loading."""

import configparser


def load_config(path: str) -> configparser.ConfigParser:
    parser = configparser.SafeConfigParser()
    parser.read(path)
    return parser


def get_config_value(parser: configparser.ConfigParser, section: str, option: str, default=None):
    if parser.has_option(section, option):
        return parser.get(section, option)
    return default
