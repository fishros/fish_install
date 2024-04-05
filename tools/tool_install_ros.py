# -*- coding: utf-8 -*-
from pickle import NONE
from .base import BaseTool
from .base import PrintUtils, CmdTask, FileUtils, AptUtils, ChooseTask
from .base import osversion
from .base import run_tool_file


class RosVersion:
    STATUS_EOL = 0
    STATUS_LTS = 1
    def __init__(self, name, version, status, deps=[]):
        self.name = name
        self.version = version
        self.status = status
        self.deps = deps


class RosVersions:
    ros_version = [
        RosVersion('kinetic', 'ROS1', RosVersion.STATUS_EOL, ['python-catkin-tools', 'python-rosdep']),
        RosVersion('melodic', 'ROS1', RosVersion.STATUS_LTS, ['python-catkin-tools', 'python-rosdep']),
        RosVersion('noetic',  'ROS1', RosVersion.STATUS_LTS, ['python3-catkin-tools', 'python3-rosdep']),
        # ubuntu 20
        RosVersion('foxy',  'ROS2', RosVersion.STATUS_LTS, ['python3-colcon-common-extensions', 'python3-argcomplete', 'python3-rosdep']),
        RosVersion('galactic',  'ROS2', RosVersion.STATUS_LTS, ['python3-colcon-common-extensions', 'python3-argcomplete', 'python3-rosdep']),
        # ubuntu 22
        RosVersion('iron',  'ROS2', RosVersion.STATUS_LTS, ['python3-colcon-common-extensions', 'python3-argcomplete', 'python3-rosdep']),
        RosVersion('rolling',  'ROS2', RosVersion.STATUS_LTS, ['python3-colcon-common-extensions', 'python3-argcomplete', 'python3-rosdep']),
        RosVersion('humble',  'ROS2', RosVersion.STATUS_LTS, ['python3-colcon-common-extensions', 'python3-argcomplete', 'python3-rosdep']),
        RosVersion('eloquent',  'ROS2', RosVersion.STATUS_EOL, ['python3-colcon-common-extensions', 'python3-argcomplete', 'python3-rosdep']),
        RosVersion('dashing',  'ROS2', RosVersion.STATUS_EOL, []),
        RosVersion('crystal',  'ROS2', RosVersion.STATUS_EOL, []),
        RosVersion('bouncy',  'ROS2', RosVersion.STATUS_EOL, []),
        RosVersion('ardent',  'ROS2', RosVersion.STATUS_EOL, []),
        RosVersion('lunar', 'ROS2', RosVersion.STATUS_EOL, []),
    ]

    @staticmethod
    def get_version_string(name):
        for version in RosVersions.ros_version:
            if version.name == name:
                return "{}({})".format(version.name, version.version)

    @staticmethod
    def get_version(name):
        for version in RosVersions.ros_version:
            if version.name == name:
                return version
       
    @staticmethod
    def install_depend(name):
        depends = RosVersions.get_version(name).deps
        for dep in depends:
            AptUtils.install_pkg(dep)

    @staticmethod
    def tip_test_command(name):
        version = RosVersions.get_version(name).version
        if version == "ROS1":
            PrintUtils.print_warn("Little fish, yellow tip: You have installed ROS1. You can open a new terminal and type roscore to test!")
        elif version == "ROS2":
            PrintUtils.print_warn("Little fish: Yellow tip: You have installed ROS2. ROS2 does not have roscore. Please open a new terminal and type ros2 test! Little fish has created ROS2 course, follow the public account 'Fish Scented ROS' to get it~")

    @staticmethod
    def get_desktop_version(name):
        version = RosVersions.get_version(name).version
        if version == "ROS1":
            return "ros-{}-desktop-full".format(name)
        elif version == "ROS2":
            return "ros-{}-desktop".format(name)

ros_mirror_dic = {
    "https.packages.ros": {"ROS1": "https://packages.ros.org/ros/ubuntu/", "ROS2": "https://packages.ros.org/ros2/ubuntu/"},
    "tsinghua": {"ROS1": "http://mirrors.tuna.tsinghua.edu.cn/ros/ubuntu/", "ROS2": "http://mirrors.tuna.tsinghua.edu.cn/ros2/ubuntu/"},
    "huawei": {"ROS1": "https://repo.huaweicloud.com/ros/ubuntu/", "ROS2": "https://repo.huaweicloud.com/ros2/ubuntu/"},
    "packages.ros": {"ROS1": "http://packages.ros.org/ros/ubuntu/", "ROS2": "http://packages.ros.org/ros2/ubuntu/"},
    "repo-ros2": {"ROS2": "http://repo.ros2.org/ubuntu/"}
}

