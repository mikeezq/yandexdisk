import os
from alembic.config import CommandLine, Config
from file_manager.utils.pg import DEFAULT_PG_URL
from pathlib import Path

PROJECT_PATH = Path(__file__).parent.parent.resolve()


def main():
    alembic = CommandLine()
    alembic.parser.add_argument("--pg-url", default=os.getenv("ANALYZER_PG_URL", DEFAULT_PG_URL),
                                help="Postgres db url")
    options = alembic.parser.parse_args()

    if not os.path.isabs(options.config):
        options.config = os.path.join(PROJECT_PATH, options.config)

    config = Config(file_=options.config, ini_section=options.name, cmd_opts=options)
    print(f"Alembic info {options.config=}, {options.name=}")
    config.set_main_option("sqlalchemy.url", options.pg_url)

    alembic_location = config.get_main_option('script_location')
    if not os.path.isabs(alembic_location):
        config.set_main_option('script_location',
                               os.path.join(PROJECT_PATH, alembic_location))

    exit(alembic.run_cmd(config, options))


if __name__ == "__main__":
    main()
