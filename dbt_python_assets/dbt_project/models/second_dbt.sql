{{ config(materialized='view') }}

select *
from {{ ref("first_dbt") }}
