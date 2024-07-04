# Password_Manager
Python script that stores hashed passwords in Azure key vault.

### Features
- This python script connects to Azure key vault using the application credentials to create a service principal to access Azure key vault. 
-Then it prompts the user to add a username and password. 
-The script then hashes the password and store the username and password as a key vault secret. 

### How to get Started?

1. Clone the GitHub repository

```bash
git clone https://github.com/Solly101/Password_Manager.git
```
2. Install the required dependencies:

```bash
pip install azure-keyvault-secrets azure-identity
```
3 Configure your App (client) Id under App registration in your Azure portal.

4. Connect the app (client) in your key vault under Access control. Make sure to give the app a Key Vault Secrets Officer role so that it has write rights.

5. In the .env file. Change the values to you key vault and app (client) credentials.

6. Once you have successfully created the app registration and connected it the key vault in 
Azure, and having copied the credentials to the .env file. You can run the python script. 

7. If a successful message is return, you may proceed to the Azure portal to check of the secret in the Azure key vault. 


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
