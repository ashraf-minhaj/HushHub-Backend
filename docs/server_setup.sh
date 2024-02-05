# doc: https://zellwk.com/blog/github-actions-deploy/
# ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
ssh-keygen -t rsa -b 4096 -C "minhaj@dev.com"
# upon asking add dir: 
gha
# add the pub key to authorized keys
cat gha.pub >> ~/.ssh/authorized_keys

# copy paste the key in gha
cat gha