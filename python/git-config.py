# -*- coding: UTF-8 -*-

"""
Authors: Carry·Leng

Date: 2020/03/01 18:11:00
"""

from Utils import isEmpty
from data.ConfigData import ConfigData

import os


def setConfig(attr, value, git_local = False, git_global = False, git_system = False):
    if isEmpty(attr):
        print("set attribute is empty!")
        return None
    if isEmpty(value):
        value = ""
        print("set attribute:%s value is empty!"%attr)
    data = ConfigData()
    if git_system:
        result = execSetConfig("--system", attr, value)
        data.setSystemConfig(attr, result)
    if git_global:
        result = execSetConfig("--global", attr, value)
        data.setGlobalConfig(attr, result)
    if git_local:
        result = execSetConfig("--local", attr, value)
        data.setLocalConfig(attr, result)
    if not git_local and not git_global and not git_system:
        result = execSetConfig("", attr, value)
        data.setLocalConfig(attr, result)

    return data


def addConfig(attr, value, git_local = False, git_global = False, git_system = False):
    if isEmpty(attr):
        print("add attribute is empty!")
        return None
    if isEmpty(value):
        value = ""
        print("add attribute:%s value is empty!"%attr)
    data = ConfigData()
    if git_system:
        result = execSetConfig("--system", attr, value, "--add")
        for value in result.splitlines():
            data.setSystemConfig(attr, value.strip())
    if git_global:
        result = execSetConfig("--global", attr, value, "--add")
        for value in result.splitlines():
            data.setGlobalConfig(attr, value.strip())
    if git_local:
        result = execSetConfig("--local", attr, value, "--add")
        for value in result.splitlines():
            data.setLocalConfig(attr, value.strip())
    if not git_local and not git_global and not git_system:
        result = execSetConfig("", attr, value, "--add")
        for value in result.splitlines():
            data.setLocalConfig(attr, value.strip())

    return data


def getConfig(attr, get_all = False, git_local = False, git_global = False, git_system = False):
    if isEmpty(attr):
        print("get attribute is empty!")
        return None
    get_mode = "--get"
    if get_all:
        get_mode = "--get-all"
    data = ConfigData()
    if git_system:
        result = execGetConfig("--system", attr, get_mode)
        for value in result.splitlines():
            data.setSystemConfig(attr, value.strip())
    if git_global:
        result = execGetConfig("--global", attr, get_mode)
        for value in result.splitlines():
            data.setGlobalConfig(attr, value.strip())
    if git_local:
        result = execGetConfig("--local", attr, get_mode)
        for value in result.splitlines():
            data.setLocalConfig(attr, value.strip())
    if not git_local and not git_global and not git_system:
        result = execGetConfig("", attr, get_mode)
        for value in result.splitlines():
            data.setLocalConfig(attr, value.strip())
    
    return data


def delConfig(attr, del_all = False, git_local = False, git_global = False, git_system = False):
    if isEmpty(attr):
        print("del attribute is empty!")
        return None
    del_mode = "--unset"
    if del_all:
        del_mode = "--unset-all"
    data = ConfigData()
    if git_system:
        result = execDelConfig("--system", attr, del_mode)
        for value in result.splitlines():
            data.setSystemConfig(attr, value.strip())
    if git_global:
        result = execDelConfig("--global", attr, del_mode)
        for value in result.splitlines():
            data.setGlobalConfig(attr, value.strip())
    if git_local:
        result = execDelConfig("--local", attr, del_mode)
        for value in result.splitlines():
            data.setLocalConfig(attr, value.strip())
    if not git_local and not git_global and not git_system:
        result = execDelConfig("", attr, del_mode)
        for value in result.splitlines():
            data.setLocalConfig(attr, value.strip())

    return data

