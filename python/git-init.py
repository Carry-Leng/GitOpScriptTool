# -*- coding: UTF-8 -*-

"""
@Authors: Carry·Leng

@Date: 2020-03-01 23:56:07
"""

from Utils import isEmpty

import os


def init(directory = None, git_bare = False, git_shared = False, template = None, shared = None):
    init_cmd = "git init"
    #if git_quiet:
    #    init_cmd = "%s --quiet" % init_cmd
    if git_bare:
        init_cmd = "%s --bare" % init_cmd
    if not isEmpty(template):
        init_cmd = "%s --template=%s" % (init_cmd, template)
    if not isEmpty(shared):
        init_cmd = "%s --shared=%s" % (init_cmd, shared)
    elif git_shared:
        init_cmd = "%s --shared" % init_cmd
    if not isEmpty(directory):
        init_cmd = "%s %s" % (init_cmd, directory)
    print(init_cmd)
    result = os.popen(init_cmd).read().strip()
    print(result)
    for line in result.splitlines():
        if "error" in line or "ERROR" in line:
            raise Exception(result)


if __name__ == "__main__":
    print("git-init start")
    init("Test-Init1")
    init("Test-Init2", True)
    init("Test-Init3", True, True)