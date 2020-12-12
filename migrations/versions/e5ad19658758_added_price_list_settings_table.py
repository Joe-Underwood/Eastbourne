"""added Price_List_Settings table

Revision ID: e5ad19658758
Revises: 23d909e3d3c6
Create Date: 2020-12-12 18:29:33.503135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5ad19658758'
down_revision = '23d909e3d3c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('price__list__settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('discount_2_weeks', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('discount_3_weeks', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('discount_4_weeks', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('active_prices_range', sa.Date(), nullable=True),
    sa.Column('future_prices_range', sa.Date(), nullable=True),
    sa.Column('default_changeover_day', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('price__list__settings')
    # ### end Alembic commands ###
