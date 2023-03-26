### Django coworkers hierarchy

To run the project, follow the next steps:

1. Create the `${HOME}/django_database` for MySQL container to store its data:
        
        mkdir ${HOME}/django_database

2. To quickly start the employee database container, the number of employees is set to 200.
   in order to change the number of employees, enter the following into the terminal command:
   
        `export EMPLOYEES_NUM=50000`

3. When running for the first time, run `docker-compose` from the root of the project with following command:

        docker-compose up -d --build
   And check if everything started properly:

        docker ps

You won't need that `--build` flag.

After that you can access working Django container under [localhost:8081](http://localhost:8081)
