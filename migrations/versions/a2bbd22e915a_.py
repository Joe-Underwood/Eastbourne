"""empty message

Revision ID: a2bbd22e915a
Revises: 1cc33578c2ce
Create Date: 2021-05-09 11:37:43.201964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2bbd22e915a'
down_revision = '1cc33578c2ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('progressive_payments', sa.Column('id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('progressive_payments', 'id')
    # ### end Alembic commands ###
