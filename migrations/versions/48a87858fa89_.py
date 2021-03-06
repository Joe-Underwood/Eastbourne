"""empty message

Revision ID: 48a87858fa89
Revises: 4cea9aa0790a
Create Date: 2021-03-28 16:03:25.181051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48a87858fa89'
down_revision = '4cea9aa0790a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cancellation__breakpoint', sa.Column('check_in', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cancellation__breakpoint', 'check_in')
    # ### end Alembic commands ###
