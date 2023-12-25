""" ********** DevTool ***************
******** for HushHub Frontend ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 25-12-2023

a docker wrapper tool for local development env.
"""


from subprocess import Popen, PIPE, STDOUT
import typer

local_compose_file      = "docker-compose-dev.yml"
local_container_name    = "dev-app"

app = typer.Typer()

def run_command(job, command):
    """ runs command and ret err code """
    print(f"Executing command: {command}")
    command_response = Popen(f"({command})", stderr=PIPE, stdout=PIPE, shell=True, executable="/bin/bash")
    output, errors = command_response.communicate()

    print(output.decode("utf-8"))
    if command_response.returncode != 0:
        print(f"{job} went wrong!")
        print(errors.decode("utf-8"))
    # if command_response.returncode == 0:
    #     print(f"{job} success")

    return output, command_response.returncode

def run_with_stream(command):
    print(f"Executing command: {command}")
    with Popen(f"({command})", stdout=PIPE, stderr=STDOUT, shell=True, executable="/bin/bash") as process:
        for line in process.stdout:
            print(line.decode('utf8'))

@app.command()
def run(compose_file: str = local_compose_file, detach: bool = False):
    """ run the application. """
    print(f"Runing app")
    if detach:
        command = f"docker compose -f {compose_file} up --build -d"
    else:
        command = f"docker compose -f {compose_file} up --build"
        run_with_stream(command)
        return
    _, err = run_command(job=f"Running app", command=command)
    if err != 0:
        print("error, notify devops team")

@app.command()
def stop(compose_file: str = local_compose_file):
    """ stop the running application. """
    print(f"stopping app")
    command = f"docker compose -f {compose_file} down"

    _, err = run_command(job=f"Stopping local env", command=command)
    if err != 0:
        print("error, notify devops team")

@app.command()
def get_logs(app_name: str = local_container_name):
    """ get application logs."""
    command = f"docker logs $(docker ps -a -q --filter ancestor={app_name})"
    _, err = run_command(job=f"Getting logs for {app_name}", command=command)
    if err != 0:
        print("error, notify devops team")

@app.command()
def get_errors(app_name: str = local_container_name):
    """ get application errors."""
    command = f"docker logs $(docker ps -a -q --filter ancestor={app_name}) | grep error"
    _, err = run_command(job=f"Getting logs for {app_name}", command=command)
    if err != 0:
        print("Probably no error found, if you are sure otherwise - notify devops team")

@app.command()
def list_images():
    """ get list of images. """
    command = f"docker images"
    _, err = run_command(job=f"getting images", command=command)
    if err != 0:
        print("error, notify devops team")

@app.command()
def ls():
    """ get list of things in current directory, use it to see if you are where you should be. """
    command = f"ls -asl"
    _, err = run_command(job=f"getting things", command=command)
    if err != 0:
        print("error, notify devops team")

if __name__ == "__main__":
    print("Thanks for using the tool, let us know if you face any bugs.")
    app()