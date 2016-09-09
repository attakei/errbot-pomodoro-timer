import os
import time
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
        assert len(plugin._runners) == 1
        assert isinstance(list(plugin._runners.keys())[0], str) is True
        id_ = testbot.bot.build_identifier(list(plugin._runners.keys())[0])
        assert isinstance(id_, Person) is True

    def test_stop_not_started(self, testbot):
        testbot.push_message('!pomodoro_stop')
        plugin = self.fetch_plugin(testbot)
        assert plugin._runners == {}

    def test_start_and_stop(self, testbot):
        testbot.push_message('!pomodoro_start')
        testbot.push_message('!pomodoro_stpo')
        plugin = self.fetch_plugin(testbot)
        assert plugin._runners == {}

    def test_run_pomodoro_none_user(self, testbot):
        plugin = self.fetch_plugin(testbot)
        plugin.pomodoro()
        assert plugin._runners == {}

    def test_run_pomodoro_one_user(self, testbot):
        testbot.push_message('!pomodoro_start')
        time.sleep(0.5)
        plugin = self.fetch_plugin(testbot)
        runner = list(plugin._runners.keys())[0]
        plugin.pomodoro()
        assert plugin._runners[runner] == 1
        plugin.pomodoro()
        assert plugin._runners[runner] == 2

    def test_run_pomodoro_turn_to_rest(self, testbot):
        testbot.push_message('!pomodoro_start')
        time.sleep(0.5)
        plugin = self.fetch_plugin(testbot)
        runner = list(plugin._runners.keys())[0]
        [ plugin.pomodoro() for _ in range(25)]
        assert plugin._runners[runner] == -5
