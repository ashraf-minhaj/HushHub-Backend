## for github actions 

1. generate ssh key `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
2. directory `gha`
3. Adding the Public Key to authorized_keys `cat gha.pub >> ~/.ssh/authorized_keys`
4. Adding the private key to your repository’s secrets `cat ~/.ssh/gha`
 
## 🚀🚀 setup ansible and ssh 🚀🚀

- step1: install on *Controller* `pip3 install ansible`
- step2: add *Controller*'s public ssh key to *Node*'s `authorized_keys` 
  - on *Controller* `cat .ssh/id_rsa.pub`, copy it
  - on *Node* `sudo nano .ssh/authorized_keys`, paste the public key
  - on *Node*, change authorized_keys permission `chmod 600 authorized_keys`
  - on *Node*, .ssh dir should have 700, `chmod 700 ~/.ssh`
- test on *Controller* `ssh hostUserName@yourIp`

### With Ansible 
- test: `ansible -i inventory.yml all -m ping`

- run playbook: `ansible-playbook -i inventory.yml docker_setup.yml`


### more
- get os `cat /etc/*-release`