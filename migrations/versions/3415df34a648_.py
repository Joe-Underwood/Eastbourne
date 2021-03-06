"""empty message

Revision ID: 3415df34a648
Revises: c9e6034cf14d
Create Date: 2021-07-12 16:42:36.496284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3415df34a648'
down_revision = 'c9e6034cf14d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('delete__booking', sa.Column('booking_type', sa.Enum('STANDARD', 'OWNER', 'EXTERNAL', name='booking_type'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('delete__booking', 'booking_type')
    # ### end Alembic commands ###
