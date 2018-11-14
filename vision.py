import requests

import settings

KEY1 = settings.KEY1

# locationを東日本で登録した場合のendpoint
endpoint = 'https://japaneast.api.cognitive.microsoft.com/vision/v1.0/ocr'

def get_text_by_ms(image_url=None, image=None):
    if image_url is None and image is None:
        return '必要な情報が足りません'

    params = {'visualFeatures': 'Categories,Description,Color'}

    if image_url:
        headers = {
            'Ocp-Apim-Subscription-Key': KEY1,
            'Content-Type': 'application/json',
        }
        data = {'url': image_url}
        response = requests.post(
            endpoint,
            headers=headers,
            params=params,
            json=data
        )

    elif image is not None:
        headers = {
            'Ocp-Apim-Subscription-Key': KEY1,
            "Content-Type": "application/octet-stream"
        }
        response = requests.post(
            endpoint,
            headers=headers,
            params=params,
            data=image,
        )

    status = response.status_code
    data = response.json()

    if status != 200:

        if data['code'] == 'InvalidImageSize':
            text = '画像のサイズが大きすぎます'

        elif data['code'] == 'InvalidImageUrl':
            text = 'この画像URLからは取得できません'

        elif data['code'] == 'InvalidImageFormat':
            text = '対応していない画像形式です'

        else:
            text = 'エラーが発生しました'

        print(status, data)
        return text

    text = ''
    for region in data['regions']:
        for line in region['lines']:
            for word in line['words']:
                text += word.get('text', '')
                if data['language'] != 'ja':
                    text += ' '
        text += '\n'

    if len(text) == 0:
        text += '文字が検出できませんでした'

    print('text:', text)
    return text


if __name__ == "__main__":
    get_text_by_ms(image_url)
