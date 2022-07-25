{{ config(materialized='view') }}


with source_data as (

select committente as id from page3.aaa_contratti_manuali

)

select *
from source_data
