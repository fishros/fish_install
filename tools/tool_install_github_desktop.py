# -*- coding: utf-8 -*-
from .base import BaseTool
from .base import PrintUtils, CmdTask, FileUtils, AptUtils, ChooseTask
from .base import osversion
from .base import run_tool_file

class Tool(BaseTool):
    def __init__(self):
        self.type = BaseTool.TYPE_INSTALL
        self.name = "Install GitHub Desktop Version"
        self.author = 'Fish'

    def install_github(self):
        CmdTask('sudo wget https://github.com/shiftkey/desktop/releases/download/release-2.9.12-linux4/GitHubDesktop-linux-2.9.12-linux4.deb -O /tmp/github.deb', os_command=True).run()
        CmdTask('sudo dpkg -i  /tmp/github.deb').run()
        CmdTask('sudo apt install /tmp/github.deb -y').run()

    def run(self):
        # Formal operation
        self.install_github()
