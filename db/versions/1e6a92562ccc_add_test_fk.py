"""add test fk

Revision ID: 1e6a92562ccc
Revises: 3be8e13f0db8
Create Date: 2017-01-26 08:46:43.805994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e6a92562ccc'
down_revision = '3be8e13f0db8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test_fk',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('paid_amount', sa.Integer(), nullable=False),
        sa.Column('sold_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.add_column('sale', sa.Column('test_fk_id', sa.Integer(), nullable=False))
    op.create_foreign_key('sale_test_fk_id_fkey', 'sale', 'test_fk', ['test_fk_id'], ['id'])


def downgrade():
    op.drop_constraint('sale_test_fk_id_fkey', 'sale', type_='foreignkey')
    op.drop_column('sale', 'test_fk_id')
    op.drop_table('test_fk')
