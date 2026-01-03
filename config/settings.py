# from dotenv import load_dotenv
# load_dotenv()  # MUST be at top-level
# from pydantic_settings import BaseSettings, SettingsConfigDict
#
# class Settings(BaseSettings):
#     vectorstore_path: str = f'D:\\langchain-research-assistant\\app\\data\\vectorstore'
#     user_agent: str | None = None
#     google_api_key: str | None = None
#
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="forbid"
#     )
#
# settings = Settings()
# from pydantic_settings import BaseSettings
#
# class Settings(BaseSettings):
#     llm_provider: str = "gemini"
#     embedding_provider: str = "hf"
#     vectorstore_path: str = f'D:\\langchain-research-assistant\\app\\data\\vectorstore'
#
#     class Config:
#         env_file = ".env"
#
# settings = Settings()



from dotenv import load_dotenv
load_dotenv()

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Paths
    vectorstore_path: str = "D:/langchain-research-assistant/app/data/vectorstore"

    # HTTP / identity
    user_agent: str | None = None

    # LLM / embeddings
    google_api_key: str | None = None
    llm_provider: str = "gemini"
    embedding_provider: str = "hf"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="forbid"
    )

settings = Settings()

