"""empty message

Revision ID: 724c1a600c49
Revises: 
Create Date: 2024-11-15 15:54:19.146033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '724c1a600c49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('airline',
    sa.Column('Airline_ID', sa.String(length=15), nullable=False),
    sa.Column('Years_of_Service', sa.Integer(), nullable=False),
    sa.Column('Airline_name', sa.String(length=100), nullable=False),
    sa.Column('Operating_Region', sa.String(length=50), nullable=False),
    sa.Column('Contact_number', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('Airline_ID'),
    sa.UniqueConstraint('Contact_number')
    )
    op.create_table('airport',
    sa.Column('AP_CODE', sa.String(length=10), nullable=False),
    sa.Column('Airport_name', sa.String(length=100), nullable=False),
    sa.Column('Airport_location', sa.String(length=50), nullable=False),
    sa.Column('facilities', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('AP_CODE')
    )
    op.create_table('flight',
    sa.Column('Flight_ID', sa.Integer(), nullable=False),
    sa.Column('Flight_name', sa.String(length=50), nullable=False),
    sa.Column('Departure_Time', sa.DateTime(), nullable=False),
    sa.Column('Arrival_Time', sa.DateTime(), nullable=False),
    sa.Column('Year_of_Services', sa.Integer(), nullable=False),
    sa.Column('Airline_name', sa.String(length=50), nullable=False),
    sa.Column('Origin_AP_name', sa.String(length=100), nullable=False),
    sa.Column('Destination_AP_name', sa.String(length=100), nullable=False),
    sa.Column('Flight_type', sa.String(length=20), nullable=False),
    sa.Column('total_seats_available', sa.Integer(), nullable=False),
    sa.Column('Class', sa.String(length=20), nullable=False),
    sa.Column('Flight_Status', sa.String(length=20), nullable=False),
    sa.Column('Flight_Location', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('Flight_ID')
    )
    op.create_table('passenger',
    sa.Column('Passenger_ID', sa.Integer(), nullable=False),
    sa.Column('First_name', sa.String(length=20), nullable=False),
    sa.Column('Last_name', sa.String(length=20), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('disabilities', sa.String(length=20), nullable=True),
    sa.Column('Email', sa.String(length=100), nullable=False),
    sa.Column('Mobile_Number', sa.String(length=10), nullable=False),
    sa.Column('Passport_number', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('Passenger_ID'),
    sa.UniqueConstraint('Email'),
    sa.UniqueConstraint('Mobile_Number'),
    sa.UniqueConstraint('Passport_number')
    )
    op.create_table('booking',
    sa.Column('Booking_ID', sa.Integer(), nullable=False),
    sa.Column('Flight_ID', sa.Integer(), nullable=False),
    sa.Column('Passenger_ID', sa.Integer(), nullable=False),
    sa.Column('Origin_AP_name', sa.String(length=100), nullable=False),
    sa.Column('Destination_AP_name', sa.String(length=100), nullable=False),
    sa.Column('Journey_date', sa.DATE(), nullable=False),
    sa.Column('Gender', sa.String(length=7), nullable=False),
    sa.Column('Age', sa.Integer(), nullable=False),
    sa.Column('Seat_number', sa.String(length=10), nullable=False),
    sa.Column('Boarding_time', sa.DateTime(), nullable=True),
    sa.Column('Check_in_time', sa.DateTime(), nullable=True),
    sa.Column('Class', sa.String(length=10), nullable=False),
    sa.Column('Price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('Status', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['Flight_ID'], ['flight.Flight_ID'], ),
    sa.ForeignKeyConstraint(['Passenger_ID'], ['passenger.Passenger_ID'], ),
    sa.PrimaryKeyConstraint('Booking_ID'),
    sa.UniqueConstraint('Seat_number')
    )
    op.create_table('notification',
    sa.Column('Notification_ID', sa.Integer(), nullable=False),
    sa.Column('Passenger_ID', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.Column('notification_type', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['Passenger_ID'], ['passenger.Passenger_ID'], ),
    sa.PrimaryKeyConstraint('Notification_ID')
    )
    op.create_table('review',
    sa.Column('Review_ID', sa.Integer(), nullable=False),
    sa.Column('Passenger_ID', sa.Integer(), nullable=False),
    sa.Column('Rating', sa.Integer(), nullable=False),
    sa.Column('Content', sa.String(length=255), nullable=False),
    sa.Column('Date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['Passenger_ID'], ['passenger.Passenger_ID'], ),
    sa.PrimaryKeyConstraint('Review_ID')
    )
    op.create_table('seat_matrix',
    sa.Column('seat_id', sa.Integer(), nullable=False),
    sa.Column('flight_id', sa.Integer(), nullable=False),
    sa.Column('passenger_id', sa.Integer(), nullable=True),
    sa.Column('seat_number', sa.String(length=5), nullable=False),
    sa.Column('seat_class', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['flight_id'], ['flight.Flight_ID'], ),
    sa.ForeignKeyConstraint(['passenger_id'], ['passenger.Passenger_ID'], ),
    sa.PrimaryKeyConstraint('seat_id'),
    sa.UniqueConstraint('flight_id', 'seat_number', name='unique_flight_seat')
    )
    op.create_table('cancellation',
    sa.Column('Cancellation_ID', sa.Integer(), nullable=False),
    sa.Column('Booking_ID', sa.Integer(), nullable=False),
    sa.Column('Request_time', sa.DateTime(), nullable=False),
    sa.Column('Issue_time', sa.DateTime(), nullable=False),
    sa.Column('Amount_refunded', sa.Integer(), nullable=False),
    sa.Column('Reason', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['Booking_ID'], ['booking.Booking_ID'], ),
    sa.PrimaryKeyConstraint('Cancellation_ID')
    )
    op.create_table('payment',
    sa.Column('Payment_ID', sa.Integer(), nullable=False),
    sa.Column('Amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('Payment_Method', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('Status', sa.String(length=10), nullable=False),
    sa.Column('Booking_ID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Booking_ID'], ['booking.Booking_ID'], ),
    sa.PrimaryKeyConstraint('Payment_ID')
    )
    op.create_table('services',
    sa.Column('Service_ID', sa.Integer(), nullable=False),
    sa.Column('Service_name', sa.String(length=100), nullable=False),
    sa.Column('Airport_ID', sa.String(length=10), nullable=False),
    sa.Column('Booking_ID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Airport_ID'], ['airport.AP_CODE'], ),
    sa.ForeignKeyConstraint(['Booking_ID'], ['booking.Booking_ID'], ),
    sa.PrimaryKeyConstraint('Service_ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('services')
    op.drop_table('payment')
    op.drop_table('cancellation')
    op.drop_table('seat_matrix')
    op.drop_table('review')
    op.drop_table('notification')
    op.drop_table('booking')
    op.drop_table('passenger')
    op.drop_table('flight')
    op.drop_table('airport')
    op.drop_table('airline')
    # ### end Alembic commands ###
