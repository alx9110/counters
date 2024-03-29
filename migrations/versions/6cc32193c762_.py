"""empty message

Revision ID: 6cc32193c762
Revises: 
Create Date: 2019-11-18 23:53:52.311023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cc32193c762'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('counters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('unit_of_measurement', sa.String(length=32), nullable=False),
    sa.Column('place_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('places',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('geo', sa.String(length=64), nullable=True),
    sa.Column('adress', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('places')
    op.drop_table('counters')
    # ### end Alembic commands ###
