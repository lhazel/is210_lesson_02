#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

FISHY= inquisition.SPANISH.replace("surprise","haddock")
VALUE_OF= len("Spanish")
INDEX_VALUE=FISHY.index("Spanish")
FLEMISH= FISHY[:INDEX_VALUE] + "Flemish"+FISHY[26:]
