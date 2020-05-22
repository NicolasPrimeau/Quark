from dataclasses import dataclass


@dataclass
class Alias:
    alias: str = None
    link: str = None


@dataclass
class Registration:
    link: str = None
