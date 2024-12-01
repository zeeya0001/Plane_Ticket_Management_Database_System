"""empty message

Revision ID: 6231e616b850
Revises: bbfa4a76fd5d
Create Date: 2024-12-02 02:33:35.275352

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6231e616b850'
down_revision = 'bbfa4a76fd5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('services')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('services',
    sa.Column('Service_ID', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Service_name', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('Airport_ID', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('Booking_ID', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('about_service', mysql.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['Airport_ID'], ['airport.AP_CODE'], name='services_ibfk_1'),
    sa.ForeignKeyConstraint(['Booking_ID'], ['booking.Booking_ID'], name='services_ibfk_2'),
    sa.PrimaryKeyConstraint('Service_ID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###