# -*- coding:utf8 -*-
from __future__ import division, print_function, absolute_import
"""Pomodoro timer
"""
from errbot import BotPlugin, botcmd


class Pomodoro(BotPlugin):
    WORK_MIN = 25
    REST_MIN = 5

    def activate(self):
        super().activate()
        self['timer'] = None
        self['target'] = None
        self.start_poller(60, self.pomodoro)

    def pomodoro(self):
        if self['timer'] is None:
            return
        time_counter = self['timer'] + 1
        if time_counter >= self.WORK_MIN:
            time_counter = -1 * self.REST_MIN
            self.send(self['target'], "Please rest for about {} minutes".format(self.REST_MIN))
        elif time_counter == 0:
            self.send(self['target'], "Let's work you about {} minutes".format(self.WORK_MIN))
        self['timer'] = time_counter

    @botcmd(name='pomodoro_start')
    def start(self, msg, args):
        if self['timer'] is not None:
            return
        yield 'Start timer'
        self['timer'] = 0
        self['target'] = msg.frm

    @botcmd(name='pomodoro_stop')
    def stop(self, msg, args):
        if self['timer'] is None:
            return
        yield 'Stop timer'
        self['timer'] = None
        self['target'] = None
