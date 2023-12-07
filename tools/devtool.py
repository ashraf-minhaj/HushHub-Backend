""" ********** DevTool ***************
******** for HushHub Frontend ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 07-12-2023

a docker wrapper tool for local development env.
"""

import sys
from subprocess import Popen, PIPE, STDOUT


local_compose_file = "docker-compose-dev.yml"

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

def build_image(image_tag):
    """ build docker image by given command. """
    command = f"cd ../app; docker build -t {image_tag} -f {local_docker_file} ."
    # command = f"cd ../app; ls"
    # _, err = run_command(job=f"building {image_tag}", command=command)
    # if err != 0:
    #     print("error, notify devops team")
    run_with_stream(command)

def run_app(to_detach=True):
    print(f"Runing app")
    if to_detach:
        command = f"cd ../app; docker compose -f {local_compose_file} up --build -d"
    else:
        command = f"cd ../app; docker compose -f {local_compose_file} up --build"
        run_with_stream(command)
        return
    out, err = run_command(job=f"Running app", command=command)
    if err != 0:
        print("error, notify devops team")

def stop():
    """ stop compose. """
    print(f"stopping app")
    command = f"cd ../app; docker compose -f {local_compose_file} down"

    _, err = run_command(job=f"Stopping local env", command=command)
    if err != 0:
        print("error, notify devops team")

def get_logs(image_tag):
    """ get backend application logs."""
    command = f"docker logs $(docker ps -a -q --filter ancestor={image_tag})"
    _, err = run_command(job=f"Getting logs for {image_tag}", command=command)
    if err != 0:
        print("error, notify devops team")

def get_errors(image_tag):
    """ get backend application logs."""
    command = f"docker logs $(docker ps -a -q --filter ancestor={image_tag}) | grep error"
    _, err = run_command(job=f"Getting logs for {image_tag}", command=command)
    if err != 0:
        print("Probably no error found, if you are sure otherwise - notify devops team")

def get_list_of_images():
    command = f"docker images"
    _, err = run_command(job=f"getting images", command=command)
    if err != 0:
        print("error, notify devops team")

if __name__ == "__main__":
    print("Thanks for using the tool, let us know if you face any bugs.")
    try:
        # get user command
        arg = sys.argv[1]

        if arg == "help":
            print("""
                  dev tool to enhance developer experience.

                  run tool - 
                  $ sudo python3 devtool.py <arg> <value>
                  list of args -
                    arg          -   value
                    help       
                    list_images 
                    run              detach/null
                    stop             or all
                    logs            
                    errors          image_tag (in future)
                    
                  """)
        elif arg == "run":
            detach = False
            if sys.argv[2] == "detach":
                detach = True
            run_app(to_detach=detach)
        elif arg == "stop":
            stop()
        elif arg == "list_images":
            get_list_of_images()
        elif arg == "logs":
            image_tag = "app-backend"
            get_logs(image_tag)
        elif arg == "errors":
            image_tag = "app-backend"
            get_errors(image_tag)
        else:
            print("Please pass a valid command, type 'sudo python3 devtool.py help'")
        # get_list_of_images()
    except Exception as e:
        print("error! report to your devops team")
        print(e)
