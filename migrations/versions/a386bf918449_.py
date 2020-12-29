"""empty message

Revision ID: a386bf918449
Revises: 09aa510c609a
Create Date: 2020-12-15 19:01:47.665646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a386bf918449'
down_revision = '09aa510c609a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('future__price__list', sa.Column('price_2_weeks', sa.Numeric(precision=10, scale=2), nullable=True))
    op.add_column('future__price__list', sa.Column('price_3_weeks', sa.Numeric(precision=10, scale=2), nullable=True))
    op.add_column('future__price__list', sa.Column('price_4_weeks', sa.Numeric(precision=10, scale=2), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('future__price__list', 'price_4_weeks')
    op.drop_column('future__price__list', 'price_3_weeks')
    op.drop_column('future__price__list', 'price_2_weeks')
    # ### end Alembic commands ###