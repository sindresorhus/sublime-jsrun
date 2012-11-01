# JsRun

Sublime plugin to run selected JavaScript code in the browser.


## Install

Install with [Package Control](http://wbond.net/sublime_packages/package_control) and restart Sublime.


## Getting started

Select some code or just highlight a line and choose "Run JavaScript in the browser" in the Command Palette *(Cmd+Shift+P)*. This will then run the command in the active tab in the frontmost browser window. Switch to the browser window to see the result, and optionally open the Console (Dev Tools) to see console.log output.

Set your preferred browser in the settings: `chrome` (default), `chrome_canary`, `safari`, `opera`  
(Preferences > Package Settings > JsRun > Settings - User)

You can also set up a keyboard shortcut to run the command by opening up "Preferences > Key Bindings - User" and adding your shortcut with the command `js_run`.

Currently supports Chrome, Chrome Canary, Safari and Opera on OS X. Firefox doesn't [expose JS to AppleScript](https://bugzilla.mozilla.org/show_bug.cgi?id=5704).


## License

[MIT License](http://en.wikipedia.org/wiki/MIT_License)
(c) [Sindre Sorhus](http://sindresorhus.com)
