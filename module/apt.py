class Apt:

    def getPackage(todo):
        return todo['params']['name'] 

    def install(host, todo, debug=False, dryRun=False):
        package = Apt.getPackage(todo)

        client = host.client
        sudo_password = host.ssh_password

        update_command = 'echo "{}" | sudo -S apt update'.format(sudo_password)

        install_command = 'echo "{}" | sudo -S apt install -y {}'.format(sudo_password, package)

        if dryRun:
            print(update_command)
            print(install_command)
            return

        stdin, stdout, stderr = client.exec_command(update_command)

        update_output = stdout.read().decode()
        update_error = stderr.read().decode()

        if debug:
            print(update_output)
            if update_error:
                print(update_error)

        stdin, stdout, stderr = client.exec_command(install_command)

        install_output = stdout.read().decode()
        install_error = stderr.read().decode()

        if debug:
            print(install_output)
            if install_error:
                print(install_error)



    def delete(host, todo, debug = False, dryRun = False):
        package_name = Apt.getPackage(todo)

        client = host.client
        sudo_password = host.ssh_password

        command_remove = 'echo "{}" | sudo -S apt remove -y {}'.format(sudo_password, package_name)
        command_purge = 'echo "{}" | sudo -S apt purge -y {}'.format(sudo_password, package_name)

        if dryRun:
            print(command_remove)
            print(command_purge)
            return

        stdin, stdout, stderr = client.exec_command(command_remove)
        output_remove = stdout.read().decode()
        error_remove = stderr.read().decode()

        if debug:
            print(output_remove)

            if error_remove:
                print(error_remove)

        stdin, stdout, stderr = client.exec_command(command_purge)
        output_purge = stdout.read().decode()
        error_purge = stderr.read().decode()

        if debug:
            print(output_purge)

            if error_purge:
                print(error_purge)
