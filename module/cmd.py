class Cmd:

    def shell(cmd, host, debug, dryRun):
        client = host.client
        sudo_password = host.ssh_password

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