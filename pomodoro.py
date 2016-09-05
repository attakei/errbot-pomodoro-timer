# -*- coding:utf8 -*-
from __future__ import division, print_function, absolute_import
"""Pomodoro timer
"""
from errbot import BotPlugin, botcmd
from time import sleep


class Pomodoro(BotPlugin):
    CONCENTRATE_SECS = 25 * 60
    REST_SECS = 5 * 60

    def activate(self):
        super().activate()
        self['timer'] = False

    @botcmd(name='pomodoro_start')
    def start_pomodoro(self, msg, args):
        if self['timer']:
            return
        self['timer'] = True
        while self['timer']:
            yield "Let's go concentration!!"
            sleep(self.CONCENTRATE_SECS)
            if not self['timer']:
                break
            yield "Rest ..."
            sleep(self.REST_SECS)

    @botcmd(name='pomodoro_stop')
    def stop_pomodoro(self, msg, args):
        if self['timer']: 
            self['timer'] = False
            return 'Timer stopped.'
