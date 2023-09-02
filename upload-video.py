import requests
import yaml

# APIキー等をyamlから取得する
class AzureInfo:
    def __init__(self) -> None:
        with open('azure-info.yaml', 'r') as f:
            data = yaml.safe_load(f)
            self.account_id = data['accountId']
            self.subscription_key = data['subscriptionKey']
            self.access_token = data['accessToken']
            self.location = data['location']
            self.video_url = data['videoUrl']
            self.video_name = data['videoName']

ai = AzureInfo()

url = f'https://api.videoindexer.ai/{ai.location}/Accounts/{ai.account_id}/Videos?name={ai.video_name}&videoUrl={ai.video_url}'

headers = {
    # Request headers
    'Cache-Control': 'no-cache',
    'Authorization': f'Bearer {ai.access_token}',
    'Ocp-Apim-Subscription-Key': ai.subscription_key,
}

# URL先のムービーをアップロード
result = requests.post(url, headers=headers)

print(result.json())

# result['id']をyamlに書き込む
with open('azure-info.yaml', 'r') as f:
    data = yaml.safe_load(f)
    data['videoId'] = result.json()['id']
