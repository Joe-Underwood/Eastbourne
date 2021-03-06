"""added invoice_status and linked_invoice_reference columns to Billing model

Revision ID: c17a67ca8134
Revises: 1a3bcda2c84d
Create Date: 2021-04-12 15:28:01.830960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c17a67ca8134'
down_revision = '1a3bcda2c84d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('billing', sa.Column('invoice_status', sa.Enum('NOT_SENT', 'SENT', 'OVERDUE', 'PAID', name='invoice_status'), nullable=True))
    op.add_column('billing', sa.Column('linked_invoice_reference', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('billing', 'linked_invoice_reference')
    op.drop_column('billing', 'invoice_status')
    # ### end Alembic commands ###
