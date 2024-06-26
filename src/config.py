from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig:
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    ECHO: bool

    @property
    def default_asyncpg_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class WebDriverConfig:
    WEB_DRIVER_TIME_OUT: int


class FarPostServiceConfig:
    FAR_POST_URL: str


class Config(BaseSettings, WebDriverConfig, FarPostServiceConfig, DatabaseConfig):
    model_config = SettingsConfigDict(env_file=".env")


config = Config()
