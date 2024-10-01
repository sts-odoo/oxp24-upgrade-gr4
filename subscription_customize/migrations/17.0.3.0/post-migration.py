def migrate(cr, version):
    cr.execute(
        """
        UPDATE sale_order so
            SET parent_id = ss.parent_id
        FROM sale_subscription ss
        WHERE ss.new_sale_order_id = so.id
        """
    )
    cr.execute(
        """
        UPDATE sale_order so
            SET child_recurring_total = ss.child_recurring_total
        FROM sale_subscription ss
        WHERE ss.new_sale_order_id = so.id
        """
    )
    cr.execute(
        """
        UPDATE sale_order so
            SET amount_at_start = ss.amount_at_start
        FROM sale_subscription ss
        WHERE ss.new_sale_order_id = so.id
        """
    )