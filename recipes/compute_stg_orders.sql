create
or replace view stg_orders as (
    with orde as (
        select
            id as order_id,
            user_id as customer_id,
            order_date,
            status
        from
            raw.jaffle_shop.ORDERS
    )
    select
        *
    from
        orde
);
