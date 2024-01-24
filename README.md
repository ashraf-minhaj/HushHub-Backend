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

### Application Features
- [x] Dockerize Application 
- [x] Docker Hot reloading for local development 
- [x] Multistage build 
- [x] Separate credentials for local dev and production (.env)
- [x] Local docker image 
- [x] Pull/push from the docker hub 
- [x] Log formatting (Configure logging in application) 
- [x] Seeding data for the application 
- [x] Docker tool to wrap complex docker commands in a simpler format

### CI/CD Features
- **On PR**:
    - [x] Linter
    - [x] Unit Test
    - [x] CodeQL
    - [x] SonarQube, With results in PR annotations (integrated with SonarCloud)

- **On Push to feature branch**:
    - [x] Unit Test
    - [x] Build Image
    - [ ] Deploy to dev env from feature branch 
        - [ ] run workflow by `commit-msg`
        - [ ] run workflow by `pr-comment`

- [ ] Cl fail email notification with details
- [ ] Implement CD from `main` branch to both the envs (dev, prod)
- [ ] Implement a simple rollback job that we use the last successful image to do the deployment 
- [ ] Calculate disaster recovery time of the CI/CD
- [ ] Notify on failed deployments with details in the email

- [ ] Setup Production and Dev Environment servers
- [ ] Scope of improvements
- [ ] Bonus: Implement Integration Test on post deployment on real environment


### Improvement scopes (future considerations)
- application health check monitoring and notification system
(more to come)

### Demo
![demo](docs/demo.png)

## setup local environment 

- Install latest version of docker in your system
- Install python3 on your system (should come with your distro BTW)

- Setup devtool. Go to 'tools' dir and run -
    ```
        $ pip3 install .
    ```

- Now run the tool from your 'app' directory. 
     ```
        $ devtool run --app-name devbackend
    ```

- example `devtool --help` -
    ``` 
        Usage: devtool [OPTIONS] COMMAND [ARGS]...

        Options:
        --install-completion [bash|zsh|fish|powershell|pwsh]
                                        Install completion for the specified shell.
        --show-completion [bash|zsh|fish|powershell|pwsh]
                                        Show completion for the specified shell, to
                                        copy it or customize the installation.
        --help                          Show this message and exit.

        Commands:
        get-errors   get application errors.
        get-logs     get application logs.
        list-images  get list of images.
        ls           get list of things in current directory, use it to see if...
        run          run the application.
        stop         stop the running application.
    ```

  Do not run in detachable mode if you want to see live logs of the app.

### Environment variable file
The file should be named as `.env`, devs will get the dev env from the lead. no env specific things should reside on the repository.

  ```
    ENV=dev
    PORT=8080
    DB_URL=mongodb://mongodb:27017 # for docker service
    # DB_URL=mongodb://localhost:27017
    # f"mongodb://{username}:{password}@host:port/"
  ```

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