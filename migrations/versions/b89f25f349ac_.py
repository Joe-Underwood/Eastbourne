"""empty message

Revision ID: b89f25f349ac
Revises: de27edcdef73
Create Date: 2021-04-12 17:03:38.822521

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b89f25f349ac'
down_revision = 'de27edcdef73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('billing', sa.Column('linked_invoice_id', sa.Integer(), nullable=True))
    op.drop_constraint('billing_ibfk_2', 'billing', type_='foreignkey')
    op.create_foreign_key(None, 'billing', 'billing', ['linked_invoice_id'], ['id'])
    op.drop_column('billing', 'linked_invoice')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('billing', sa.Column('linked_invoice', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'billing', type_='foreignkey')
    op.create_foreign_key('billing_ibfk_2', 'billing', 'billing', ['linked_invoice'], ['id'])
    op.drop_column('billing', 'linked_invoice_id')
    # ### end Alembic commands ###
