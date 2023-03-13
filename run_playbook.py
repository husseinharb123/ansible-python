import ansible_runner
from flask import Flask



# pip install ansible_runner 
# pip install flask 

app = Flask(__name__)

@app.route('/runplaybook')
def run_playbook():
    
    playbook_path = 'playbook.yaml'
    # inventory_path = './inventory'
    # roles_path = '/path/to/roles'
    ansible_config_file = 'ansible.cfg'

    respond = ansible_runner.run(
        playbook=playbook_path,
        # inventory=inventory_path, # specify the path of inventory
        # extravars={'ansible_roles_path': roles_path}, # specify the path of roles folder
        quiet=False, # show the tasks steps
        private_data_dir='.',
        envvars={'ANSIBLE_CONFIG': ansible_config_file}
    )

    print(f"Playbook execution status: {respond.status}")
    return "okes"

if __name__ == '__main__':
    app.run(debug=True)