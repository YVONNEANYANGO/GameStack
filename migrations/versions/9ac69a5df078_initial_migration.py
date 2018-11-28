"""Initial Migration

Revision ID: 9ac69a5df078
Revises: 545c88e5c5b5
Create Date: 2018-11-28 17:54:02.102129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ac69a5df078'
down_revision = '545c88e5c5b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
