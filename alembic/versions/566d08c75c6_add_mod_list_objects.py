"""Add mod list objects

Revision ID: 566d08c75c6
Revises: 18af22fa9e4
Create Date: 2014-09-25 11:19:16.916489

"""

# revision identifiers, used by Alembic.
revision = '566d08c75c6'
down_revision = '18af22fa9e4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('modlist', sa.Column('background', sa.String(length=32), nullable=True))
    op.add_column('modlist', sa.Column('bgOffsetY', sa.Integer(), nullable=True))
    op.add_column('modlist', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('modlist', sa.Column('description', sa.Unicode(length=100000), nullable=True))
    op.add_column('modlist', sa.Column('name', sa.Unicode(length=1024), nullable=True))
    op.add_column('modlist', sa.Column('short_description', sa.Unicode(length=1000), nullable=True))
    op.add_column('modlistitem', sa.Column('mod_list_id', sa.Integer(), nullable=True))
    op.add_column('modlistitem', sa.Column('sort_index', sa.Integer(), nullable=True))
    op.drop_column('modlistitem', 'list_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('modlistitem', sa.Column('list_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('modlistitem', 'sort_index')
    op.drop_column('modlistitem', 'mod_list_id')
    op.drop_column('modlist', 'short_description')
    op.drop_column('modlist', 'name')
    op.drop_column('modlist', 'description')
    op.drop_column('modlist', 'created')
    op.drop_column('modlist', 'bgOffsetY')
    op.drop_column('modlist', 'background')
    ### end Alembic commands ###
