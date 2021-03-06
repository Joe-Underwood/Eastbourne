"""empty message

Revision ID: b5d2e7331630
Revises: 7b80e7ee3f88
Create Date: 2021-07-15 14:39:07.911088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b5d2e7331630'
down_revision = '7b80e7ee3f88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('billing', 'invoice_status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('billing', sa.Column('invoice_status', mysql.ENUM('DRAFT', 'ACTIVE', 'OVERDUE', 'PAID', 'INACTIVE', collation='utf8_bin'), nullable=True))
    # ### end Alembic commands ###
