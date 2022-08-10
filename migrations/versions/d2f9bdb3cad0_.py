"""empty message

Revision ID: d2f9bdb3cad0
Revises: 684d1a33970b
Create Date: 2022-08-08 20:00:25.091356

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd2f9bdb3cad0'
down_revision = '684d1a33970b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('favorite__planets', 'planet_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorite__planets', sa.Column('planet_name', mysql.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###