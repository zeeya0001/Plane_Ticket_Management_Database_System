"""empty message

Revision ID: b392d5a6bc1e
Revises: 4c96e2d79a74
Create Date: 2024-12-01 04:01:49.457166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b392d5a6bc1e'
down_revision = '4c96e2d79a74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('passenger', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seat_number', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('passenger', schema=None) as batch_op:
        batch_op.drop_column('seat_number')

    # ### end Alembic commands ###