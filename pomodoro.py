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
        self._runners = {}
        self.start_poller(60, self.pomodoro)

    def pomodoro(self):
        for runner, counter in self._runners.items():
            counter += 1
            # Timer count events
            if counter >= self.WORK_MIN:
                counter = -1 * self.REST_MIN
                message = "Please rest for about {} minutes".format(self.REST_MIN)
            elif counter == 0:
                message = "Let's work you about {} minutes".format(self.WORK_MIN)
            else:
                message = None
            # Post having message
            if message is not None:
                identifier = self.build_identifier(runner)
                self.send(identifier, message)
            self._runners[runner] = counter

    @botcmd(name='pomodoro_start')
    def start(self, msg, args):
        runner = str(msg.frm)
        if runner in self._runners:
            return
        yield 'Start timer'
        self._runners[runner] = 0

    @botcmd(name='pomodoro_stop')
    def stop(self, msg, args):
        runner = str(msg.frm)
        if runner not in self._runners:
            return
        yield 'Stop timer'
        del self._runners[runner]
