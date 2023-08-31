import requests
import yaml

# APIキー等をyamlから取得する
class AzureInfo:
    def __init__(self) -> None:
        with open('azure-info.yaml', 'r') as f:
            data = yaml.safe_load(f)
            self.account_id = data['accountId']
            self.subscription_key = data['subscriptionKey']
            self.location = data['location']
            self.video_id = data['videoId']

ai = AzureInfo()

url = f'https://api.videoindexer.ai/{ai.location}/Accounts/{ai.account_id}/Videos/{ai.video_id}/Index'

headers = {
    # Request headers
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': ai.subscription_key,
}

result = requests.get(url, headers=headers)

print(result.json())