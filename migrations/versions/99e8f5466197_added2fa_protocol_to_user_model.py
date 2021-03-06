"""added2FA protocol to User model

Revision ID: 99e8f5466197
Revises: 2f4ed0d60ebe
Create Date: 2021-07-10 21:47:36.807634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99e8f5466197'
down_revision = '2f4ed0d60ebe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('otp_secret', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'otp_secret')
    # ### end Alembic commands ###
