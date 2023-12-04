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
        build           image_tag 
        list_images 
        run             image_tag 
        stop            image_tag or all
        logs            image_tag
        errors          image_tag
    ```