# -*- coding: utf-8 -*-
from .base import BaseTool
from .base import PrintUtils, CmdTask, FileUtils, AptUtils, ChooseTask
from .base import osversion, osarch
from .base import run_tool_file

class Tool(BaseTool):
    def __init__(self):
        self.name = "FishInstall Installation of Vscode"
        self.type = BaseTool.TYPE_INSTALL
        self.author = 'Fish'

    def install_vscode(self):
        PrintUtils.print_info("Starting to download the corresponding version of vscode based on system architecture.")
        # Download different versions of installation packages based on system architecture
        if osarch == 'amd64':
            CmdTask('sudo wget https://vscode.download.prss.microsoft.com/dbazure/download/stable/903b1e9d8990623e3d7da1df3d33db3e42d80eda/code_1.86.2-1707854558_amd64.deb -O /tmp/vscode.deb', os_command=True).run()
        elif osarch == 'arm64':
            CmdTask('sudo wget https://vscode.download.prss.microsoft.com/dbazure/download/stable/903b1e9d8990623e3d7da1df3d33db3e42d80eda/code_1.86.2-1707853305_arm64.deb -O /tmp/vscode.deb', os_command=True).run()
        else:
            return False
        PrintUtils.print_info("Download complete. Next, installing Vscode for you.")
        CmdTask("sudo dpkg -i /tmp/vscode.deb").run()
        CmdTask("rm -rf /tmp/vscode.deb").run()
        PrintUtils.print_info("Installation completed.")

    def run(self):
        self.install_vscode()
