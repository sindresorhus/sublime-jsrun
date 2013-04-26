import sublime
import sublime_plugin
from subprocess import call

try:
	from urllib.parse import quote
except ImportError:
	from urllib import quote


class JsRunCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		browser = sublime.load_settings('JsRun.sublime-settings').get('browser')
		selection = ''
		for region in self.view.sel():
			if region.empty():
				selection += self.view.substr(self.view.line(region)) + '\n'
			else:
				selection += self.view.substr(region) + '\n'
		selection = selection.strip().replace('"', '\\"')
		if not selection:
			return
		self.runjs(selection, browser)

	def _applescript(self, command):
		call(['osascript', '-e', command])

	def runjs(self, selection, browser):
		if browser == 'chrome':
			self._applescript("""
				tell application "Google Chrome" to execute front window's active tab javascript "%s"
			""" % selection)
		if browser == 'chrome_canary':
			self._applescript("""
				tell application "Google Chrome Canary" to execute front window's active tab javascript "%s"
			""" % selection)
		if browser == 'safari':
			self._applescript("""
				tell application "Safari" to do JavaScript "%s" in document 1
			""" % selection)
		if browser == 'opera':
			self._applescript("""
				tell application "Opera" to set URL of front window to "javascript:%s"
			""" % quote(selection))
