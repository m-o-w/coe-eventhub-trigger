import os
import logging
import uuid
from azure.appconfiguration import AzureAppConfigurationClient

request_id = str(uuid.uuid4())
interface_id = "INTSVC114_MOCKAPI"
log_prefix = f"{interface_id} [{request_id}]"

class AppConfigManager:
    def __init__(self):
        self.connection_string = os.getenv('AZURE_APP_CONFIG_CONNECTION_STRING')
        if not self.connection_string:
            raise ValueError(f'{log_prefix}: Azure App Configuration connection string is not set in environment variables.')
        self.client = AzureAppConfigurationClient.from_connection_string(self.connection_string)

    def get_configuration_value(self, key):
        try:
            config_setting = self.client.get_configuration_setting(key=key)
            logging.info(f'{log_prefix}: Retrieved configuration value for key {key}')
            return config_setting.value
        except Exception as e:
            logging.error(f'{log_prefix}: Error retrieving configuration value for key {key}: {e}')
            return None