# JsRun

Sublime plugin to run selected JavaScript code in the browser.


## Install

Install with [Package Control](http://wbond.net/sublime_packages/package_control)


## Getting started

Set your preferred browser in the settings: `chrome` (default), `chrome_canary`, `safari`, `opera`  
(Preferences > Package Settings > JsRun > Settings - User)

Select some code or just highlight a line and choose "Run JavaScript in the browser" in the Command Palette *(Cmd+Shift+P)*.

You can also set up a keyboard shortcut to run the command by opening up "Preferences > Key Bindings - User" and adding your shortcut with the command `js_run`.

Currently supports Chrome, Chrome Canary, Safari and Opera on OS X. Firefox doesn't [expose JS to AppleScript](https://bugzilla.mozilla.org/show_bug.cgi?id=5704).


## License

[MIT License](http://en.wikipedia.org/wiki/MIT_License)
(c) [Sindre Sorhus](http://sindresorhus.com)
