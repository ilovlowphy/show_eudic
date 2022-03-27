# -*- coding: utf-8 -*-
#  Copyright (C) 2012 Christopher Brochtrup
#
#  This file is part of show_eudic
#
#  show_eudic is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  show_eudic is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with show_eudic.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
# Description:
#
# show_eudic will automatically copy a single card field to the clipboard
# when either the card's question side is shown or when the card's answer side
# is shown (or both, if desired).
#
# Default behavior:
#
#   * When the card's question is shown:
#       Nothing will be copied to the clipboard.
#
#   * When the card's answer is shown:
#       The card's "Expression" field will be copied to the clipboard (if one exists).
#
# To change the default behavior simply edit the questionField or answerField
# variables via Anki - Tools - Add-ons - copy2clipboard - Config.
#
###############################################################################
# Version: 1.0
# Tested with Anki 2.1.49
# Contact: ilovlowphy88@163.com
###############################################################################

#### Includes ####

from aqt import mw
from aqt.reviewer import Reviewer
from anki.hooks import wrap
from PyQt5.QtWidgets import QApplication
from os import popen

#### Default User Options (config.json) ####

# {
#   The name of the field to copy to the clipboard when the question side of the
#   card is shown. Case sensitive. If you don't want to copy, set to a blank string.
# 
#   "questionField": "Front",
#   
#   The name of the field to copy to the clipboard when the answer side of the
#   card is shown. Case sensitive. If you don't want to copy, set to a blank string.
# 
#   "answerField": ""
# }

#### Functions ####

def copyTextToClipboard(text):
    clipboard = QApplication.clipboard()
    clipboard.setText(text)


def copyField(fieldToCopy, card):
    for field in card.model()['flds']:
        fieldName = field['name']
        if(fieldName == fieldToCopy):
            value = card.note()[fieldName]
            copyTextToClipboard(value)
            cmd='start /b eudic -w '+str(value)
            popen(cmd)

def wrapped_showQuestion(self):
    config = mw.addonManager.getConfig(__name__)
    copyField(config['questionField'], self.card)


def wrapped_showAnswer(self):
    config = mw.addonManager.getConfig(__name__)
    copyField(config['answerField'], self.card)


#### Main ####

Reviewer._showQuestion = wrap(Reviewer._showQuestion, wrapped_showQuestion)
Reviewer._showAnswer = wrap(Reviewer._showAnswer, wrapped_showAnswer)
