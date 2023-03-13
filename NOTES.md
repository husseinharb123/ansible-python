# Ansible 

## - generate key : ` ssh-keygen -t ed25519`
##  - copy the key : `ssh-copy-id -i .ssh/id_ed25519.pub  ip_adresss`
## - pass by passphrase :  ssh-agent to store your passphrase in a secure manner.

Here are the steps to set up ssh-agent to cache your passphrase:

1. eval "$(ssh-agent -s)" This command will start the SSH agent and display the agent's process ID.
2. Add your SSH private key to the agent by running the following command: ssh-add /path/to/your/private/key
When you run this command, you will be prompted to enter your passphrase.enter your passphrase and press Enter.
Once you have added your private key, the SSH agent will cache your passphrase for the current session.
3. To cache your passphrase permanently, you can add the following line to your shell startup file (such as ~/.bashrc or ~/.zshrc):
eval "$(ssh-agent -s)"
ssh-add /path/to/your/private/key
This will start the SSH agent and add your private key to the agent's cache every time you start a new shell session.


- This command shows you the disk space usage on your system : `df -h` 
- this command check of page found : apt search nameofpackage
- check os version : `/etc/os-release`
- Identify the process that is holding the lock of packge manager  : `sudo lsof /var/lib/dpkg/lock-frontend `
- check process : `ps aux | grep 2108`
- sudo kill -9 2108 force kill process

- avoid each time enter passord when using sudo 
    1. sudo visudo 
    2. add this `username ALL=(All) NOPASSWD: All `
    3. or create a file in etc/sudoers.d and add in the file the above script

- check the connection within the invertory are working 
    ```
    ansible all --key-file /path/private -i /path/invertory -m ping
    ```
- show all hosts in a inventory
  ```
  ansible all --list-hosts
  ```
- get info about hosts : used for trouble shooting

    ```
    ansible all -m gather_facts --limit <ip address>
    ```

- alternative for sudo apt update in ansible :

    ```
    ansible all -m apt -a update_cache=true --become --ask-become-pass
    ```
- install a specfic package :
    ```
    ansible all -m apt -a name=vim-nox --become --ask-become-pass

    ```
- you can add -vvv for commands after all to see logs 

- update a specfic package :
    ```
    ansible all -m apt -a "name=vim-nox state=latest" --become --ask-become-pass
    ```
- install all the updates  :
    ```
    ansible all -m apt -a "upgrade=dist" --become --ask-become-pass
    
    ```
- run  a playbook:
  ```
    ansible-playbook  --ask-become-pass  playbook.yml
  ```
- list all tags within a playbook :

    ```
    ansible-playbook --list-tags playbook.yaml
    ```
- run plays with specfic tag   :

    ```
    ansible-playbook --tags tagname  --ask-become-pass  playbook.yaml
    ```
- run plays with mutilpe  tag   :

    ```
    ansible-playbook --tags "tagname1,tagname2"  --ask-become-pass  playbook.yaml
    ```

- if you want to run the ansible-playbook with --ask-become-book
    1. make sure you specfiy the remote user in ansible.cfg
    2. make sure you configured sudors to avoid password when using sudo in remote
    
- `If change_when is set to false in an Ansible playbook task`, Ansible will never consider that task as having made changes, even if changes were actually made during the execution of the task.


- how to use roles 
  1. create roles folder
  2. with roles folder create folders with same name as rolename 
  3. mininum requriement is roles/rolename/tasks/main.yml
  4. inside yml add the task you want to run 


- how to use host variables 
  1. create host_vars directory 
  2. create file /host_vars/<ipaddress>.yml 
  3. inside the file add the varibles :
   ```
   varaiblename: value 
   ```
- how to use handlers :
  1. add to task you want react after a changed in it `notify: anyname`
  2. create new file in this path  roles/rolename/handlers/main.yml
  3. inside main.yml add this
   ```
   - name: nameofnotify
     serivce:
        name : nameofserive
        state : restarted 
   ```
- how to handle templtes :
    1. create a jinja file with extentions .j2
    2. path of file roles/rolesname/templates/file.j2
    3. add varaibles {{  var_name   }} in side thr file.j2 
    4.  var_name can be found in host_vars foldes
    5.  use this module to use it :
     ```
    -   name: openssh | generate sshd_config file from template
        tags: ssh
        template:
            src: "Template:Ssh template file"
            dest: /etc/ssh/sshd_config
            owner: root
            group: root
            mode: 0644
    ```