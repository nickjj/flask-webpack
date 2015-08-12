def test_index_page(client):
    """ Expect to see the md5 tagged assets in the source code. """
    response = client.get('/')
    assert response.status_code == 200

    asset_path = 'https://yourdomainname_or_asset_cdn.com/assets/'
    css = 'app_css.d5cbf1ea13fccdf706e2.css'
    js = 'app_js.8b7c0de88caa3f366b53.js'
    image = 'images/dog/no-idea.b9252d5fd8f39ce3523d303144338d7b.jpg'

    response_data = response.data.decode('utf-8')
    assert asset_path in response_data
    assert css in response_data
    assert js in response_data
    assert image in response_data
