class Service:

    def getCmd(sudo_password, params):
        name = Service.getName(params)
        state = Service.getState(params)

        if state is False:
            return False
        
        cmd = 'echo "{}" | sudo -S systemctl {} {} '.format(sudo_password, state, name)
        return cmd

    def getName(params):
        return params['name']
    
    def getState(params):
        state = params['state']

        if state == "started":
            return "start"
        elif state == "restarted":
            return "restart"
        elif state == "stopped":
            return "stop"
        elif state == "enabled":
            return "enable"
        elif state == "disabled":
            return "disabled"
        else:
            return False

    def state(host, params, debug=False, dryRun=False):
        
        sudo_password = host.ssh_password
        cmd = Service.getCmd(sudo_password,  params)

        if cmd is False:

            if debug:
                print("state incorect")

            return False

        client = host.client

        if dryRun:
            print(cmd)
            return
        
        stdin, stdout, stderr = client.exec_command(cmd)

        update_output = stdout.read().decode()
        update_error = stderr.read().decode()

        if debug:
            print(update_output)
            if update_error:
                print(update_error)