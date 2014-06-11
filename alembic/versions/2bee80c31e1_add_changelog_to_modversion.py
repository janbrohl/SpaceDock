"""Add changelog to ModVersion

Revision ID: 2bee80c31e1
Revises: 3c9f83ee88c
Create Date: 2014-06-11 14:59:34.261896

"""

# revision identifiers, used by Alembic.
revision = '2bee80c31e1'
down_revision = '3c9f83ee88c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('modversion', sa.Column('changelog', sa.Unicode(length=1024), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('modversion', 'changelog')
    ### end Alembic commands ###
