# Databricks notebook source
# Define the variables used for creating connection strings
adlsAccountName = "group3adlsstorage"
adlsContainerName = "training"
adlsFolderName = ""
mountPoint = "/mnt/tmpadls"

# Application (Client) ID
applicationId = dbutils.secrets.get(scope="Group3Scope",key="ClientID")

# Application (Client) Secret Key
authenticationKey = dbutils.secrets.get(scope="Group3Scope",key="ClientSecret")

# Directory (Tenant) ID
tenandId = dbutils.secrets.get(scope="Group3Scope",key="TenantID")

endpoint = "https://login.microsoftonline.com/" + tenandId + "/oauth2/token"
source = "abfss://" + adlsContainerName + "@" + adlsAccountName + ".dfs.core.windows.net/"

# Connecting using Service Principal secrets and OAuth
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": applicationId,
           "fs.azure.account.oauth2.client.secret": authenticationKey,
           "fs.azure.account.oauth2.client.endpoint": endpoint}

# Mounting ADLS Storage to DBFS
# Mount only if the directory is not already mounted
if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
  dbutils.fs.mount(
    source = source,
    mount_point = mountPoint,
    extra_configs = configs)
