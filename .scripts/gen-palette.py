#!/usr/bin/python3

import re

with open("../themes/Steffula-color-theme.json") as file:
    while line := file.readline():
        if match := re.search(r'''["']name["']: ?["']([a-z-]+)["'],''', line):
            name = match.group(1)
            while line := file.readline():
                if match := re.search(r'''["']foreground["']: ?["'][#]([0-9a-f]+)["'],''', line):
                    color = match.group(1)
                    print(f"- ![{name}](https://img.shields.io/static/v1?style=flat-square&label={name}&color={color}&message=%23{color})")
                    break
