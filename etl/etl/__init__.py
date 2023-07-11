from dagster import (
    AssetSelection,
    Definitions,
    define_asset_job,
    ScheduleDefinition,
    load_assets_from_modules,
)

from . import assets

btc_job = define_asset_job("btc_job", selection=AssetSelection.all())

all_assets = load_assets_from_modules([assets])

btc_schedule = ScheduleDefinition(
    job=btc_job,
    cron_schedule="0 * * * *",  # every hour
)

defs = Definitions(
    assets=all_assets,
    jobs=[btc_job],
)
