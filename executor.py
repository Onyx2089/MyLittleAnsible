import time
import logging

from module.apt import Apt
from module.cmd import Cmd
from module.service import Service
from module.copy import Copy

class Executor:

    # def getLogger(FORMAT, msg, params): 
    #     logging.basicConfig(format=FORMAT)

    #     logger = logging.getLogger('tcpserver')
    #     logger.setLevel(logging.DEBUG)

    #     logger_adapter = logging.LoggerAdapter(logger, params)
    #     logger_adapter.info(msg)

    def aptModule(todo, host, debug, dry_run):
        params = todo['params']

        if "name" not in params or "state" not in params:
            return False

        state = params['state']

        if state == "present":
            Apt.install(host, todo, debug, dry_run)
        elif state == "absent":
            Apt.delete(host, todo, debug, dry_run)

# 2022-01-06 21:49:16,432 - root - INFO - [1] host=192.168.1.22 op=apt name=nginx-common state=present

        return False

    def cmdModule(todo, host, debug, dry_run):
        params = todo['params']

        if "command" not in params:
            return False

        cmd = params["command"]

        Cmd.shell(cmd, host, debug, dry_run)



    def serviceModule(todo, host, debug, dry_run):
        params = todo['params']

        if "name" not in params or "state" not in params:
            return False
        
        Service.state(host, params, debug, dry_run)

    def serviceCopy(todo, host, debug, dry_run):
        params = todo['params']

        if "src" not in params or "dest" not in params:
            return False
        
        Copy.copy(host, todo, debug, dry_run)