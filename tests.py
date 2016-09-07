import os
from errbot.backends.test import testbot


class PomodoroPluginTests(object):
    extra_plugin_dir = '.'

    def test_command(self, testbot):
        testbot.push_message('!pomodoro_start')
        assert 'Start timer' in testbot.pop_message()
