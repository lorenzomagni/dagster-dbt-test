
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='view') }}


with source_data as (

select committente as id from page3.aaa_contratti_manuali

)

select *
from source_data
