from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str
    server_port: int
    database_url: str
    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_exp_time: int = 60 * 60

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
