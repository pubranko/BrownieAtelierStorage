from decouple import config, AutoConfig

# .envファイルが存在するパスを指定。実行時のカレントディレクトリに.envを配置している場合、以下の設定不要。
# config = AutoConfig(search_path="./shared")

# Azure Storage設定
AZURE_STORAGE__ACCOUNT_NAME: str = str(
    config("AZURE_STORAGE__ACCOUNT_NAME", default="brownieatelierdata")
)
AZURE_STORAGE__ACCOUNT_KEY: str = str(config("AZURE_STORAGE__ACCOUNT_KEY", default=""))
AZURE_STORAGE__CONNECTION_STRING: str = str(
    config("AZURE_STORAGE__CONNECTION_STRING", default="")
)
AZURE_STORAGE__FILE_SHARE: str = str(
    config("AZURE_STORAGE__FILE_SHARE", default="controller")
)
AZURE_STORAGE__QUE_NAME: str = str(config("AZURE_STORAGE__QUE_NAME", default=""))
AZURE_STORAGE__BLOB_CONTAINER_NAME: str = str(
    config("AZURE_STORAGE__BLOB_CONTAINER_NAME", default="brownie-atelier")
)
AZURE_STORAGE__BLOB_FILE_NAME: str = str(
    config("AZURE_STORAGE__BLOB_FILE_NAME", default="container-stop-coomand-execute")
)
