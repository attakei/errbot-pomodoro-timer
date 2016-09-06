# -*- coding:utf8 -*-
from __future__ import division, print_function, absolute_import
"""Pomodoro timer
"""
from errbot import BotPlugin, botcmd
from time import sleep


class Pomodoro(BotPlugin):
    WORK_SECS = 25 * 60
    REST_SECS = 5 * 60

    def activate(self):
        super().activate()
        self['runners'] = []

    def pomodoro(self, user):
        identifier = self.build_identifier(user)
        self.send(identifier, "Let's go work!")
        sleep(self.WORK_SECS)
        if user not in self['runners']:
            return
        self.send(identifier, "Rest...")
        sleep(self.REST_SECS)

    @botcmd(name='pomodoro_start')
    def start(self, msg, args):
        target = str(msg.frm) 
        if target in self['runners']:
            return
        targets = self['runners']
        targets.append(target)
        self['runners'] = targets
        self.start_poller(
            self.WORK_SECS + self.REST_SECS,
            self.pomodoro,
            (target, )
        )
        self.pomodoro(target)

    @botcmd(name='pomodoro_stop')
    def stop(self, msg, args):
        target = str(msg.frm) 
        if target not in self['runners']:
            return
        targets = self['runners']
        targets.remove(target)
        self['runners'] = targets
        self.stop_poller(self.pomodoro, (target,))
        identifier = self.build_identifier(target)
        self.send(identifier, 'Timer stopped.')
