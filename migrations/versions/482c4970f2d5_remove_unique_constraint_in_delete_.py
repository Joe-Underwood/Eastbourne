"""remove unique constraint in Delete_Price_List model

Revision ID: 482c4970f2d5
Revises: 66d3801ca27a
Create Date: 2021-01-29 18:01:57.399280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '482c4970f2d5'
down_revision = '66d3801ca27a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('start_date', table_name='delete__price__list')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('start_date', 'delete__price__list', ['start_date'], unique=True)
    # ### end Alembic commands ###
