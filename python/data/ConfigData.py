# -*- coding: UTF-8 -*-

"""
Authors: Carry·Leng

Date: 2020/03/01 22:11:00
"""

class ConfigData(object):

    local_config = None

    global_config = None

    system_config = None

    """docstring for ConfigData"""
    def __init__(self):
        super(ConfigData, self).__init__()
        self.system_config = GitConfig()

    def setLocalConfig(self, attr, value):
        if self.local_config is None:
            self.local_config = GitConfig()
        self.local_config.setKeyValuePair(attr, value)

    def getLocalConfig(self, attr, def_value = None):
        if self.local_config is None:
            return def_value
        return self.local_config.getKeyValuePair(attr, def_value)

    def setGlobalConfig(self, attr, value):
        if self.global_config is None:
            self.global_config = GitConfig()
        self.global_config.setKeyValuePair(attr, value)

    def getGlobalConfig(self, attr, def_value = None):
        if self.global_config is None:
            return def_value
        return self.global_config.getKeyValuePair(attr, def_value)

    def setSystemConfig(self, attr, value):
        if self.system_config is None:
            self.system_config = GitConfig()
        self.system_config.setKeyValuePair(attr, value)

    def getSystemConfig(self, attr, def_value = None):
        if self.system_config is None:
            return def_value
        return self.system_config.getKeyValuePair(attr, def_value)

    def getConfig(self, attr, def_value = None):
        value = self.getLocalConfig(attr)
        if value is None:
            value = self.getGlobalConfig(attr)
            if value is None:
                value = self.getSystemConfig(attr)
        if value is None:
            return def_value
        return value

    def __str__(self):
        config_list = []
        config_list.append("[system_config]\n")
        if self.system_config is not None:
            config_list.append(self.system_config.__str__())
        config_list.append("[global_config]\n")
        if self.global_config is not None:
            config_list.append(self.global_config.__str__())
        config_list.append("[local_config]\n")
        if self.local_config is not None:
            config_list.append(self.local_config.__str__())
        return "\n".join(config_list)
        

class GitConfig(object):

    key_value_pair_dict = None

    """docstring for GitConfig"""
    def __init__(self):
        super(GitConfig, self).__init__()
        self.key_value_pair_dict = {}
        
    def setKeyValuePair(self, attr, value):
        if self.key_value_pair_dict.has_key(attr):
            if isinstance(self.key_value_pair_dict[attr], list):
                self.key_value_pair_dict[attr].append(value)
            else:
                values = []
                values.append(self.key_value_pair_dict[attr])
                values.append(value)
                self.key_value_pair_dict[attr] = values
        else:
            self.key_value_pair_dict[attr] = value

    def getKeyValuePair(self, attr, def_value = None):
        value = self.key_value_pair_dict.get(attr, def_value)
        return value

    def __str__(self):
        key_value_pair_list = []
        for key in self.key_value_pair_dict:
            key_value_pair_list.append("    %s=%s"%(key, self.key_value_pair_dict[key]))
        return "\n".join(key_value_pair_list)
