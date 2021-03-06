"""added check in/check out fields to price_list_settings table

Revision ID: 0f4645f9b2c0
Revises: b89f25f349ac
Create Date: 2021-04-23 11:57:00.364281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f4645f9b2c0'
down_revision = 'b89f25f349ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('price__list__settings', sa.Column('check_in_time', sa.Time(), nullable=True))
    op.add_column('price__list__settings', sa.Column('check_out_time', sa.Time(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('price__list__settings', 'check_out_time')
    op.drop_column('price__list__settings', 'check_in_time')
    # ### end Alembic commands ###
