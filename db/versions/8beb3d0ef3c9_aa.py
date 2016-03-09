"""aa

Revision ID: 8beb3d0ef3c9
Revises: 58e1f3f99aaf
Create Date: 2016-03-09 19:04:04.293101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8beb3d0ef3c9'
down_revision = '58e1f3f99aaf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('phone', sa.String(length=15), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'item',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('price', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'sale',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('account_id', sa.Integer(), nullable=False),
        sa.Column('item_id', sa.Integer(), nullable=False),
        sa.Column('paid_amount', sa.Integer(), nullable=False),
        sa.Column('sold_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
        sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('sale')
    op.drop_table('item')
    op.drop_table('account')
