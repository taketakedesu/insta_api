import requests
import json
import datetime
from pprint import pprint

# Instagram Graph APIの認証用関数を作成
def basic_info():
    # 初期
    config = dict()
    # 【要修正】アクセストークン
    config["access_token"]         = 'EAAIWrzRNhqMBAOux5jwyrGZAy5nz1BtspwtJFffTOKLppxZB5vgdozU10fT7skuWwQCGtZAWYqLJf7lPYi7CgkZBEBuwAnesI8Y9pZCZANAKFp3s5XhssadsSwQDPGciQ3NZBOC8EkeSUmSpmOlTsYSTsnjolWgFr60r8SCiDFa5JyMMTxdZCIy7'
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

    import requests
import json
import datetime
from pprint import pprint

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
print("no changes")