from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: PostgresDsn | None = None
    celery_brocker_dsn: RedisDsn | None = None
    celery_is_active: bool = False
    secret_key: str = "VMcqXhjBcluujpGnOU8ymK0dYMsIz6Ho7aWRdu6wqsZMybWPYxJManmHRyWR4QVH"
    access_token_expire_days: int = 1

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


CONFIG = Settings()
