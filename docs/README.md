connect with server

1. generate ssh key
ssh-keygen -t rsa -b 4096 -C "min@haj.com"

enter passphrase: 12345 

2. copy the public key 
cat ~/.ssh/id_rsa.pub

3. Navigate to "deploy keys" in your GitHub repository settings (Settings > Deploy keys);

4. 
