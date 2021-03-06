"""account_confirmation

Revision ID: 790ca16ec37b
Revises: fb5f89ab61d7
Create Date: 2017-04-24 13:47:30.583692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '790ca16ec37b'
down_revision = 'fb5f89ab61d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
