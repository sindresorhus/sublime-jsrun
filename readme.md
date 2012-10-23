# JsRun

Sublime plugin to run selected JavaScript code in the browser.


## Install

Install with [Package Control](http://wbond.net/sublime_packages/package_control)

While the plugin is in Package Control queue you can get it by choosing `Package Control: Add repository` in the Command Palette *(Cmd+Shift+P)* and enter `https://raw.github.com/sindresorhus/sublime-jsrun/master/packages.json`. Then just install it normally through Package Control.


## Getting started

Set your browser in the settings: `chrome` (default), `chrome_canary`, `safari`, `opera`.

Select some text or just highlight a line and choose "Run JavaScript in the browser" in the Command Palette *(Cmd+Shift+P)*.

You can also set up a keyboard shortcut to run the command by opening up `Preferences -> Key Bindings - User` and adding your shortcut with the command `js_run`.

Currently supports Chrome, Chrome Canary, Safari and Opera on OS X. Firefox doesn't [expose JS to AppleScript](https://bugzilla.mozilla.org/show_bug.cgi?id=5704).


## License

[MIT License](http://en.wikipedia.org/wiki/MIT_License)
(c) [Sindre Sorhus](http://sindresorhus.com)
