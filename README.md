<div align="center">

# Hush Hub Backend
*Share thoughts wihtout letting them know who you are*
![banner](docs/banner.png)

![](https://img.shields.io/badge/License-MIT%20License-red?style=plastic&logo=mit)&nbsp;
<!-- ![](https://img.shields.io/badge/Platform-Linux-black?labelColor=black&style=plastic&logo=linux)&nbsp; -->
![](https://img.shields.io/badge/Python-3.10-blue?style=plastic&logo=python)&nbsp;
![](https://img.shields.io/badge/docker--blue?style=plastic&logo=docker)&nbsp;
![](https://img.shields.io/badge/Docker%20Compose-3.8-blue?style=plastic&logo=docker)&nbsp;
</div>

see [demo snap](#demo)
see [HushHub Frontend](https://github.com/ashraf-minhaj/HushHub-Frontend/)

### Features
- [x] Dockerize Application 
- [x] Docker Hot reloading for local development 
- [x] Multistage build 
- [x] Separate credentials for local dev and production (.env)
- [x] Local docker image 
- [x] Pull/push from the docker hub 
- [x] Log formatting (Configure logging in application) 
- [x] Seeding data for the application 
- [x] Docker tool to wrap complex docker commands in a simpler format 

### Improvement scopes (future considerations)
- application health check monitoring and notification system
- test scripts to catch bugs at early stage
- CI/CD
(more to come)

### Demo
![demo](docs/demo.png)

### setup local development envionment 
- Install latest version of docker in your system
- Install python3 on your system (should come with your distro BTW)

- go to the `tools` dir and run tool - 
  You just need to remember the `image_tag`, the tool handles the rest.
    ```
        $ sudo python3 devtool.py <arg> <value>
    ```

- list of args -
    ``` 
        arg          -   value
        help       
        list_images 
        run              detach/null
        stop             
        logs            
        errors          
    ```

  Do not run in detachable mode if you want to see live logs of the app.

### Environment variable file
The file should be named as `.env`, devs will get the dev env from the lead. no env specific things should reside on the repository.

### Build and Push image to dockerhub

    ```
    cd scripts/
    bash build_n_push.sh <version-tag>
    ```

### Refactoring
- If gitignore is not taking changes, reason is Git's cache hasn't been refreshed to reflect the changes in Gitignore.

    ```bash
    git rm -r --cached
    git add . .
    ```

- if you are a mac OSX user and facing permission issue please change setting on your docker-desktop application - 

    ```
    In Preferences > General there is an option "Use gRPC FUSE for file sharing" which is by default checked. Uncheck that option Apply and restart.
    ```

> ashraf minhaj