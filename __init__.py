# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
import datetime

currentDT = datetime.datetime.now()

__author__ = 'drewlg'

class GoodMorningSkill(MycroftSkill):
    def __init__(self):
        super(GoodMorningSkill, self).__init__(name="GoodMorningSkill")

    def initialize(self):
        thank_you_intent = IntentBuilder("ThankYouIntent"). \
            require("ThankYouKeyword").build()
        self.register_intent(thank_you_intent, self.handle_thank_you_intent)

        how_are_you_intent = IntentBuilder("HowAreYouIntent"). \
            require("HowAreYouKeyword").build()
        self.register_intent(how_are_you_intent,
                             self.handle_how_are_you_intent)

        good_morning_intent = IntentBuilder("GoodMorningIntent"). \
            require("GoodMorningKeyword").build()
        self.register_intent(good_morning_intent,
                             self.handle_good_morning_intent)

    def handle_how_are_you_intent(self, message):
        self.speak_dialog("how.are.you")

    if currentDT  < datetime.time(17, 0, 0, 78915):
        def handle_good_morning_intent(self, message):
            self.speak_dialog("good.morning")
    else:
        def handle_good_morning_intent(self, message):
            self.speak_dialog("good.evening")

    def stop(self):
        pass


def create_skill():
    return GoodMorningSkill()
