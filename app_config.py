import os
from azure.identity import DefaultAzureCredential
from azure.appconfiguration import AzureAppConfigurationClient


def get_app_config_values():
    # Initialize Azure App Configuration client
    print('in app config values')
    credential = DefaultAzureCredential()

    #app_config_connection_string = "Endpoint=https://coe-appconfig.azconfig.io;Id=8UUe;Secret=4sGOzqNOKZU3XUxsIOn6KQbrBH8LGsuQUyCSD6GslRL3Atf2J3PHJQQJ99AHACYeBjF7yJoqAAACAZACowuK"
    #app_config_client = AzureAppConfigurationClient.from_connection_string(app_config_connection_string)

    app_config_client = AzureAppConfigurationClient.from_connection_string(os.getenv("APP_CONFIG_CONNECTION_STRING"))
    print(f'app_config_client: {app_config_client}')

    # Fetch the Event Hub name from App Configuration
    config_setting_event_hub_name = app_config_client.get_configuration_setting(key="EventHubName_FOREX_EVENTHUB_TRIGGER")
    event_hub_name = config_setting_event_hub_name.value

    # Fetch the RootManageSharedAccessKey connection string from App Configuration
    config_setting_sas_key = app_config_client.get_configuration_setting(key="EventHubRootManageSharedAccessKey_FOREX_EVENTHUB_TRIGGER")
    event_hub_root_manage_shared_access_key = config_setting_sas_key.value

    print(f'event_hub_name: {event_hub_name}, event_hub_root_manage_shared_access_key: {event_hub_root_manage_shared_access_key}')

    return event_hub_name, event_hub_root_manage_shared_access_key

print(get_app_config_values())