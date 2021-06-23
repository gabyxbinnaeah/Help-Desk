"""add name column

Revision ID: b6fe63049c1b
Revises: 4928a252b617
Create Date: 2021-06-23 14:52:50.119453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6fe63049c1b'
down_revision = '4928a252b617'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('name', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'name')
    # ### end Alembic commands ###
