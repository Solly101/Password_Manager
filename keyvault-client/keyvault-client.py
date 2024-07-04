from dotenv import load_dotenv
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
from azure.core.exceptions import AzureError
import hashlib
import getpass

def main():
    global cog_endpoint
    global cog_key

    try:
        # Get Configuration Settings
        load_dotenv()
        
        key_vault_name = os.getenv('KEY_VAULT')
        app_tenant = os.getenv('TENANT_ID')
        app_id = os.getenv('APP_ID')
        app_password = os.getenv('APP_PASSWORD')

        # Get Azure AI services key from keyvault using the service principal credentials
        key_vault_uri = f"https://{key_vault_name}.vault.azure.net/"
        credential = ClientSecretCredential(app_tenant, app_id, app_password)
        keyvault_client = SecretClient(key_vault_uri, credential)
        
        # Get user input (until they enter "quit")
        userName =''
        userPassword=''
        while userName.lower() != 'quit' or userPassword.lower() != 'quit':
            userName = input('\nEnter username or website name ("quit" to stop)\n')
            if userName.lower() == 'quit':
                break
            userPassword = getpass.getpass('Enter your password (Password will be masked as you type) \n')
            if userName.lower() != 'quit' or userPassword.lower() != 'quit':
                hashedPassword = hash_password(userPassword)
                try:
                    keyvault_client.set_secret(userName, hashedPassword)
                    print(f"Successfully stored hashed password for user {userName} in Key Vault.")
                except AzureError as e:
                    print(f"An error occurred while storing the secret: {str(e)}")
         
                except Exception as e:
                    print(f"An unexpected error occurred: {str(e)}")

                

    except Exception as ex:
        print(ex)



def hash_password(password):
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')
    
    # Create a SHA256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the password bytes
    hash_object.update(password_bytes)
    
    # Get the hexadecimal representation of the hash
    hashed_password = hash_object.hexdigest()
    
    return hashed_password
  


if __name__ == "__main__":
    main()