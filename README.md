# Configuration-Management-and-automation
<h2>Description</h2>
<br/> This project showcases how to use ansible to automate a webserver enviroment as well as python to backup files to a desired location
<br />
<p align="center">
<img src="https://github.com/user-attachments/assets/c6926a60-f791-4f8d-9b87-ae8f993733a3"/>

<h2>Languages and Utilities Used</h2>

Bash, VSCode, Ansible, Python

<h2>Environments Used </h2>

- <b>CentOS Linux release 8.5.2111
 10</b>

<h2>Project walk-through:</h2>
<p align="center">
Make sure you have 2 vms and designate the control node by running dnf install epel-release ansible -y   : <br/>
<img src="https://github.com/user-attachments/assets/f3741360-8c1b-4bbf-b836-05987406ea32"/>
<br /> 
<br /> generate an ssh key by running ssh-keygen and then ssh-copy-id [other machine ip addr] to make the other host known <br />  
<br />
<br/>   
<img src="https://github.com/user-attachments/assets/a624c522-34d4-4ddf-9cf3-bc42628a9dc4"/>
<br />
<br /> Now add an entry to the /etc/ansible/hosts file and add the other machines ip address<br/>
 <br/>
<img src="https://github.com/user-attachments/assets/5dd8b48d-d972-46ce-91a4-104463e8f41e"/>
<br />
<br /> Now cd /etc/ansible/playbooks and create a playbook called webserver_env_setup.yml <br/> 
 <br/> 
 <br/> Now add the following entries into the yml playbook. First we will put localhost in hosts so that we can test our playbook <br/>
 <img src="https://github.com/user-attachments/assets/89ff43c1-f32b-4b6d-9e9f-051283b78320"/>
<br/>
 <br/> 
 Now create a template file for the nginx configuration titled nginx.conf.j2
 <br/>
 <img src="https://github.com/user-attachments/assets/3aed03e0-cb9a-4c3b-bf9f-3fa7bbefc313"/>
<br/>
<br/>
<br/> Next run ansible-playbook -i inventory.ini webserver_env_setup.yml and watch to confirm the output from playbook on local machine <br/>
<img src="https://github.com/user-attachments/assets/59e3ca83-0e0f-4366-96f5-ced539932fc1"/>
<img src="https://github.com/user-attachments/assets/fa759689-41ea-4579-8bc6-025c129592c6"/>
<br/>
<br/>
<br/> Go to a browser and search https://serverIP/info.php <br/> 
<br/> <br/> Now if the output of the search appears this way then we must troubleshoot <br/>
<img src="https://github.com/user-attachments/assets/85a3bb82-72bf-40d3-a0ac-7b7fb24eb525"/>
   <br/>
   <br/> Returning to the control node confirm the proper nginx and php packages were installed from the playbook <br/> 
   <br/>
 <img src="https://github.com/user-attachments/assets/5e6b30c4-5be1-4b33-ae64-ba57c250aefb"/>
   <br/>
 <br/> Run systemctl status php-fpm to see if thats the issue <br/>
 <img src="https://github.com/user-attachments/assets/e481d01a-3bbe-48cd-bc62-e44243504423"/> 
<br/> <br/> 
<br/> Let's recheck our configurations in nginx.conf and update the php-fpm configuration by going to /etc/php-fpm.d/www.conf<br/>
<img src="https://github.com/user-attachments/assets/b1a92ae2-51e9-430f-b299-8603d528c1e5"/>
 <img src="https://github.com/user-attachments/assets/29e1e224-4e66-4d12-9289-cc00d593c858"/>
   <br/>
   <br/>
   <br/><br/> Run firewall-cmd --zone=public --add-port=80/tcp --permanent to make sure that http traffic is allowed (here we can see it has been successfully configured from out playbook)<br/> 
 <img src="https://github.com/user-attachments/assets/3190a29b-7037-403d-913a-d34fc0102537"/>
  <br/> Here we can see the http service has not been added so let's add it <br/>
  <img src="https://github.com/user-attachments/assets/b04f3e26-635a-4e84-8ca5-b9cdc2f00110"/>
<br/> Now run systemctl restart nginx and php-fpm service. Webserver still unavailable? Run cat /var/log/nginx/error.log and cat /var/log/php-fpm/error.log <br/>
<img src="https://github.com/user-attachments/assets/d9818778-b475-4ab2-a012-bfe2c93c4545"/>
   <br/> Now it can be seen that SELinux is preventing nginx from connecting to tcp port 9000 (If enabled) <br/>
   <br/> To fix this make the following entry to the yml webserver env playbook and then attempt to access the webserver again <br/> 
 <img src="https://github.com/user-attachments/assets/b492d3d0-ee0f-4473-a170-0dbaa9d9327e" />
 <img src="https://github.com/user-attachments/assets/5c2b5b75-9535-4e0d-ad6a-7bfa73bd2638"/>
   <br/>
   <br/><br/> If the webserver issue persists disable SELinux for testing and check the nginx configuration file <br/> 
<br/>
<img src="https://github.com/user-attachments/assets/06a25df0-76e0-4532-ba8d-dc06baee3a17"/>
   <br/>
   <br/> Here we can double check and see if our playbooks new firewall ports as well as service status have been completed <br/> 
 <img src="https://github.com/user-attachments/assets/3458295a-d063-4a64-888d-ced3788670a3"/>
   <br/>
   <br/>
 <br/> Now edit the yml playbook to include everything mentioned to test on the localhost again prior to configuring a new server <br/> 
<br/>
<img src="https://github.com/user-attachments/assets/dd3089cc-e21e-4555-ac75-00ebdfccf7bc"/>
 <br/> create the revised nginx template <br/>
 <img src="https://github.com/user-attachments/assets/74fb58f6-f820-42ee-a43c-792e3ee77c20"/>
   <br/>
   <br/> Confirm setting, configure hosts if needed, and run the playbook <br/> 
   <br/>
 <br/>Afterwards confirm the services started and enabled at boot, firewall rules, and go to http://ipaddr/info.php to view webpage   <br/>
  <img src="https://github.com/user-attachments/assets/fa711b1e-889b-499b-8108-7d998a979ebf"/>
 <br/><br/>
 <br/> 
<br/>
 <br/> Now with other vm from the control node and confirm the services, firewall, and webpage <br/>
<img src="https://github.com/user-attachments/assets/cae3b2ba-5df0-42e4-9fc0-8c43b0b56810"/>
  <img src="https://github.com/user-attachments/assets/a8471e28-21f9-4af9-8f34-0a109d3bcea9"/>
  <img src="https://github.com/user-attachments/assets/cf1eb8e7-5fc5-43fd-b208-25f381a90849"/>
   <br/> Success! <br/>
   <br/> Uninstall packages and services if necessary to clean up and run playbook again: <br/>
 <img src="https://github.com/user-attachments/assets/240d1349-b252-4052-95e8-fe6049d9ea14"/>
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/><br/> <br/> 
<br/>
<img src=""/>
   <br/>
   <br/> <br/> 
   <br/>
   <br/>
