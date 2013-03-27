import sublime, sublime_plugin

class ScrollUpWithCaretCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.insert(edit, 0, "Hello, World!")
        self.view.run_command("move", {"by": "lines", "forward": False})
        self.view.run_command("scroll_lines", {"amount": 1.0 })

class ScrollDownWithCaretCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.insert(edit, 0, "Hello, World!")
        self.view.run_command("move", {"by": "lines", "forward": True})
        self.view.run_command("scroll_lines", {"amount": -1.0 })
