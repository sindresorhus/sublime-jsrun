import sublime
import sublime_plugin
import urllib
from subprocess import call


settings = sublime.load_settings('JsRun.sublime-settings')


class JsRunCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = ''
		for region in self.view.sel():
			if region.empty():
				selection += self.view.substr(self.view.line(region)) + '\n'
			else:
				selection += self.view.substr(region) + '\n'
		selection = selection.strip().replace('"', '\\"')
		if selection in ('', '\n'):
			return
		self.runjs(selection)

	def _applescript(self, command):
		call(['osascript', '-e', command])

	def runjs(self, selection):
		browser = settings.get('browser')
		if browser == 'chrome':
			self._applescript("""
				tell application "Google Chrome"
					execute front window's active tab javascript "%s"
				end tell
			""" % selection)
		if browser == 'chrome_canary':
			self._applescript("""
				tell application "Google Chrome Canary"
					execute front window's active tab javascript "%s"
				end tell
			""" % selection)
		if browser == 'safari':
			self._applescript("""
				tell application "Safari" to do JavaScript "%s" in document 1
			""" % selection)
		if browser == 'opera':
			self._applescript("""
				tell application "Opera"
					activate
					set URL of front window to "javascript:%s"
				end tell
			""" % urllib.quote(selection))
