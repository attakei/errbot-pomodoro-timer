import os
from errbot.backends.test import testbot, FullStackTest
from errbot.backends.base import Person


class PomodoroPluginTests(object):
    extra_plugin_dir = '.'

    def fetch_plugin(self, testbot):
        return testbot.bot.plugin_manager.get_plugin_obj_by_name('Pomodoro')

    def test_start(self, testbot):
        testbot.push_message('!pomodoro_start')
        assert 'Start timer' in testbot.pop_message()
        plugin = self.fetch_plugin(testbot)
        assert plugin._timer[0] == 0
        assert isinstance(plugin._timer[1], Person) is True

    def test_stop_not_started(self, testbot):
        testbot.push_message('!pomodoro_stop')
        plugin = self.fetch_plugin(testbot)
        assert plugin._timer == [None, None]

    def test_start_and_stop(self, testbot):
        testbot.push_message('!pomodoro_start')
        testbot.push_message('!pomodoro_stpo')
        plugin = self.fetch_plugin(testbot)
        assert plugin._timer == [None, None]
