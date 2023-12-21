 
  create or replace   view stg_orders
  
   as (
    with order as (

    select
        id as order_id,
        user_id as customer_id,
        order_date,
        status

    from orders

)

select * from order
  );

