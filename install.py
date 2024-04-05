# -*- coding: utf-8 -*-
import os

url_prefix = 'http://mirror.fishros.com/install/'

base_url = url_prefix+'tools/base.py'

INSTALL_ROS = 0  # Install ROS-related
INSTALL_SOFTWARE = 1  # Install software
CONFIG_TOOL = 2  # Configuration tool


tools_type_map = {
    INSTALL_ROS: "ROS Related",
    INSTALL_SOFTWARE: "Common Software",
    CONFIG_TOOL: "Configuration Tool"
}


tools ={
    1: {'tip':'Installation: ROS (Supports ROS/ROS2, Raspberry Pi/Jetson)',  'type':INSTALL_ROS,     'tool':url_prefix+'tools/tool_install_ros.py' ,'dep':[2,3] },
    2: {'tip':'Configuration: ROS Environment (Quickly update ROS environment settings, automatically generate environment selection)',     'type':INSTALL_ROS,     'tool':url_prefix+'tools/tool_config_rosenv.py' ,'dep':[] },
    3: {'tip':'Installation: GitHub Desktop', 'type':INSTALL_SOFTWARE,     'tool':url_prefix+'tools/tool_install_github_desktop.py' ,'dep':[] },
    }


# Create a dictionary to store tools of different types
tool_categories = {}

# Traverse the tools dictionary and classify them according to the type value
for tool_id, tool_info in tools.items():
    tool_type = tool_info['type']
    # If the type has not been created in the dictionary yet, create a new list to store tools of that type
    if tool_type not in tool_categories:
        tool_categories[tool_type] = {}
    # Add tool information to the list of the corresponding type
    tool_categories[tool_type][tool_id]=tool_info


def main():
    # download base
    os.system("wget {} -O /tmp/fishinstall/{} --no-check-certificate".format(base_url,base_url.replace(url_prefix,'')))
    from tools.base import CmdTask,FileUtils,PrintUtils,ChooseTask,ChooseWithCategoriesTask
    from tools.base import encoding_utf8,osversion,osarch
    from tools.base import run_tool_file,download_tools
    from tools.base import config_helper
    # PrintUtils.print_delay(f"Detected your system version information as {osversion.get_codename()},{osarch}",0.001)
    # Usage statistics
    # CmdTask("wget https://fishros.org.cn/forum/topic/1733 -O /tmp/t1733 -q && rm -rf /tmp/t1733").run()

    # check base config
    if not encoding_utf8:
        print("Your system encoding not support, will install some packages..")
        # CmdTask("sudo apt-get install language-pack-zh-hans -y",0).run()
        CmdTask("sudo apt-get install apt-transport-https -y",0).run()
        # FileUtils.append("/etc/profile",'export LANG="zh_CN.UTF-8"')
        print('Finish! Please Try Again!')
        print('Solutions: https://fishros.org.cn/forum/topic/24 ')
        return False
    PrintUtils.print_success("Basic check passed...")

    tip = """===============================================================================
====== fish_install is open source: https://github.com/fishros/fish_install =======
===============================================================================
    """
    PrintUtils.print_delay(tip,0.001)

    # download tools
    choose_dic = {}
    code,result = ChooseWithCategoriesTask(tool_categories, tips="----Many tools, waiting for you to use----",categories=tools_type_map).run()

    if code==0: PrintUtils().print_success("Don't see anything you like? Contact Fish to add more menus~")
    download_tools(code,tools)
    run_tool_file(tools[code]['tool'].replace(url_prefix,'').replace("/","."))

    config_helper.gen_config_file()
    # PrintUtils.print_success("If you encounter any problems during use, please open: https://github.com/fishros/fish_install/issues for feedback",0.001)

if __name__=='__main__':
    main()
