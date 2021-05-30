"""added columns to Delete_Booking to match Booking

Revision ID: 660eeb0a29d5
Revises: 5ff81f5918f2
Create Date: 2021-05-30 17:12:02.789788

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '660eeb0a29d5'
down_revision = '5ff81f5918f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('delete__booking', sa.Column('multi_week_discount', sa.Numeric(precision=10, scale=2), nullable=True))
    op.add_column('delete__booking', sa.Column('status', sa.Enum('AWAITING_CONFIRMATION', 'ACCEPTED', 'REJECTED', 'ACTIVE', 'INACTIVE', name='status'), nullable=True))
    op.add_column('delete__booking', sa.Column('total', sa.Numeric(precision=10, scale=2), nullable=True))
    op.drop_column('delete__booking', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('delete__booking', sa.Column('price', mysql.DECIMAL(precision=10, scale=2), nullable=True))
    op.drop_column('delete__booking', 'total')
    op.drop_column('delete__booking', 'status')
    op.drop_column('delete__booking', 'multi_week_discount')
    # ### end Alembic commands ###
