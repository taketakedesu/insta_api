import requests
import json
import datetime
from pprint import pprint

# Instagram Graph APIの認証用関数を作成
def basic_info():
    # 初期
    config = dict()
    # 【要修正】アクセストークン
    config["access_token"]         = 'EAAIWrzRNhqMBAGFYZCbPwGd279ZA51ZBOBKyI2kDCMrmGEZBdSApHjsR008ia1hzNdGgtMk4WiBMjYpMrYE54HAurZBwIYcPpOYmHVVhxKQz4HCcRhB2pEZAdIOM0TpZB5DbHFLCcTvZApJVnZCZC43XA4g0EOyZB1SrGtKA8wDA5ACn0qhukRLaSMd'
    # 【要修正】アプリID
    config["app_id"]               = '587891706005155'
    # 【要修正】アプリシークレット
    config["app_secret"]           = 'af9f025dd5d8633b5d04628314f6c71d'
    # 【要修正】インスタグラムビジネスアカウントID
    config['instagram_account_id'] = "168307399273709"
    # 【要修正】グラフバージョン
    config["version"]              = 'v15.0'
    # 【修正不要】graphドメイン
    config["graph_domain"]         = 'https://graph.facebook.com/'
    # 【修正不要】エンドポイント
    config["endpoint_base"]        = config["graph_domain"]+config["version"] + '/'
    # 出力
    return config

# APIリクエスト用の関数
def InstaApiCall(url, params, request_type):
    
    # リクエスト
    if request_type == 'POST' :
        # POST
        req = requests.post(url,params)
    else :
        # GET
        req = requests.get(url,params)
    
    # レスポンス
    res = dict()
    res["url"] = url
    res["endpoint_params"]        = params
    res["endpoint_params_pretty"] = json.dumps(params, indent=4)
    res["json_data"]              = json.loads(req.content)
    res["json_data_pretty"]       = json.dumps(res["json_data"], indent=4)
    
    # 出力
    return res

def debugAT(params):
    # エンドポイントに送付するパラメータ
    Params = dict()
    Params["input_token"]  = params["access_token"]
    Params["access_token"] = params["access_token"]
    # エンドポイントURL
    url = params["graph_domain"] + "/debug_token"
    # 戻り値
    return InstaApiCall(url, Params, 'GET')

# リクエスト
params   = basic_info()       # リクエストパラメータ
response = debugAT(params)    # レスポンス

# レスポンス
pprint(response)

# インスタグラムユーザー名からフォロワー数を取得
ig_username = 'nintendo_jp'

def get_user_media_stats(params, ig_username):
    """
    ***********************************************************************************
    【APIのエンドポイント】
    "https://graph.facebook.com/v14.0/17841405309211844?fields=business_discovery.username('ig_username'){followers_count,media_count}&access_token={access-token}"
    ***********************************************************************************
    """
    
    # エンドポイントに送付するパラメータ
    Params = dict()
    Params['user_id']      = params['instagram_account_id']
    Params['access_token'] = params['access_token']
    Params['fields']       = 'business_discovery.username(' + ig_username + '){followers_count,media_count,media{comments_count,like_count}}'
    # エンドポイントURL
    url = params['endpoint_base'] + Params['user_id']
    # 出力
    return InstaApiCall(url, Params, 'GET')
# リクエストパラメータ
params      = basic_info()                                # リクエストパラメータ
response    = get_user_media_stats(params, ig_username)   # レスポンス

# 出力
pprint(response)