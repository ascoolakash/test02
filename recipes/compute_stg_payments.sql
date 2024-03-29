
  create or replace   view stg_payments
  
   as (
    select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    status,
    
    (amount / 100)::numeric(16, 2)
  as amount,
    created as created_at
from raw.stripe.payment
  );

