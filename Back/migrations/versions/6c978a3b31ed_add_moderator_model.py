"""add Moderator model

Revision ID: 6c978a3b31ed
Revises: 6b7ca7f4c8b8
Create Date: 2024-06-05 07:49:46.797373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c978a3b31ed'
down_revision: Union[str, None] = '6b7ca7f4c8b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moderator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('passanger_to_order',
    sa.Column('passanger_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['passanger_id'], ['passanger.id'], )
    )
    op.drop_table('association')
    op.drop_index('ix_country_id', table_name='country')
    op.drop_index('ix_region_id', table_name='region')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_region_id', 'region', ['id'], unique=False)
    op.create_index('ix_country_id', 'country', ['id'], unique=False)
    op.create_table('association',
    sa.Column('passanger_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name='association_order_id_fkey'),
    sa.ForeignKeyConstraint(['passanger_id'], ['passanger.id'], name='association_passanger_id_fkey')
    )
    op.drop_table('passanger_to_order')
    op.drop_table('moderator')
    # ### end Alembic commands ###
