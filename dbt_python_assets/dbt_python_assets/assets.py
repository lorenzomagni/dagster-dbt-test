from dagster import AssetGroup, load_assets_from_current_module, repository
from dagster_dbt import dbt_cli_resource, load_assets_from_dbt_project
from dagster.core.execution.with_resources import with_resources
from dagster.utils import file_relative_path


#Define the nedeed paths as variables
DBT_PROJECT_DIR = file_relative_path(__file__, "../dbt_project")
DBT_PROFILES_DIR = file_relative_path(__file__, "../dbt_project/")
DBT_CONFIG = {"project_dir": DBT_PROJECT_DIR, "profiles_dir": DBT_PROFILES_DIR}

#Load the assets from dbt_project automatically
dbt_assets = load_assets_from_dbt_project(project_dir=DBT_PROJECT_DIR)

#Group the defined assets, in this case we only have one (dbt_assets)
analytics_assets = AssetGroup(
    dbt_assets,
    resource_defs={
        "dbt":dbt_cli_resource.configured(
            {"project_dir": DBT_PROJECT_DIR},
        )
    },
)

# all of the resources needed for interacting with our tools
resource_defs = {
    "dbt": dbt_cli_resource.configured(DBT_CONFIG),
}

@repository
def example_repo():
    from dagster import define_asset_job

    return with_resources(
        load_assets_from_current_module(),
        resource_defs=resource_defs,
    ) + [define_asset_job("all")]