ros_dist_dic = {
    'artful': {"packages.ros"},
    'bionic': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'buster': {"packages.ros"},
    'cosmic': {"packages.ros"},
    'disco': {"packages.ros"},
    'eoan': {"packages.ros"},
    'focal': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'jessie': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'lucid': {"packages.ros"},
    'maverick': {"packages.ros"},
    'natty': {"packages.ros"},
    'oneiric': {"packages.ros"},
    'precise': {"packages.ros"},
    'quantal': {"packages.ros"},
    'raring': {"packages.ros"},
    'saucy': {"packages.ros"},
    'stretch': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'trusty': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'utopic': {"packages.ros"},
    'vivid': {"packages.ros"},
    'wheezy': {"packages.ros"},
    'wily': {"packages.ros"},
    'xenial': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'yakkety': {"packages.ros"},
    'zesty': {"packages.ros"},
}

ros2_dist_dic = {
    'bionic': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'bullseye': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'buster': {"packages.ros"},
    'cosmic': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'disco': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'eoan': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'focal': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'jessie': {"tsinghua", "huawei"},
    'jammy': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'stretch': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
    'trusty': {"tsinghua", "huawei"},
    'xenial': {"tsinghua", "huawei", "packages.ros", "https.packages.ros"},
}

class Tool(BaseTool):
    def __init__(self):
        self.name = "FishInstall Installation of ROS and ROS2, Support Raspberry Pi and Jetson"
        self.type = BaseTool.TYPE_INSTALL
        self.author = 'Little Fish'


    def get_mirror_by_code(self, code, arch='amd64', first_choose="tsinghua"):
        """
        Get mirror by system version number
        """
        ros1_choose_queue = [first_choose, "tsinghua", "huawei", "packages.ros"]
        ros2_choose_queue = [first_choose, "tsinghua", "huawei", "packages.ros"]
        
        # For armhf architecture, prioritize official sources
        if arch == 'armhf': 
            ros2_choose_queue = ["packages.ros", "tsinghua", "huawei"]

        mirror = []
        # Ensure that there are corresponding systems in the source, such as jammy
        if code in ros_dist_dic.keys():
            for item in ros1_choose_queue:
                if item in ros_dist_dic[code]:
                    mirror.append(ros_mirror_dic[item]['ROS1'])
                    break
         # Ensure that there are corresponding systems in the source, such as jammy
        if code in ros2_dist_dic.keys():
            for item in ros2_choose_queue:
                if item in ros2_dist_dic[code]:
                    mirror.append(ros_mirror_dic[item]['ROS2'])
                    break
        return mirror


    def add_key(self):
        # check apt
        if not AptUtils.checkapt(): 
            pass
            # Failure to check may cause subsequent installation failures
        # Pre-install
        AptUtils.install_pkg('curl')
        AptUtils.install_pkg('gnupg2')

        # Add key
        cmd_result = CmdTask("curl -s https://gitee.com/ohhuo/rosdistro/raw/master/ros.asc | sudo apt-key add -", 10).run()
        if cmd_result[0] != 0:
            cmd_result = CmdTask("curl -s https://gitee.com/ohhuo/rosdistro/raw/master/ros.asc | sudo apt-key add -", 10).run()
        if cmd_result[0] != 0:
            PrintUtils.print_info("Failed to import key. Changing import method and trying again...")
            cmd_result = CmdTask("sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F42ED6FBAB17C654", 10).run()
        if FileUtils.check_result(cmd_result, ['trusted.gpg.d']):
            cmd_result = CmdTask("curl -s https://gitee.com/ohhuo/rosdistro/raw/master/ros.asc | sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/ros.gpg --import", 10).run()
            cmd_result = CmdTask("sudo chmod 644 /etc/apt/trusted.gpg.d/ros.gpg", 10).run()
        return cmd_result


    def check_sys_source(self):
        # Change system source
        dic = {1: "Change system source and continue installation", 2: "Continue installation without changing source"}
        PrintUtils.print_warn("=========The following step is very important. If you don't know what to choose, please select 1========")
        code, result = ChooseTask(dic, "For novices or first-time installations, you must change the source and clean the third-party source. Change the source!!! The system default foreign source is prone to failure!!").run()
        if code == 1: 
            tool = run_tool_file('tools.tool_config_system_source', autorun=False)
            tool.change_sys_source()

    def get_all_instsll_ros_pkgs(self):
        AptUtils.checkapt()
        dic_base = AptUtils.search_package('ros-base', 'ros-[A-Za-z]+-ros-base', "ros-", "-base")
        if dic_base == None: 
            return None
        ros_name = {}
        for a in dic_base.keys(): 
            ros_name[RosVersions.get_version_string(a)] = a
        if len(ros_name) == 0:
            return None
        return ros_name

    def add_source(self):
        """
        Check and add ROS system sources
        """

        arch = AptUtils.getArch()
        if arch == None: 
            return False

        # Add source 1
        mirrors = self.get_mirror_by_code(osversion.get_codename(), arch=ArithmeticError, first_choose="https.packages.ros")
        PrintUtils.print_info("According to your system, the recommended installation source for you is {}".format(mirrors))
        source_data = ''
        for mirror in mirrors:
            source_data += 'deb [arch={}]  {} {} main\n'.format(arch, mirror, osversion.get_codename())
        FileUtils.delete('/etc/apt/sources.list.d/ros-fish.list')
        FileUtils.new('/etc/apt/sources.list.d/', "ros-fish.list", source_data)

        ros_pkg = self.get_all_instsll_ros_pkgs()
        if ros_pkg and len(ros_pkg) > 1:
            PrintUtils.print_success("Congratulations, ROS source added successfully. You can now install ROS using apt or use [1] to install ROS in one click!") 
            return
        
        # Add source 2 
        PrintUtils.print_warn("Update failed after source change. Starting the second time to switch sources, trying to change ROS2 source to Huawei source!") 
        mirrors = self.get_mirror_by_code(osversion.get_codename(), arch=arch, first_choose="packages.ros")
        PrintUtils.print_info("According to your system, the recommended installation source for you is {}".format(mirrors))
        source_data = ''
        for mirror in mirrors:
            source_data += 'deb [arch={}]  {} {} main\n'.format(arch, mirror, osversion.get_codename())
        FileUtils.delete('/etc/apt/sources.list.d/ros-fish.list')
        FileUtils.new('/etc/apt/sources.list.d/', "ros-fish.list", source_data)
        ros_pkg = self.get_all_instsll_ros_pkgs()
        if ros_pkg and len(ros_pkg) > 1:
            PrintUtils.print_success("Congratulations, ROS source added successfully. You can now install ROS using apt or use [1] to install ROS in one click!") 
            return

        # Add source 3 
        PrintUtils.print_warn("Update failed after source change. Starting the third time to switch sources, trying to change ROS2 source to ROS2 huawei!") 
        mirrors = self.get_mirror_by_code(osversion.get_codename(), arch=arch, first_choose="huawei")
        PrintUtils.print_info("According to your system, the recommended installation source for you is {}".format(mirrors))
        source_data = ''
        for mirror in mirrors:
            source_data += 'deb [arch={}]  {} {} main\n'.format(arch, mirror, osversion.get_codename())
        FileUtils.delete('/etc/apt/sources.list.d/ros-fish.list')
        FileUtils.new('/etc/apt/sources.list.d/', "ros-fish.list", source_data)
        ros_pkg = self.get_all_instsll_ros_pkgs()
        if ros_pkg and len(ros_pkg) > 1:
            PrintUtils.print_success("Congratulations, ROS source added successfully. You can now install ROS using apt or use [1] to install ROS in one click!") 
            return


        if  not AptUtils.checkapt(): 
            PrintUtils.print_error("Failed to update after four source changes. Please contact Little Fish immediately to obtain a solution and handle it!") 



    def support_install(self):
        # check support
        if (osversion.get_codename() not in ros_dist_dic.keys()) and (osversion.get_codename() not in ros2_dist_dic.keys()):
            PrintUtils.print_error("Little Fish: The current system {}{}:{} does not support FishInstall installation of ROS. Please follow the official account [Fish Roasted with ROS] for help.".format(osversion.get_name(), osversion.get_version(), osversion.get_codename()))
            return False
        PrintUtils.print_success("Little Fish: The current system {}{}:{} supports FishInstall installation of ROS".format(osversion.get_name(), osversion.get_version(), osversion.get_codename()))
        return True

    def install_success(self, name):
        """
        Check if a version of ROS is installed successfully
        """
        result = CmdTask("ls /opt/ros/{}/setup.bash".format(name), 0).run()
        if str(result[1]).find('setup.bash') >= 1:
            return True
        return False

    

    def choose_and_install_ros(self):
        # Search ROS packages
        dic_base = AptUtils.search_package('ros-base', 'ros-[A-Za-z]+-ros-base', "ros-", "-base")
        if dic_base == None: 
            return False

        ros_name = {}
        for a in dic_base.keys(): 
            ros_name[RosVersions.get_version_string(a)] = a

        code, rosname = ChooseTask(ros_name.keys(), "Please select the ROS version you want to install (please note the difference between ROS1 and ROS2):", True).run()
        if code == 0: 
            PrintUtils.print_error("You choose to exit...")
            return
        version_dic = {1: rosname + " Desktop Edition", 2: rosname + " Basic Edition (Small)"}
        code, name = ChooseTask(version_dic, "Please select the specific version to install (if you don't know how to choose, please select 1 Desktop Edition):", False).run()
        
        if code == 0: 
            print("You choose to exit...")
            return
        
        install_tool = 'aptitude'
        install_tool_apt = 'apt'
        if osversion.get_version() == "16.04":
            install_tool = 'apt'

        install_version = ros_name[rosname]

        if install_tool == 'aptitude':
            AptUtils.install_pkg('aptitude')
            AptUtils.install_pkg('aptitude')

        # Try apt installation first, then use aptitude.
        if code == 2:
            # First attempt
            cmd_result = CmdTask("sudo {} install  {} -y".format(install_tool_apt, dic_base[install_version]), 300, os_command=True).run()
            cmd_result = CmdTask("sudo {} install  {} -y".format(install_tool_apt, dic_base[install_version]), 300, os_command=False).run()
            if FileUtils.check_result(cmd_result, ['Unmet dependencies', 'unmet dependencies', 'but it is not installable']):
                # Try using aptitude to solve dependency problems
                PrintUtils.print_warn("============================================================")
                PrintUtils.print_delay("Please pay attention to me. If you encounter dependency problems during installation, enter n later, and then select y to resolve it")
                import time
                input("Confirm that you understand the situation, please press Enter to continue the installation")
                cmd_result = CmdTask("sudo {} install   {} ".format(install_tool, install_version), 300, os_command=True).run()
                cmd_result = CmdTask("sudo {} install   {} -y".format(install_tool, dic_base[install_version]), 300, os_command=False).run()
        
        elif code == 1:
            cmd_result = CmdTask("sudo {} install   {} -y".format(install_tool_apt, RosVersions.get_desktop_version(install_version)), 300, os_command=True).run()
            cmd_result = CmdTask("sudo {} install   {} -y".format(install_tool_apt, RosVersions.get_desktop_version(install_version)), 300, os_command=False).run()
            if FileUtils.check_result(cmd_result, ['Unmet dependencies', 'unmet dependencies', 'but it is not installable']):
                # Try using aptitude to solve dependency problems
                PrintUtils.print_warn("============================================================")
                PrintUtils.print_delay("Please pay attention to me. If you encounter dependency problems during installation, enter n later, and then select y to resolve it (If it cannot be resolved, try to install the basic version)")
                import time
                input("Confirm that you understand the situation, please press Enter to continue the installation")
                cmd_result = CmdTask("sudo {} install   {} ".format(install_tool, RosVersions.get_desktop_version(install_version)), 300, os_command=True).run()
                cmd_result = CmdTask("sudo {} install   {} -y".format(install_tool, RosVersions.get_desktop_version(install_version)), 300, os_command=False).run()

        # Verify installation results
        rosname = install_version
        if self.install_success(rosname):
            PrintUtils.print_success("Congratulations, {} installation was successful! ".format(rosname))
            if rosname == "ROS1":
                RosVersions.install_depend(rosname.lower())
                RosVersions.tip_test_command(rosname.lower())
            elif rosname == "ROS2":
                RosVersions.install_depend(rosname.lower())
                RosVersions.tip_test_command(rosname.lower())
        else:
            PrintUtils.print_error("Failed to install {}, please contact Little Fish for assistance.".format(rosname))


    def run(self):
        """
        Perform automatic installation
        """
        if not self.support_install(): 
            return
        if not AptUtils.checkapt(): 
            PrintUtils.print_error("Sorry, apt update failed. This will affect the installation of ROS, please contact the system administrator to solve it!")
            return
        # Check and add ROS system sources
        # self.check_sys_source()
        self.add_source()

        # install ROS
        self.choose_and_install_ros()
