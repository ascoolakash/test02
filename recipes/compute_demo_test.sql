create or replace transient table demo_test
         as
        (

with customers as (
    select * from stg_customers
),

orders as (
    select * from stg_orders
),

payments as (
    select * from stg_payments
),


final as (

    select 
    orders.order_id,
    customers.customer_id,
    customers.first_name,
    customers.last_name,
    orders.order_date,
    orders.status,
    payments.payment_id,
    payments.payment_method,
    payments.amount,
    payments.created_at
        
    from customers

    left join orders using (customer_id)
    left join payments using (order_id)
   

)

select 
    *
from final
        );
      
  
