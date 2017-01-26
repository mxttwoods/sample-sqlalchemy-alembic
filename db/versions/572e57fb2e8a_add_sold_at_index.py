"""add sold_at index

Revision ID: 572e57fb2e8a
Revises: 1e6a92562ccc
Create Date: 2017-01-26 09:01:21.759319

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '572e57fb2e8a'
down_revision = '1e6a92562ccc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index(op.f('ix_sale_sold_at'), 'sale', ['sold_at'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_sale_sold_at'), table_name='sale')
