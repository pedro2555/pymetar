#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pymetar
Copyright (C) 2018  Pedro Rodrigues <prodrigues1990@gmai.com>

This file is part of pymetar.

pymetar is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

pymetar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pymetar.  If not, see <http://www.gnu.org/licenses/>.
"""

import unittest

from pymetar import Metar


class TestMetarStation(unittest.TestCase):

    def test_metar_parsestation_withvalid(self):
        test = Metar('METAR X000 010000Z 00000KT CAVOK 10/10 Q1013')
        self.assertEqual(test.station, 'X000')

    def test_metar_parsestation_withinvalid(self):
        with self.assertRaises(ValueError):
            Metar('METAR 0000 010000Z 00000KT CAVOK 10/10 Q1013')
