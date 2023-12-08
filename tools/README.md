## ### setup local development envionment 

- Install latest version of docker in your system
- Install python3 on your system (should come with your distro BTW)

- run tool - 
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