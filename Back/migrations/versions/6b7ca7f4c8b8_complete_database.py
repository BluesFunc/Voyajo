"""Complete database

Revision ID: 6b7ca7f4c8b8
Revises: a01f08132674
Create Date: 2024-06-05 06:29:22.954057

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import  sqlalchemy_utils

# revision identifiers, used by Alembic.
revision: str = '6b7ca7f4c8b8'
down_revision: Union[str, None] = 'a01f08132674'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_country_id'), 'country', ['id'], unique=False)
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_id'), 'customer', ['id'], unique=False)
    op.create_table('extranet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_extranet_id'), 'extranet', ['id'], unique=False)
    op.create_table('region',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_region_id'), 'region', ['id'], unique=False)
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_city_id'), 'city', ['id'], unique=False)
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('company_link', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('company_type', sa.Enum('AIRLINE', 'RAILWAY', 'BUS', name='companytype'), nullable=False),
    sa.Column('extranet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['extranet_id'], ['extranet.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_company_id'), 'company', ['id'], unique=False)
    op.create_table('passanger',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('second_name', sa.String(), nullable=True),
    sa.Column('gender', sa.Enum('male', 'female', 'other', name='customergender'), nullable=True),
    sa.Column('passport_series', sa.String(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('station',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('station_type', sa.Enum('BUS', 'TRAIN', 'AIRPORT', name='stationtype'), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_station_id'), 'station', ['id'], unique=False)
    op.create_table('fare',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.DECIMAL(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('departure_station_id', sa.Integer(), nullable=True),
    sa.Column('arrival_station_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['arrival_station_id'], ['station.id'], ),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['departure_station_id'], ['station.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fare_id'), 'fare', ['id'], unique=False)
    op.create_table('ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fare_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['fare_id'], ['fare.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticket_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('ticket_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('ticket_count', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('passanger_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['passanger_id'], ['passanger.id'], )
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('association')
    op.drop_table('order')
    op.drop_table('trip')
    op.drop_table('ticket')
    op.drop_index(op.f('ix_fare_id'), table_name='fare')
    op.drop_table('fare')
    op.drop_index(op.f('ix_station_id'), table_name='station')
    op.drop_table('station')
    op.drop_table('passanger')
    op.drop_index(op.f('ix_company_id'), table_name='company')
    op.drop_table('company')
    op.drop_index(op.f('ix_city_id'), table_name='city')
    op.drop_table('city')
    op.drop_index(op.f('ix_region_id'), table_name='region')
    op.drop_table('region')
    op.drop_index(op.f('ix_extranet_id'), table_name='extranet')
    op.drop_table('extranet')
    op.drop_index(op.f('ix_customer_id'), table_name='customer')
    op.drop_table('customer')
    op.drop_table('admin')
    op.drop_index(op.f('ix_country_id'), table_name='country')
    op.drop_table('country')
    # ### end Alembic commands ###