def loadConfig(git_local = False, git_global = False, git_system = False):
    data = ConfigData()
    if not git_local and not git_global and not git_system:
        git_local = True
        git_global = True
        git_system = True
    if git_system:
        result = execLoadConfig("--system")
        for line in result.splitlines():
            key_value_pair = line.strip().split("=")
            if len(key_value_pair) == 1:
                data.setSystemConfig(key_value_pair[0], "")
            elif len(key_value_pair) == 2:
                data.setSystemConfig(key_value_pair[0].strip(), key_value_pair[1].strip())
            elif len(key_value_pair) > 2:
                raise Exception("git config --system %s not a key value pair!"%line)
    if git_global:
        result = execLoadConfig("--global")
        for line in result.splitlines():
            key_value_pair = line.strip().split("=")
            if len(key_value_pair) == 1:
                data.setGlobalConfig(key_value_pair[0], "")
            elif len(key_value_pair) == 2:
                data.setGlobalConfig(key_value_pair[0], key_value_pair[1])
            elif len(key_value_pair) > 2:
                raise Exception("git config --global %s not a key value pair!"%line)
    if git_local:
        result = execLoadConfig("--local")
        for line in result.splitlines():
            key_value_pair = line.strip().split("=")
            if len(key_value_pair) == 1:
                data.setLocalConfig(key_value_pair[0], "")
            elif len(key_value_pair) == 2:
                data.setLocalConfig(key_value_pair[0], key_value_pair[1])
            elif len(key_value_pair) > 2:
                raise Exception("git config --local %s not a key value pair!"%line) 

    return data


def setConfigUserName(user_name, git_local = False, git_global = False, git_system = False):
    setConfig("user.name", user_name, git_local, git_global, git_system)


def getConfigUserName(git_local = False, git_global = False, git_system = False):
    getConfig("user.name", False, git_local, git_global, git_system)


def delConfigUserName(git_local = False, git_global = False, git_system = False):
    delConfig("user.name", False, git_local, git_global, git_system)


def setConfigUserEmail(user_email, git_local = False, git_global = False, git_system = False):
    setConfig("user.email", user_email, git_local, git_global, git_system)


def getConfigUserEmail(git_local = False, git_global = False, git_system = False):
    getConfig("user.email", False, git_local, git_global, git_system)


def delConfigUserEmail(git_local = False, git_global = False, git_system = False):
    delConfig("user.email", False, git_local, git_global, git_system)


def execGetConfig(level, attr, mode = "--get"):
    get_cmd = "git config %s %s %s"%(level, mode, attr)
    print(get_cmd)
    result = os.popen(get_cmd).read().strip()
    print(result)
    return result


def execLoadConfig(level):
    load_cmd = "git config %s -l"%(level)
    print(load_cmd)
    result = os.popen(load_cmd).read().strip()
    print(result)
    return result


def execDelConfig(level, attr, mode = "--unset"):
    del_cmd = 'git config %s %s %s'%(level, mode, attr)
    print(del_cmd)
    get_mode = "--get"
    if mode == "--unset-all":
        get_mode = "--get-all"
    old_value = execGetConfig(level, attr, get_mode)
    result = os.popen(del_cmd).read().strip()
    print(result)
    if result:
        raise Exception(result)
    return old_value


def execSetConfig(level, attr, value, mode = ""):
    set_cmd = 'git config %s %s %s "%s"'%(level, mode, attr, value)
    print(set_cmd)
    result = os.popen(set_cmd).read().strip()
    print(result)
    if result:
        raise Exception(result)
    if mode == "--add":
        return execGetConfig(level, attr, "--get-all")
    return execGetConfig(level, attr)


if __name__ == "__main__":
    data = setConfig("carry.set1", "1", True)
    print(data)
    print("=====================")
    data = setConfig("carry.set2", "2", True, True)
    print(data)
    print("=====================")
    data = setConfig("carry.set3", "3", True, True, True)
    print(data)
    print("=====================")
    data = addConfig("carry.add", "1", True)
    print(data)
    print("=====================")
    data = addConfig("carry.add", "2" , True, True)
    print(data)
    print("=====================")
    data = addConfig("carry.add", "3", True, True, True)
    print(data)
    print("=====================")
    data = delConfig("carry.set1", git_local = True)
    print(data)
    print("=====================")
    data = delConfig("carry.set2", git_local = True, git_global = True)
    print(data)
    print("=====================")
    data = delConfig("carry.set3", git_local = True, git_global = True, git_system = True)
    print(data)
    print("=====================")
    data = delConfig("carry.add", True, True)
    print(data)
    print("=====================")
    data = delConfig("carry.add", True, True, True)
    print(data)
    print("=====================")
    data = delConfig("carry.add", False, True, True, True)
    print(data)
    print("=====================")
    data = loadConfig()
    print(data)
    print("=====================")
    