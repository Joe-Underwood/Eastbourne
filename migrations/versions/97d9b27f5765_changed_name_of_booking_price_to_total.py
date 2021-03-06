"""changed name of Booking.price to total

Revision ID: 97d9b27f5765
Revises: 81fc4e16ce9b
Create Date: 2021-05-17 11:19:40.317564

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '97d9b27f5765'
down_revision = '81fc4e16ce9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ##
    op.alter_column('booking', 'price', existing_type=sa.Numeric(precision=10, scale=2), existing_server_default=None, existing_nullable=True, new_column_name='total')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('booking', 'total', existing_type=sa.Numeric(precision=10, scale=2), existing_server_default=None, existing_nullable=True, new_column_name='price')
    # ### end Alembic commands ###
