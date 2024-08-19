from azure.appconfiguration import AzureAppConfigurationClient
import os
import logging

class AppConfigManager:
    def __init__(self):
        self.connection_string = os.getenv('AZURE_APP_CONFIG_CONNECTION_STRING')
        if not self.connection_string:
            raise ValueError("Azure App Configuration connection string is not set in environment variables.")
        self.client = AzureAppConfigurationClient.from_connection_string(self.connection_string)
        self.cached_config = None

    def get_configuration_value(self, key):
        try:
            config_setting = self.client.get_configuration_setting(key=key)
            return config_setting.value
        except Exception as e:
            logging.error(f"Error retrieving configuration value for key {key}: {e}")
            return None

    def get_cached_config(self):
        if self.cached_config is None:
            self.cached_config = {
                "mongo_uri": self.get_configuration_value("MongoUri_FOREX_EVENTHUB_TRIGGER"),
                "database_name": self.get_configuration_value("DatabaseName_FOREX_EVENTHUB_TRIGGER"),
                "collection_name": self.get_configuration_value("CollectionName_FOREX_EVENTHUB_TRIGGER")
            }
        return self.cached_config

# Usage example
if __name__ == "__main__":
    try:
        app_config_manager = AppConfigManager()
        config = app_config_manager.get_cached_config()
        print(config)
    except ValueError as e:
        print(e)