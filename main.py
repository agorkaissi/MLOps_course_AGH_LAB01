import os
import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml


def load_secrets_to_env(secrets_file: str) -> None:
    with open(secrets_file, "r") as f:
        secrets = yaml.safe_load(f)

    for key, value in secrets.items():
        os.environ[key] = str(value)


def export_envs(environment: str = "dev") -> None:
    allowed = {"dev", "test", "prod"}

    if environment not in allowed:
        raise ValueError(
            f"Invalid environment '{environment}'. Must be one of {allowed}"
        )

    env_file = os.path.join("config", f".env.{environment}")
    if os.path.exists(env_file):
        load_dotenv(dotenv_path=env_file)
        print(f"Loaded legacy .env variables from '{env_file}'")

    secrets_file = "secrets.yaml"  # lub secrets.{environment}.yaml
    load_secrets_to_env(secrets_file)
    print(f"Loaded secrets from '{secrets_file}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
