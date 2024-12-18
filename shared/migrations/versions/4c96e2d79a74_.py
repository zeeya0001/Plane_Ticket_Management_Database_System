"""empty message

Revision ID: 4c96e2d79a74
Revises: ebf3002d67ae
Create Date: 2024-11-25 11:20:25.914024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c96e2d79a74'
down_revision = 'ebf3002d67ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_constraint('payment_ibfk_1', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.create_foreign_key('payment_ibfk_1', 'booking', ['Booking_ID'], ['Booking_ID'])

    # ### end Alembic commands ###
