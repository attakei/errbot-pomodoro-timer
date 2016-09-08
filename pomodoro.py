# -*- coding:utf8 -*-
from __future__ import division, print_function, absolute_import
"""Pomodoro timer
"""
from errbot import BotPlugin, botcmd


class Pomodoro(BotPlugin):
    WORK_MIN = 25
    REST_MIN = 5

    def __init__(self, bot):
        super().__init__(bot)
        self._timer = [None, None]

    def activate(self):
        super().activate()
        self.start_poller(60, self.pomodoro)

    def pomodoro(self):
        time_counter = self._timer[0]
        target = self._timer[1]
        if time_counter is None:
            return
        time_counter += 1
        if time_counter >= self.WORK_MIN:
            time_counter = -1 * self.REST_MIN
            self.send(target, "Please rest for about {} minutes".format(self.REST_MIN))
        elif time_counter == 0:
            self.send(target, "Let's work you about {} minutes".format(self.WORK_MIN))
        self._timer[0] = time_counter

    @botcmd(name='pomodoro_start')
    def start(self, msg, args):
        if self._timer != [None, None]:
            return
        yield 'Start timer'
        self._timer = [0, msg.frm]

    @botcmd(name='pomodoro_stop')
    def stop(self, msg, args):
        if self._timer == [None, None]:
            return
        yield 'Stop timer'
        self._timer = [None, None]
