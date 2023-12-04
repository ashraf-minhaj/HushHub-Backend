""" ********** DevTool ***************
******** for HushHub Frontend ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 02-12-2023

a docker wrapper tool for local development env.
"""

import sys
from subprocess import Popen, PIPE, STDOUT

# commands = {
#     "build_image" : "cd ../app; sudo docker build -t hushfront:1"
# }

local_docker_file = "Dockerfile.dev"

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

def run_container(image_tag, to_detach=True):
    print(f"Runing app Container {image_tag}")
    if to_detach:
        command = f"cd ../app; docker run --rm -v .:/app -d -p 80:3000 --env-file .env {image_tag}"
    else:
        command = f"cd ../app; docker run --rm -v .:/app -it -p 80:3000 --env-file .env {image_tag}"
        run_with_stream(command)
        return
    out, err = run_command(job=f"Running {image_tag}", command=command)
    if err != 0:
        print("error, notify devops team")

def stop(image_tag):
    """ stop a specific container. """
    print(f"stopping {image_tag}")
    if image_tag != "all":
        command = f"docker stop $(docker ps -a -q --filter ancestor={image_tag})"
    elif image_tag == "all":
        command = "docker stop $(docker ps -a -q)"
    else:
        print("please pass 'image_tag' or 'all' to stop all containers.")
    # command = f"""docker rm $(docker stop $(docker ps -a -q --filter ancestor={image_tag} --format="{{.ID}}"""
    _, err = run_command(job=f"Stopping {image_tag}", command=command)
    if err != 0:
        print("error, notify devops team")

def get_logs(image_tag):
    command = f"docker logs $(docker ps -a -q --filter ancestor={image_tag})"
    _, err = run_command(job=f"Getting logs for {image_tag}", command=command)
    if err != 0:
        print("error, notify devops team")

def get_list_of_images():
    command = f"docker images"
    # command = f"cd ../app; ls"
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
                    build           image_tag 
                    list_images 
                    run             image_tag 
                    stop            image_tag or all
                    logs            image_tag
                    errors          image_tag
                    
                  """)
        if arg == "build":
            # print(type(sys.argv[2]))
            build_image(sys.argv[2])
        elif arg == "run":
            # print(type(sys.argv[2]))
            run_container(image_tag=f"{sys.argv[2]}", to_detach=False)
        # elif arg == "stop_all":
        #     stop_all()
        elif arg == "stop":
            stop(sys.argv[2])
        elif arg == "list_images":
            get_list_of_images()
        elif arg == "logs":
            get_logs(sys.argv[2])
        elif arg == "errors":
            pass
        else:
            print("Please pass a valid command, type 'sudo python3 devtool.py help'")
        # get_list_of_images()
    except Exception as e:
        print("error! report to your devops team")
        print(e)
